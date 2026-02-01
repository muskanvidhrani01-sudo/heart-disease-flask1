from flask import Flask, render_template,request
import pickle


app = Flask(__name__)

@app.route("/home")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login",methods=["post"])
def login1():
    em=request.form.get("t1")
    p=request.form.get("t2")
    if em=="abc" and p=="123":
        return "Login success"
    else:
        return "Failed"

@app.route("/Addition")
def Addition():
    return render_template("Addition.html")


@app.route("/Addition",methods=["post"])
def Addition1():
    num1=int(request.form.get("t1"))
    num2=int(request.form.get("t2"))
    ans=num1+num2
    return render_template("Addition.html", ans=ans)

@app.route("/nb")
def nb():
    return render_template("nbdemo.html")


@app.route("/nb",methods=["post"])
def nb1():
    l1=[]
    l1.append(int(request.form.get("t1")))
    l1.append(int(request.form.get("t2")))
    l1.append(int(request.form.get("t3")))
    l1.append(int(request.form.get("t4")))
    
    with open("nb.pkl","rb") as f:
        model=pickle.load(f)
    
    predy=model.predict([l1])[0]
    if predy==1:
        ans="Yes"
    else:
        ans="No"
    return render_template("nbdemo.html", ans=ans)

@app.route("/ID3")
def ID3():
    return render_template("ID32.html")


@app.route("/ID3",methods=["post"])
def ID32():
    l1=[]
    l1.append(int(request.form.get("t1")))
    l1.append(int(request.form.get("t2")))
    l1.append(int(request.form.get("t3")))
    l1.append(int(request.form.get("t4")))

    with open("nb.pkl","rb") as f:
        model=pickle.load(f)
    
    predy=model.predict([l1])[0]
    if predy==1:
        ans="Yes"
    else:
        ans="No"
    return render_template("ID32.html", ans=ans)

if __name__ == "__main__":
    app.run()