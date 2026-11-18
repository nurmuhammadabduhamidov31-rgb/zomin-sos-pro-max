from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚨 ZOMIN SOS PRO MAX</h1>
    <h2>Yordam tizimi ishga tushdi!</h2>
    <p>Favqulodda yordam platformasi</p>
    <button onclick="alert('SOS signali tayyor!')">
        🆘 SOS
    </button>
    """

@app.route("/status")
def status():
    return jsonify({
        "app": "ZOMIN SOS PRO MAX",

        "status": "working"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)