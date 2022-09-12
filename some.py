from scipy.signal import filtfilt
from scipy import stats
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

# def plot():
#   data = pd.read_csv('./three_freq_signal2.csv')
#   sensor_data = data[['data']]

#   sensor_data = np.array(sensor_data)

#   time = np.linspace(0, 0.0002, 1001)

#   plt.plot(time,sensor_data)
#   plt.show()

# plot()
def plot():
   df = pd.read_csv("three_freq_signal2.csv")
   sensor_data = data[['data']]
`  sensor_dataa = np.array(sensor_data)
    time=np.linspace (0,0.0002,4000)
    plt.plot(time,sensor_dataa)
    plt.show()
    plot()

# filtered_signal = bandPassfilter(sensor_dataa)
# plt.plot
# def bandPassfilter(signal):
#   fs = 4000.0
#   lowcut = 20.0
#   highcut = 50.0

#   nyq = 0.5*fs
#   low = lowcut/nyq
#   high = highcut/nyq

#   order = 2

#   b,a = scipy.signal.butter(order,[low,high], 'bandpass',analog=False)
#   y = scipy.signal.filtfilt(b,a,signal,axis=0)

#   return(y)

# plot()