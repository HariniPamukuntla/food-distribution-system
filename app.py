from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# sample data
data = [
    {"id": 1, "food": "Rice", "qty": 30, "location": "Miyapur", "urgency": "MEDIUM", "status": "Pending"},
]

@app.route("/")
def dashboard():
    return render_template("dashboard.html", data=data)

@app.route("/incoming")
def incoming():
    return render_template("incoming.html", data=data)

@app.route("/accepted")
def accepted():
    accepted_data = [d for d in data if d["status"] == "Accepted"]
    return render_template("accepted.html", data=accepted_data)

@app.route("/completed")
def completed():
    completed_data = [d for d in data if d["status"] == "Completed"]
    return render_template("completed.html", data=completed_data)

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


