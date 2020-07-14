import json
from flask import Flask
from flask import request

app = Flask(__name__)

_PRODUCER = Producer({
    'bootstrap.servers': 'localhost:9092'
})


@app.route("/kafka", methods=['GET', 'POST', 'OPTIONS'])
def home():

    # Set CORS headers for the pre-flight request. change.
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': 'https://www.sephora.sg',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'Access-Control-Allow-Credentials': 'true'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Content-Type':'application/json',
        'Access-Control-Allow-Origin': 'https://www.sephora.sg',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Credentials': 'true'
    }

    print("\n\n")
    print("I AM HERE")
    print("\n\n")
    print(request.get_json())
    print("\n\n")

    return ("something", 200, headers)


if __name__ == "__main__":
    app.run(debug=True)
