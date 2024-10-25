from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "AIzaSyChwEIjeMtU3_ObWfxXLPa61rbnZE5-oxw"
ENGINE_ID = "e44a4cd7a664b49c1"

def search(query):
    url = f"https://www.googleapis.com/customsearch/v1"
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
