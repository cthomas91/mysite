from flask import Flask, render_template                        #import flask framework

app=Flask(__name__)                                             # variable (flask object)

@app.route('/')                                                  # decorator
def home():                                                      #function
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True)