#!/usr/bin/python3
"""this starts flask web app
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.teardown_appcontext
def close(self):
    """this shows html page for states"""
    storage.close()


@app.route('/states', strict_slashes=False)

@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """this shows html page for states"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """this destroys session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
