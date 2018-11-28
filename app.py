from flask import Flask, render_template, jsonify, request, session
from desserts import dessert_list

app = Flask(__name__)


@app.route("/")
def home():
    """Return home page with basic info"""

    return render_template("index.html")


@app.route("/desserts")
def show_desserts():
    """Return all desserts"""

    return jsonify(dessert_list.serialize())


@app.route('/desserts', methods=["POST"])
def add_new_dessert():
    """Adds a new dessert to the dessert list"""

    dessert_list.add(
        name=request.json['name'],
        description=request.json['description'],
        calories=request.json['calories'])

    return jsonify(dessert_list.desserts[-1].serialize())