from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/healthz")
def healthz():
    # a very simple "are you alive?" check
    return jsonify(status="ok"), 200

@app.get("/api/v1/hello")
def hello():
    name = os.getenv("HELLO_NAME", "world")
    return jsonify(message=f"Hello, {name}!"), 200

if __name__ == "__main__":
    # 0.0.0.0 lets Docker reach it later
    app.run(host="0.0.0.0", port=8000, debug=False)
