# AWAKE GSoC 2019 Evaluation

Author: @Aniq55 (Aniq Ur Rahman)

## Directories and Files
`eval_test/`
`|-- data/`
`|-- out/`
`|-- library.py`
`|-- awake_gsoc_eval.ipynb`
`|-- README.md`

## `library.py`
### `file2utc`
Converts the hdf filename's first 19 digits to UNIX time in nanoseconds and
returns the timestamp in UTC.

### `utc2cern`
Converts the UTC timestamp to CERN's local time.

### `hdf2csv`
Reads the hdf file.

###  `plot_image`
Plots a 2D matrix as an image and saves it.

### `linear2matrix`
Converts the linear dataset into 2D matrix and plots the image.
