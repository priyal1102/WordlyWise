import ocr
from flask import *
import os
import secrets

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.config['CACHE_TYPE'] = 'simple'
words = {}


@app.route('/')
def main():
    return render_template("index.html")


# @app.route('/uploads', methods=['POST', 'GET'])
# def uploads():

#     if request.method == 'POST':

#         # check if there is a file in the request
#         if 'file' not in request.files:
#             return render_template('upload.html', msg='No file selected')
#         file = request.files['file']
#         # if no file is selected
#         if file.filename == '':
#             return render_template('upload.html', msg='No file selected')
#         # Get the list of files from webpage
#         files = request.files.getlist("file")

#         # Iterate for each file in the files List, and Save them
#         for file in files:
#             filename = file.filename
#             filepath = os.path.join(app.static_folder, filename)
#             file.save(filepath)
#             text = get_res(filepath)
#             key = f"{file.filename}"
#             words[key] = text

#         return render_template("result.html", my_dict=words, words="Text recognition image")
#     else:
#         return render_template("upload.html")

@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')
        # Get the list of files from webpage
        files = request.files.getlist("file")
        # Remove all files from the static folder
        uploads_folder = os.path.join(app.root_path, 'static', 'upload')
        for filename in os.listdir(uploads_folder):
            file_path = os.path.join(uploads_folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting file: {e}")

        # Iterate for each file in the files List, and Save them
        for file in files:
            filename = file.filename
            filepath = f"{uploads_folder}/{filename}"
            file.save(filepath)
            text = get_res(filepath)
            key = f"{file.filename}"
            words[key] = text

        return render_template("result.html", my_dict=words, words="Text recognition image")
    else:
        return render_template("upload.html")

@app.route('/about')
def about():
    return render_template("about.html")


def get_res(img):
    obj = ocr.Ocr("en")
    word = obj.get_text(img)
    return word


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)
#Hello World
# h
