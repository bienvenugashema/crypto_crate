from flask import Flask, render_template, request
from ciphers import ceasar

app = Flask(__name__)

@app.route("/ceaser", methods=['GET', 'POST'])
def ceaser():
    result = ''
    if request.method == "POST":
        text = request.form['text']
        shift = int(request.form['shift'])
        mode = request.form['mode']
        result = ceasar.caesar_cipher(text, shift, mode)
    return render_template("ceaser.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
