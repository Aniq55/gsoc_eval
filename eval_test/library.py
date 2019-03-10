import pytz
from datetime import datetime

import h5py
import pandas as pd

import numpy as np
from scipy.signal import medfilt
import matplotlib.pyplot as plt


def file2utc(filepath):
    filename = (filepath.split('/')[-1])[0:19]
    time_ns = float(filename)/(10**9)
    return pytz.utc.localize(datetime.fromtimestamp(time_ns))

def utc2cern(timestamp_utc):
    return timestamp_utc.astimezone(pytz.timezone('Europe/Zurich'))

def hdf2csv(filepath, output):
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
    input_file= h5py.File(hdf_path, 'r')
    output_path = output + ((hdf_path.split('/')[-1]).split('.'))[0] + '_' + image_path.split('/')[-2] + '.png'

    data = input_file[ image_path + 'streakImageData'][:]
    h = input_file[ image_path + 'streakImageHeight'][0]
    w = input_file[ image_path + 'streakImageWidth'][0]

    reshaped_data = np.reshape(data, (h,w))
    filtered_img = medfilt(reshaped_data)

    plot_image(filtered_img, (h/100.0, w/100.0), image_path, output_path)


# Task 1
timestamp_utc = file2utc('./1541962108935000000_167_838.h5')
timestamp_cern = utc2cern(timestamp_utc)

print(timestamp_utc)
print(timestamp_cern)

# Task 2
hdf2csv('./data/1541962108935000000_167_838.h5', './out/')

# Task 3
linear2matrix('./data/1541962108935000000_167_838.h5', '/AwakeEventData/XMPP-STREAK/StreakImage/', './out/')
