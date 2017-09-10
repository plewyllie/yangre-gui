import subprocess
import config
from flask import render_template, jsonify, request
from app import app


@app.route(config.PREFIX + '/', methods=['GET', 'POST'])
@app.route(config.PREFIX + '/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route(config.PREFIX + '/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route(config.PREFIX + '/yangre', methods=['GET', 'POST'])
def yangre():
    # writing the test string to file, as required by w3cgrep
    with open("w3c_input", "w") as testfile:
        testfile.write(request.form['content'])
        testfile.write("\n")

    # An unquoted string is any sequence of characters that does not
    # contain any space, tab, carriage return, or line feed characters, a
    # single or double quote character, a semicolon (";"), braces ("{" or
    # "}"), or comment sequences ("//", "/*", or "*/").

    # python 3.5 dependency. To get stdout as a string we need the universal_newlines=True parameter
    # in python 3.6 this changes to encoding='utf8'
    w3c_input_obj = subprocess.run(
        [config.W3CGREP_PATH,
         str(request.form['pattern']), "w3c_input"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True)
    if not w3c_input_obj.stdout:
        w3c_input_result = 1
    else:
        w3c_input_result = 0

    yangre_input_obj = {}
    if request.form['inverted'] == "true":
        w3c_input_result = int(not w3c_input_result)

        # python 3.5 dependency. To get stdout as a string we need the universal_newlines=True parameter
        # in python 3.6 this changes to encoding='utf8'
        yangre_input_obj = subprocess.run(
            [
                config.YANGGRE_PATH, "-p",
                str(request.form['pattern']), "-i",
                str(request.form['content'])
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True)
    else:
        # python 3.5 dependency. To get stdout as a string we need the universal_newlines=True parameter
        # in python 3.6 this changes to encoding='utf8'
        print("Passing", config.YANGGRE_PATH, "-p",
              str(request.form['pattern']), str(request.form['content']))
        yangre_input_obj = subprocess.run(
            [
                config.YANGGRE_PATH, "-p",
                str(request.form['pattern']),
                str(request.form['content'])
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True)

    if w3c_input_obj.returncode == 1:
        w3c_input_result = -1  # I used -1 as error code

    return jsonify({
        'pattern_nb': request.form['pattern_nb'],
        'w3cgrep_result': w3c_input_result,
        'w3cgrep_output': w3c_input_obj.stdout,
        'yangre_result': yangre_input_obj.returncode,
        'yangre_output': yangre_input_obj.stdout
    })
