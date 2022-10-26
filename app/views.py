# from crypt import methods
import json
from types import DynamicClassAttribute
from app import app
import numpy as np
from flask import render_template,redirect,request


@app.route("/")
def index():
    return render_template("index2.html") 

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


