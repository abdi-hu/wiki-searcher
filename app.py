from flask import Flask, Blueprint
from flask.json import jsonify

import requests
import json

app = Flask(__name__, subdomain_matching = True)

app.config["SERVER_NAME"] = "wiki-search.com:5000"

# Blueprint declaration
# bp = Blueprint('subdomain', __name__, subdomain="<search_term>")

@app.route('/', subdomain='<search_term>', methods=['GET'])
def wiki(search_term):
    
    uri = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={search_term}"
    req = requests.get(uri)

    search_list = json.loads(req.content)
    link_list = search_list[3]

    return jsonify(lists=link_list)
    
    # Code below displays the first results if there's an exact match
    # term = search_term.capitalize()
    # if link_list[0]==f"https://en.wikipedia.org/wiki/{term}":
    #     return jsonify(link_list[0])
    # else:
    #     return jsonify(lists=link_list)

if __name__ == '__main__':
    app.run(debug=True)

