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

    with open("w3c_input", "w") as f: # writing the test string to file, as required by w3cgrep
        f.write(request.form['content'])
        f.write("\n")

    w3c_input_obj = subprocess.run([config.W3CGREP_PATH,str(request.form['pattern']),"w3c_input"], stdout=subprocess.PIPE)
    if not w3c_input_obj.stdout:
        w3c_input_result = 0
    else:
        w3c_input_result = 1

    print (config.YANGGRE_PATH, "-p", "\"" + str(request.form['pattern']) +  "\"", "\""+ str(request.form['content'] + "\""))

    return jsonify({'w3cgrep_result' : w3c_input_result,
                    'yangre_result' : subprocess.run([config.YANGGRE_PATH,
                       "-p", "\"" + str(request.form['pattern']) +  "\"",
                       "\""+ str(request.form['content'] + "\"")]).returncode });
