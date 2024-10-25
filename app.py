from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = ""
ENGINE_ID = ""

def search(query):
    url = 
    params = {
        "key": API_KEY,
        "cx": ENGINE_ID,
        "q": query
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "items" in data:
        results = data["items"]
        return results
    else:
        return []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search_route():
    query = request.args.get("query")
    search_results = search(query)
    return render_template("results.html", query=query, results=search_results)

if __name__ == "__main__":
    app.run(debug=True)
