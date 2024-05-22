from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
  host_header = request.headers.get('Host')
  return f"telegram API wrapper. instead of using api.telegram.org just replace api.telegram.org with {host_header}"
  
@app.route("/<path:wildcard>")
def handle_all(wildcard):
  return requests.get(f"https://api.telegram.org/{wildcard}").content
  
if __name__ == "__main__":
  app.run(debug=True)
