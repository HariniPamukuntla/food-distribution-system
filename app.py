from flask import Flask, render_template, redirect

app = Flask(__name__)

data = [
    {"id":1,"food":"Rice","qty":"30","location":"Miyapur","status":"Pending"},
    {"id":2,"food":"Bread","qty":"20","location":"Kukatpally","status":"Pending"},
    {"id":3,"food":"Curry","qty":"15","location":"Ameerpet","status":"Pending"}
]

@app.route("/")
def dashboard():
    return render_template("dashboard.html", data=data)

@app.route("/incoming")
def incoming():
    pending = [d for d in data if d["status"] == "Pending"]
    return render_template("incoming.html", data=pending)

@app.route("/accepted")
def accepted():
    accepted = [d for d in data if d["status"] == "Accepted"]
    return render_template("accepted.html", data=accepted)

@app.route("/completed")
def completed():
    completed = [d for d in data if d["status"] == "Completed"]
    return render_template("completed.html", data=completed)

@app.route("/ngos")
def ngos():
    return render_template("ngos.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")

@app.route("/accept/<int:id>")
def accept(id):
    for d in data:
        if d["id"] == id:
            d["status"] = "Accepted"
    return redirect("/incoming")

@app.route("/reject/<int:id>")
def reject(id):
    for d in data:
        if d["id"] == id:
            d["status"] = "Rejected"
    return redirect("/incoming")


import os
 if __name__=='__main__':
    app.run(host="0.0.0.0",
             port=int(os.environ.get("PORT", 5000)))