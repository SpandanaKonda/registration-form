from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
def hello():
    return render_template("index.html")
@app.route('/submit',methods=["POST"])
def submit():
    name=request.form['name']
    age=request.form['age']
    ph=request.form['ph']
    return render_template("greetings.html", name=name,age=age,ph=ph)
if __name__=="__main__":
    app.run(debug=True)
