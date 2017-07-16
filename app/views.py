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
    with open("w3c_input", "w") as f: # writing the test string to file, as required by w3cgrep
        f.write(request.form['content'])
        f.write("\n")

    # python 3.5 dependency. To get stdout as a string we need the universal_newlines=True parameter
    # in python 3.6 this changes to encoding='utf8'
    w3c_input_obj = subprocess.run([config.W3CGREP_PATH,str(request.form['pattern']),"w3c_input"],
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True);
    if not w3c_input_obj.stdout:
        w3c_input_result = 1
    else:
        w3c_input_result = 0

    yangre_input_obj = {}
    if request.form['inverted'] == "true":
        w3c_input_result = int(not(w3c_input_result))
        # python 3.5 dependency. To get stdout as a string we need the universal_newlines=True parameter
        # in python 3.6 this changes to encoding='utf8'
        yangre_input_obj = subprocess.run([config.YANGGRE_PATH, "-p", str(request.form['pattern']), "-i",
                                          str(request.form['content'])],
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True);
    else:
        # python 3.5 dependency. To get stdout as a string we need the universal_newlines=True parameter
        # in python 3.6 this changes to encoding='utf8'
        yangre_input_obj = subprocess.run([config.YANGGRE_PATH, "-p", str(request.form['pattern']),
                                          str(request.form['content'])],
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True);


    #print (config.YANGGRE_PATH, "-p", str(request.form['pattern']), "\""+ str(request.form['content'] + "\""))
    #print (config.W3CGREP_PATH, str(request.form['pattern']), )

    return jsonify({'w3cgrep_result' : w3c_input_result,
                    'w3cgrep_output' : w3c_input_obj.stdout,
                    'yangre_result' : yangre_input_obj.returncode,
                    'yangre_output': yangre_input_obj.stdout });
