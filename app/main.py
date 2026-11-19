from flask import Flask, jsonify, request

app = Flask(__name__)


def add(a: float, b: float) -> float:
    return a + b


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/add")
def add_route():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=add(a, b))
