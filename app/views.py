import json
import os
# `from os import sendfile
from types import DynamicClassAttribute
from app import app
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy 
from flask import render_template,redirect,request

picFolder = os.path.join('pics')
app.config['UPLOAD_FOLDER']=picFolder
@app.route("/")
def index():
    return render_template("index2.html")


@app.route("/Button.html")
def button():
    return render_template("Button.html") 

@app.route("/Polynomial.html",methods=['GET','POST'])
def Polynomial():
 list = []
 list2 = []
 list3=[]
 if request.method == "POST":
       num1 = request.form.get('num1')
       num2 = request.form.get('num2')
       num3 = request.form.get('num3')
       num5 = request.form.get('num5')
       num6 = request.form.get('num6')
       num7 = request.form.get('num7')
       fnum1 =float(num1) 
       fnum2 =float(num2) 
       fnum3 =float(num3) 
       fnum5 =float(num5) 
       fnum6 =float(num6) 
       fnum7 =float(num7) 

       list.append(fnum1)
       list.append(fnum2)
       list.append(fnum3)

       list2.append(fnum5)
       list2.append(fnum6)
       list2.append(fnum7)
       print(list)
       print(list2)
       rx = np.polynomial.polynomial.polymul(list, list2)
    #    arr1 = np.array(list,dtype=float)
    #    arr2 = np.array(list2,dtype=float)
    #    list4 =np.convolve(arr1,arr2,mode='full')
       json_str = json.dumps({'nums': rx.tolist()})

       print(json_str)  # 👉️ {"nums": [1, 2, 3, 4]}
       print(type(json_str))  # 👉️ <class 'str'>
    #    print("Result\n",np.convolve(arr1,arr2,mode='full'))
    #    list3 =np.convolve(arr1,arr2,mode='valid') 
       return json_str 
 return render_template("Polynomial.html")

@app.route("/Convolution3by3.html",methods=['GET','POST'])
def Convolution3by3():
 list = []
 list2 = []
 list3=[]
 if request.method == "POST":
       num1 = request.form.get('num1')
       num2 = request.form.get('num2')
       num3 = request.form.get('num3')
       num5 = request.form.get('num5')
       num6 = request.form.get('num6')
       num7 = request.form.get('num7')
       fnum1 =float(num1) 
       fnum2 =float(num2) 
       fnum3 =float(num3) 
       fnum5 =float(num5) 
       fnum6 =float(num6) 
       fnum7 =float(num7) 

       list.append(fnum1)
       list.append(fnum2)
       list.append(fnum3)

       list2.append(fnum5)
       list2.append(fnum6)
       list2.append(fnum7)
       print(list)
       print(list2)

       arr1 = np.array(list,dtype=float)
       arr2 = np.array(list2,dtype=float)
       list4 =np.convolve(arr1,arr2,mode='full')
       json_str = json.dumps({'nums': list4.tolist()})

       print(json_str)  # 👉️ {"nums": [1, 2, 3, 4]}
       print(type(json_str))  # 👉️ <class 'str'>
       print("Result\n",np.convolve(arr1,arr2,mode='full'))
    #    list3 =np.convolve(arr1,arr2,mode='valid') 
       return json_str 
 return render_template("Convolution3by3.html")

@app.route("/Convolution2.html")
def Convolution2():
     list = []
     list2 = []
     list3=[]
     if request.method == "POST":
        num1 = request.form.get('num1')
        # fnum1 =float(num1) 
        # list.append(fnum1)
        num2 = request.form.get('num2')
        num3 = request.form.get('num3')
        num4 = request.form.get('num4')
        num5 = request.form.get('num5')
        num6 = request.form.get('num6')
        num7 = request.form.get('num7')
        num8 = request.form.get('num8')
        
        fnum1 =float(num1) 
        fnum2 =float(num2) 
        fnum3 =float(num3) 
        fnum4 =float(num4) 
        fnum5 =float(num5) 
        fnum6 =float(num6) 
        fnum7 =float(num7) 
        fnum8 =float(num8) 

        list.append(fnum1)
        list.append(fnum2)
        list.append(fnum3)
        list.append(fnum4)

        list2.append(fnum5)
        list2.append(fnum6)
        list2.append(fnum7)
        list2.append(fnum8)
        print(list)
        print(list2)

        arr1 = np.array(list,dtype=float)
        arr2 = np.array(list2,dtype=float)
        list4 =np.convolve(arr1,arr2,mode='full')
        json_str = json.dumps({'nums': list4.tolist()})

        print(json_str)  # 👉️ {"nums": [1, 2, 3, 4]}
        print(type(json_str))  # 👉️ <class 'str'>
        print("Result\n",np.convolve(arr1,arr2,mode='full'))
        #    list3 =np.convolve(arr1,arr2,mode='valid') 
        return json_str 
        print(list)

     return render_template("Convolution2.html")


