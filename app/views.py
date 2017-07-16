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

    #w3c_input_obj = subprocess.run([config.W3CGREP_PATH,str(request.form['pattern']),"w3c_input"],
    #                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT);
    w3c_input_obj = subprocess.getstatusoutput([config.W3CGREP_PATH,str(request.form['pattern']),"w3c_input"])
    if not w3c_input_obj[1]:
        w3c_input_result = 1
    else:
        w3c_input_result = 0

    #yangre_input_obj = subprocess.run([config.YANGGRE_PATH, "-p", str(request.form['pattern']),
    #                                  str(request.form['content'])],
    #                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8');

    yangre_input_obj = subprocess.getstatusoutput([config.YANGGRE_PATH, "-p", str(request.form['pattern']),
                                                   str(request.form['content'])]);

    print (config.YANGGRE_PATH, "-p", str(request.form['pattern']), "\""+ str(request.form['content'] + "\""))

    return jsonify({'w3cgrep_result' : w3c_input_result,
                    'w3cgrep_output' : w3c_input_obj[1],
                    'yangre_result' : yangre_input_obj[0],
                    'yangre_output': yangre_input_obj[1] });
