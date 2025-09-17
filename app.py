from flask import Flask, jsonify, request

app = Flask(__name__)
todos = []

@app.route("/")
def hello():
    return "Todo app"

@app.route("/todos", methods=["GET"])
def list_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json() or {}
    item = {"id": len(todos)+1, "task": data.get("task", "")}
    todos.append(item)
    return jsonify(item), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