@app.route("/upload.html", methods=['GET','POST'])
def upload():
    #  if request.method =="POST":

        def plot():
                data = pd.read_csv('./noise.csv')
                sensor_data = data[['data']]
                sensor_data = np.array(sensor_data)
                time = np.linspace(0,0.0002,2000)
                plt.plot(time,sensor_data)
                plt.savefig('pics/noise.png')
                # plt.show()

                filtered_signal = bandPassFilter(sensor_data)

                plt.plot(time,filtered_signal)
                plt.savefig('pics/noise2.png')
                # plt.show()


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
        pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'noise2.png')
        return render_template("upload.html")

@app.route("/Practise2.html", methods=['GET','POST'])
def Practise2():
    list = []
    list2 = []
    list3=[]
    if request.method == "POST":
       num1 = request.form.get('num1')
       fnum1 =float(num1) 
       list.append(fnum1)
       num2 = request.form.get('num2')
       num3 = request.form.get('num3')
       num4 = request.form.get('num4')
       num5 = request.form.get('num5')
       num6 = request.form.get('num6')
       num7 = request.form.get('num7')
       num8 = request.form.get('num8')
       
       fnum1 =float(num1) 
       fnum2 =float(num2) 
       fnum3 =float(num3) 
       fnum4 =float(num4) 
       fnum5 =float(num5) 
       fnum6 =float(num6) 
       fnum7 =float(num7) 
       fnum8 =float(num8) 

       list.append(fnum1)
       list.append(fnum2)
       list.append(fnum3)
       list.append(fnum4)

       list2.append(fnum5)
       list2.append(fnum6)
       list2.append(fnum7)
       list2.append(fnum8)
       print(list)
       print(list2)

       arr1 = np.array(list,dtype=float)
       arr2 = np.array(list2,dtype=float)
       list4 =np.convolve(arr1,arr2,mode='full')
       json_str = json.dumps({'nums': list4.tolist()})

       print(json_str)  # 👉️ {"nums": [1, 2, 3, 4]}
       print(type(json_str))  # 👉️ <class 'str'>
       print("Result\n",np.convolve(arr1,arr2,mode='full'))
    #    list3 =np.convolve(arr1,arr2,mode='valid') 
       return json_str 
       print(list)

    return render_template("Practise2.html")

@app.route("/index2.html")
def index2():
     return render_template("index2.html")

@app.route("/Operations2.html")
def Operations():
    return render_template("Operations2.html")


@app.route("/Convolution.html", methods=['GET','POST'])
def Convolution():
    if request.method == "POST":
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        add = float(num1)*float(num2)
        return  [add]
    return render_template("Convolution.html")

@app.route("/Practise.html",methods=['GET','POST'])
def Pracitse():
 list = []
 list2 = []
 list3=[]
 if request.method == "POST":
       num1 = request.form.get('num1')
       num2 = request.form.get('num2')
       num3 = request.form.get('num3')
       num4 = request.form.get('num4')
       num5 = request.form.get('num5')
       num6 = request.form.get('num6')
       num7 = request.form.get('num7')
       num8 = request.form.get('num8')
       num9 = request.form.get('num9')
       num10 = request.form.get('num10')
       fnum1 =float(num1) 
       fnum2 =float(num2) 
       fnum3 =float(num3) 
       fnum4 =float(num4) 
       fnum5 =float(num5) 
       fnum6 =float(num6) 
       fnum7 =float(num7) 
       fnum8 =float(num8) 

       list.append(fnum1)
       list.append(fnum2)
       list.append(fnum3)
       list.append(fnum4)

       list2.append(fnum5)
       list2.append(fnum6)
       list2.append(fnum7)
       list2.append(fnum8)
       print(list)
       print(list2)

       arr1 = np.array(list,dtype=float)
       arr2 = np.array(list2,dtype=float)
       list4 =np.convolve(arr1,arr2,mode='full')
       json_str = json.dumps({'nums': list4.tolist()})

       print(json_str)  # 👉️ {"nums": [1, 2, 3, 4]}
       print(type(json_str))  # 👉️ <class 'str'>
       print("Result\n",np.convolve(arr1,arr2,mode='full'))
    #    list3 =np.convolve(arr1,arr2,mode='valid') 
       return json_str 
 return render_template("Practise.html")


