import pytz
from datetime import datetime

import h5py
import pandas as pd

import numpy as np
from scipy.signal import medfilt
import matplotlib.pyplot as plt


def file2utc(filepath):
    """
    Converts the first 19 digits of the hdf filename (filepath) to UNIX time
    and returns the UTC timestamps.
    """
    filename = (filepath.split('/')[-1])[0:19]
    time_ns = float(filename)/(10**9)
    return pytz.utc.localize(datetime.fromtimestamp(time_ns))

def utc2cern(timestamp_utc):
    """
    Converts the UTC timestamp (timestamp_utc) to CERN's local timestamp.
    """
    return timestamp_utc.astimezone(pytz.timezone('Europe/Zurich'))

def hdf2csv(filepath, output):
    """
    Reads the hdf file at filepath and stores its csv details equivalent at
    the output directory
    """
    output_path = output+ ((filepath.split('/')[-1]).split('.'))[0] +'.csv'
    input_file = h5py.File(filepath, 'r')

    rows = dict()

    def traverse(path, element):
        if isinstance(element, h5py.Dataset):
            try:
                data_type = element.dtype
            except Exception as e:
                data_type = str(e)

            rows[path] = ['Dataset', element.size, element.shape, data_type]
        else:
            rows[path] = ['Group', '','','']

    input_file.visititems(traverse)
    df = pd.DataFrame.from_dict(rows, orient='index', columns = ['type', 'size', 'shape', 'data_type'])
    df.to_csv(output_path, sep=',')


def plot_image(im_data, dimensions, im_title= None, output_path= None):
    """
    Plots a 2D matrix as an image as saves it at output path.
    """
    fig = plt.figure(figsize = dimensions)

    ax = fig.add_subplot(111)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    if im_title is not None:
        plt.title(im_title)

    plt.imshow(im_data)

    if output_path is not None:
        plt.savefig(output_path, bbox_inches='tight')

def linear2matrix(hdf_path, image_path, output):
    """
    Converts the linear data in the image dataset to its 2D equivalent
    and saves it as an image.
    """
    input_file= h5py.File(hdf_path, 'r')
    output_path = output + ((hdf_path.split('/')[-1]).split('.'))[0] + '_' + image_path.split('/')[-2] + '.png'

    data = input_file[ image_path + 'streakImageData'][:]
    h = input_file[ image_path + 'streakImageHeight'][0]
    w = input_file[ image_path + 'streakImageWidth'][0]

    reshaped_data = np.reshape(data, (h,w))
    filtered_img = medfilt(reshaped_data)

    plot_image(filtered_img, (h/100.0, w/100.0), image_path, output_path)
