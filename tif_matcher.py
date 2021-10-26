import os
import rasterio
import matplotlib.pyplot as plt
import concurrent.futures as cp
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir1', type=str, help='')
parser.add_argument('--dir1', type=str, help='')
parser.add_argument('--out_file', type=str, defualt='matched_tifs', help='Name of output file')



def match_image(image_path, dir2):
  """
  Find image path in dir2 that matches image in image_path
  """
  with rasterio.open(image_path, 'r') as src:
      img = src.read()
  for image2 in os.listdir(dir2):
    image2_path = os.path.join(dir1, image2)
    with rasterio.open(image2_path, 'r') as src:
        img2 = src.read()
    if img2 == img:
      print(image_path, image2_path)
      # return matching sets
      return [image_path, image2_path]
  return


## Match the two datasets
matches_th = []
matches = []
with cp.ThreadPoolExecutor() as ex:
  for image in os.listdir(dir1):
    image_path = os.path.join(dir1, image)
    matches_th.append(ex.submit(match_image, image_path, dir2))
for match in cp.as_completed(matches_th):
    matches.append(match.result())


with open(out_file, 'w') as wf:
  json.dump(matches, wf)
