"""Ibnul Jahan
SoftDev1 pd7
HW13 -- A RESTful Journey Skyward
2017-11-08
"""



from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__) #create instance of class 

#assign following fxn to run when
#root route requested

@app.route("/")
def hello():
    return render_template("temp.html", title = "NASA")


if __name__=="__main__":
    app.debug = True
    app.run()
