import os
import rasterio
import concurrent.futures as cp
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir1', type=str, help='Input dir 1')
parser.add_argument('--dir2', type=str, help='Input dir 2')
parser.add_argument('--out_file', type=str, default='./matched_tifs.json', help='Name of output file')
parser.add_argument('--key_word1', type=str, default='', help='Key word to select only some images from dir1')
parser.add_argument('--key_word2', type=str, default='', help='Key word to select only some images from dir2')
parser.add_argument('--normalize', action='store_true', help='Match normalized images')
parser.add_argument('--verbose', action='store_true', help='Print matches')

args = parser.parse_args()


def match_image(img, image_path, dir2, key_word, normalize=False, verbose=False):
  """
  Find image path in dir2 that matches image in image_path
  """
  for image2 in os.listdir(dir2):
    if key_word not in image2:
      continue
    image2_path = os.path.join(dir2, image2)
    with rasterio.open(image2_path, 'r') as src:
        img2 = src.read()
    if normalize:
      img2=img2/img2.max()
    if (img2 == img).all():
      if args.verbose
      print(image_path, image2_path)
      # return matching sets
      return [image_path, image2_path]
  return None


## Match the two datasets
matches_th = []
matches = []
with cp.ProcessPoolExecutor() as ex:
  for image in os.listdir(args.dir1):
    if args.key_word1 not in image:
      continue
    image_path = os.path.join(args.dir1, image)
    with rasterio.open(image_path, 'r') as src:
      img = src.read()
    if args.normalize:
      img=img/img.max()
    matches_th.append(ex.submit(match_image, img, image_path, args.dir2, args.key_word2, args.normalize, args.verbose))
for match in cp.as_completed(matches_th):
    matches.append(match.result())

with open(args.out_file, 'w') as wf:
  json.dump(matches, wf)
