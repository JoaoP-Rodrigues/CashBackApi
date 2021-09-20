from flask import Flask

app = Flask("CashBack")

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"ola": "mundo"}

app.run