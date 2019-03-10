# AWAKE GSoC 2019 Evaluation

Author: @Aniq55 (Aniq Ur Rahman)

## Directories and Files
```

eval_test/
|-- data/
|-- out/
|-- library.py
|-- awake_gsoc_eval.ipynb
|-- README.md

```
## `library.py`
#### `file2utc(filepath)`
Converts the hdf filename's first 19 digits to UNIX time in nanoseconds and
returns the timestamp in UTC.

#### `utc2cern(timestamp_utc)`
Converts the UTC timestamp to CERN's local time.

#### `hdf2csv(filepath, output)`
Reads the hdf file and converts it to CSV.

####  `plot_image(im_data, dimensions, im_title= None, output_path= None)`
Plots a 2D matrix as an image and saves it.

#### `linear2matrix(hdf_path, image_path, output)`
Converts the linear dataset into 2D matrix and plots the image.

## `awake_gsoc_eval.ipynb`
Jupter Notebook to demonstrate the usage of `library.py` to accomplish the tasks.

## `data/`
Contains the `.h5` file.

## `out/`
Contains the output files: `csv` and `png`.
 
