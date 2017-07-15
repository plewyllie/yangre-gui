from flask import render_template, flash, redirect, jsonify, request
from app import app
import subprocess
import config

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
        return render_template('index.html')
                                #title='Home',
                                #user=user)

@app.route('/yangre', methods=['GET','POST'])
def yangre():
    #with open("test.txt", "w") as f:
        #f.write(request.form['pattern'])
        #f.write(str(subprocess.run(["./yangre", "1"]).returncode))
    #print (config.YANGGRE_PATH + " -p " + "\"" + str(request.form['pattern']) +  "\" " + "\""+ str(request.form['content'] + "\""));
    #return jsonify({'result': "1"})
    return jsonify({'result': subprocess.run([config.YANGGRE_PATH,
                       " -p ", "\"" + str(request.form['pattern']) +  "\" ",
                       "\""+ str(request.form['content'] + "\"")]).returnvalue });
