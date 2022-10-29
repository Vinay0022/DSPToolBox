from copy import copy
import json
import os
# `from os import sendfile
from types import DynamicClassAttribute
from app import app
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy 
from flask import render_template,redirect,request,jsonify,abort
from main import*

#Filtering code
picFolder = os.path.join('pics')
app.config['UPLOAD_FOLDER']=picFolder
@app.route("/")
def index():
    return render_template("index2.html")

#Matrix
@app.route('/MatrixButton.html')
def MatrixButton():
    return render_template("MatrixButton.html")




@app.route('/twoByTwo.html')
def twoByTwo():
	return render_template("twoByTwo.html")

@app.route('/api/twoByTwo', methods=["POST", "GET"])
def api_twoByTwo():
	if request.method == "GET":
		return abort(403)

	try:
		a11 = float(request.form["a11"])
		a12 = float(request.form["a12"])
		a21 = float(request.form["a21"])
		a22 = float(request.form["a22"])
		A = [None,[None,a11, a12], [None,a21, a22]]
		matrixA = twoBytwo(copy.deepcopy(A),2)
		returned_determinant = matrixA.determinant()
		returned_square = str(matrixA.multiply(matrixA))
		returned_transpose = str(matrixA.transpose())
		if returned_determinant == 0:
			returned_inverse = "Inverse does not exist."
		else:
			returned_inverse = str(matrixA.inverse())
		return jsonify(returned_determinant, returned_transpose, returned_inverse, returned_square)
		
	except Exception as e:
		return str(e)

@app.route('/threeByThree.html')
def threeByThree():
	return render_template("threeByThree.html")

@app.route('/api/threeByThree', methods=["POST", "GET"])
def api_threeByThree():
	if request.method == "GET":
		return abort(403)

	try:
		a11 = float(request.form["a11"])
		a12 = float(request.form["a12"])
		a13 = float(request.form["a13"])
		a21 = float(request.form["a21"])
		a22 = float(request.form["a22"])
		a23 = float(request.form["a23"])
		a31 = float(request.form["a31"])
		a32 = float(request.form["a32"])
		a33 = float(request.form["a33"])
		A = [None,[None,a11, a12, a13], [None,a21, a22, a23], [None,a31, a32, a33]]
		matrixA = threeBythree(copy.deepcopy(A),3)
		returned_determinant = matrixA.determinant()
		returned_square = str(matrixA.multiply(matrixA))
		returned_transpose = str(matrixA.transpose())
		if returned_determinant == 0:
			returned_inverse = "Inverse does not exist."
		else:
			returned_inverse = str(matrixA.inverse())
		return jsonify(returned_determinant, returned_transpose, returned_inverse, returned_square)
	except Exception as e:
		return "Error: " + str(e)

#Buttons 
@app.route("/Button.html")
def button():
    return render_template("Button.html") 

#Polynomial multiplication
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

#Convolution 3*3
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



#Filtering code
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


#First page
@app.route("/index2.html")
def index2():
     return render_template("index2.html")


@app.route("/Operations2.html")
def Operations():
    return render_template("Operations2.html")



#For 4*4 Convolution
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


