import os
import json
from flask import Flask, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=["GET"])
def main():
  response="Hello World from Local"
  return Response(json.dumps(response), status=200, mimetype='application/json')


if __name__ == '__main__':
  PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8080
  app.run(host="0.0.0.0", port=PORT, debug=True)