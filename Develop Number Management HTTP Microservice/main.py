from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


all_numbers = []

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')

    for url in urls:
        response = get_numbers_from_url(url)
        if response and 'numbers' in response:
            all_numbers.extend(response['numbers'])

    
    unique_sorted_numbers = sorted(list(set(all_numbers)))

    return jsonify(numbers=unique_sorted_numbers)


def get_numbers_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"numbers": []}
    except requests.exceptions.RequestException:
        return {"numbers": []}

if __name__ == '__main__':
    app.run(port=8008,debug=True)
