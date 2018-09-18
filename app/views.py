import subprocess
import os
import config
from flask import render_template, jsonify, request, send_from_directory
from app import app


@app.route(config.PREFIX + '/', methods=['GET', 'POST'])
@app.route(config.PREFIX + '/index', methods=['GET', 'POST'])
def index():
    return render_template(
        'index.html', title="YANG Regex Expression Validator")


@app.route(config.PREFIX + '/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route(config.PREFIX + '/w3cgrep', methods=['GET'])
def w3cgrep():  # loads the w3cgrep validator
    return render_template(
        'w3cgrep.html', title="W3C Regex Expression Validator")


@app.route(config.PREFIX + '/v1', methods=['GET'])
def swagger():  # loads the SWAGGER API UI
    return render_template('swagger.html')


@app.route(config.APIPREFIX + '/w3c', methods=['GET', 'POST'])
def w3c():  # JSON API to validate W3C input
    req_data = request.get_json()

    # writing the test string to file, as required by w3cgrep
    w3cinput_filename = "w3c_input" + str(req_data['pattern_nb'])
    with open(w3cinput_filename, "w") as testfile:
        testfile.write(req_data['content'])
        testfile.write("\n")
        testfile.flush()
        os.fsync(testfile.fileno())

    # python 3.5 dependency. To get stdout as a string we need the universal_newlines=True parameter
    # in python 3.6 this changes to encoding='utf8'
    w3c_input_obj = subprocess.run(
        [config.W3CGREP_PATH,
         str(req_data['pattern']), w3cinput_filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True)
    if not w3c_input_obj.stdout:
        w3c_input_result = 1
    else:
        w3c_input_result = 0

    if req_data['inverted'] == "true":
        w3c_input_result = int(not w3c_input_result)

    if w3c_input_obj.returncode == 1:
        w3c_input_result = -1  # I used -1 as error code

    # clean up files
    try:
        os.remove(w3cinput_filename)
    except FileNotFoundError:
        print("Oops, file not found")

    return jsonify({
        'pattern_nb': req_data['pattern_nb'],
        'w3cgrep_result': w3c_input_result,
        'w3cgrep_output': w3c_input_obj.stdout
    })


@app.route(config.APIPREFIX + '/yangre', methods=['POST'])
def yangre():  # JSON API to validate YANG input
    req_data = request.get_json()

    # writing the test string to another file for yangre
    yangreinput_filename = "yangre_input" + str(req_data['pattern_nb'])
    with open(yangreinput_filename, "w") as yangrefile:
        yangrefile.write(str(req_data['pattern']))
        yangrefile.write("\n\n")
        yangrefile.write(str(req_data['content']))
        yangrefile.flush()
        os.fsync(yangrefile.fileno())

    yangre_input_obj = {}
    if req_data['inverted'] == "true":
        # python 3.5 dependency. To get stdout as a string we need the universal_newlines=True parameter
        # in python 3.6 this changes to encoding='utf8'
        yangre_input_obj = subprocess.run(
            [config.YANGGRE_PATH, "-f", yangreinput_filename, "-i"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True)
    else:
        # python 3.5 dependency. To get stdout as a string we need the universal_newlines=True parameter
        # in python 3.6 this changes to encoding='utf8'
        yangre_input_obj = subprocess.run(
            [config.YANGGRE_PATH, "-f", yangreinput_filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True)

    # clean up files
    try:
        os.remove(yangreinput_filename)
    except FileNotFoundError:
        print("Oops, file not found")

    return jsonify({
        'pattern_nb': req_data['pattern_nb'],
        'yangre_result': yangre_input_obj.returncode,
        'yangre_output': yangre_input_obj.stdout
    })
