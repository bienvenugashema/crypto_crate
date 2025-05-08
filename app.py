from flask import Flask, render_template, request
from ciphers import ceasar, xor, base64_template
app = Flask(__name__)

@app.route("/")
def home():
   return render_template("index.html")

@app.route("/caesar", methods=['GET', 'POST'])
def ceaser():
    result = ''
    if request.method == "POST":
        text = request.form['text']
        shift = int(request.form['shift'])
        mode = request.form['mode']
        result = ceasar.caesar_cipher(text, shift, mode)
    return render_template("caesar.html", result=result)


@app.route("/base64", methods=["POST", "GET"])
def base64():
    result=''
    if request.method == "POST":
        text = request.form["text"]
        mode = request.form['mode']

        result = base64_template.base64_tool(text, mode)
    return render_template("base64.html", result=result)


@app.route("/xor", methods=["POST", "GET"])
def xor_tool():
    result = ""
    mode = "encrypt"  # Default mode
    if request.method == "POST":
        text = request.form['text']
        key = int(request.form['key'])  # Convert key to integer
        mode = request.form['mode']
        if mode == "encrypt":
            result = xor.encrypt(text, key)
        else:
            result = xor.decrypt(text)
    return render_template("xor.html", result=result, mode=mode)

if __name__ == "__main__":
    app.run(debug=True)
