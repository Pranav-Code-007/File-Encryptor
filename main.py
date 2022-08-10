# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, request, send_file
import Encryption

app = Flask(__name__)
key = b'272653^&W%&^%&$%^&%&$%(@*&(@*^'
filename = ''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


@app.route('/')
@app.route('/home')
def hom():
    return render_template('home.html')


@app.route('/uploader', methods=["POST"])
def upload():
    f = request.files['file']
    print(f.filename)
    global filename
    filename = f.filename
    f.save(filename)
    return render_template('download.html')

@app.route('/download')
def download_file():
    Encryption.encrypt(filename)

    return send_file(filename+".enc", as_attachment=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
