# tif_matcher
Matches .tif images across two directories by image (when your naming is off). We use concurrent.futures to get incredible speedup here (60x faster when I ran the code) 


## Requirements:
```
rasterio
```

## Usage:
```
python3 tif_matcher.py [-h] [--dir1 DIR1] [--dir2 DIR2] [--out_file OUT_FILE] 
                       [--key_word1 KEY_WORD1] [--key_word2 KEY_WORD2]
                       [--normalize] [--verbose]
```
* dir1 (str) -      Input directory 1
* dir2 (str) -      Input directory 2
* out_file (str) -  Name of output file
* key_word1 (str) - Key word to select subset of images in dir1
* key_word2 (str) - Key word to select subset of images in dir2
* normalize -       Normalize images before comparison
* verbose -         Print out each match found
