import requests
import requests_cache
from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
__author__ = "nikspandya2@gmail.com"

# To enables CORS support on all routes
CORS(app, resources={r"/*": {"origins": "*"}})

# Get only required data from randomuser api (name, gender, location, enail)
RANDOM_USER_API_URL = (
    "https://randomuser.me/api?results=500&inc=name,gender,location,email"
)

# Cache a response that will expire immediately
requests_cache.install_cache("random_user_cache", expire_after=0.001)
# The cached response will still be used until the content from randomuser api actually changes
# So if synchronization fails with randomuser api then
# previous cached response will be used to serve data to ui


@app.route("/", methods=["GET"])
def default_route():
    return jsonify({"message": "API connector is us and running"}), 200


@app.route("/users", methods=["GET"])
def user_data():
    if request.method == "GET":
        # pull data from randomuser api
        api_response = requests.get(RANDOM_USER_API_URL)
        data_json = api_response.json()
        results = data_json.get("results")
        users = []
        for entry in results:
            country = entry.get("location").get("country")
            user_name = (
                entry.get("name").get("first") + " " + entry.get("name").get("last")
            )
            gender = entry.get("gender")
            email_ = entry.get("email")
            user = {
                "country": country,
                "name": user_name,
                "gender": gender,
                "email": email_,
            }
            users.append(user)
        return jsonify({"users": users}), 200
    else:
        return jsonify({"message": "Invalid request"}), 400


if __name__ == "__main__":
    app.run(debug=True, port=8601, host="0.0.0.0")
    # Please use waitress serve for the production deployement
    # serve(app=app, host='0.0.0.0', port='8601')
