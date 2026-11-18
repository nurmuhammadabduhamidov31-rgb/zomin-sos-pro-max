from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/status")
def status():
    return jsonify({
        "app": "ZOMIN SOS PRO MAX",
        "status": "online"
    })

@app.route("/sos", methods=["POST"])
def sos():
    return jsonify({
        "message": "SOS signal qabul qilindi",
        "status": "received"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)