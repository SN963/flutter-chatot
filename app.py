from re import DEBUG
from tkinter.constants import TRUE
from flask import flask,jsonify,request
import time
app=flask(__name__)
@app.route("/bot",method=["POST"])

def response():
    query=dict(request.form)['query']
    result=query+"  "+time.ctime()
    return jsonify({"response":result})

if __name__=="__main__":
    app.run(host="0.0.0.0",)
