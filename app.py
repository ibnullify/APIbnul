"""Ibnul Jahan
SoftDev1 pd7
HW13 -- A RESTful Journey Skyward
2017-11-08
"""


import urllib2
from flask import Flask, render_template, request, session, redirect, url_for
import json

api_key = "1I3RG0HH1aH67s0fi9nWhhc5oudr3UvzxprRK35f"

data_file = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key="+ api_key)
info = data_file.read()
data = json.loads(info)
img= data['hdurl']
explanation= data['explanation']

app = Flask(__name__) #create instance of class 

#assign following fxn to run when
#root route requested

@app.route("/")
def hello():
    return render_template("temp.html", title = "NASA",img_url = img, description = explanation)


if __name__=="__main__":
    app.debug = True
    app.run()
