from flask import Flask, request, jsonify, render_template, session
from auth import verify_admin
from hybrid_ai import hybrid_ai
from memory import save_memory
from users import create_user, login_user

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message")
    save_memory("user", msg)
    return jsonify({"reply": hybrid_ai(msg)})

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    create_user(data["username"], data["password"])
    return {"status":"ok"}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = login_user(data["username"], data["password"])
    if user:
        session["user"] = data["username"]
        return {"status":"ok"}
    return {"error":"invalid"}

@app.route("/admin-login", methods=["POST"])
def admin():
    if verify_admin(request.json.get("password")):
        session["admin"]=True
        return {"status":"admin ok"}
    return {"error":"wrong"},403

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
