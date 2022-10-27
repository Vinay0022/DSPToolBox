from scipy.signal import filtfilt
from scipy import stats
import scipy

import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np

def plot():
    data = pd.read_csv('./noise.csv')
    sensor_data = data[['data']]
    sensor_data = np.array(sensor_data)
    time = np.linspace(0,0.0002,2000)
    plt.plot(time,sensor_data)
    plt.show()

    filtered_signal = bandPassFilter(sensor_data)

    plt.plot(time,filtered_signal)
    plt.savefig('pics/noise.png')
    plt.show()


def bandPassFilter(signal):
    fs = 4000.0
    lowcut = 20.0
    highcut = 50.0

    nyq = 0.5*fs
    low = lowcut/nyq
    high = highcut/nyq

    order = 2

    b,a = scipy.signal.butter(order,[low,high], 'bandpass',analog= False)
    y = scipy.signal.filtfilt(b,a,signal,axis=0)

    return(y)

plot()