from flask import Flask, render_template, request
import cgi, os
import cgitb; cgitb.enable()
import matplotlib.image as mpimg
import numpy as np
import tensorflow as tf
from miniprojetiaa import predictt
from tensorflow.keras.models import load_model

app = Flask(__name__)
import os
@app.route('/')
def home():
    return render_template('prediction.html')
@app.route('/pred',methods = ['POST', 'GET'])
def analysis():
	UPLOAD_DIR="C:\\Users\\asus\\Mini projet IAA\\tmp"
	if request.method == 'POST':
            newfile = request.files.get('myfile')
            save_path = os.path.join(UPLOAD_DIR, newfile.filename)
            newfile.save(save_path)	    
            #history=fit(model)
            #pred=predictt(newfile)
            model=tf.keras.models.load_model("C:\\Users\\asus\\Mini projet IAA\\modelle.h5")
            pred=predictt(model,save_path)
            


	return render_template('analysis.html',name=pred)


if __name__=="__main__":
	app.run(host='0.0.0.0', port=5000)