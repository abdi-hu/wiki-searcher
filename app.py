from flask import Flask
from flask.json import jsonify

import requests
import json


app = Flask(__name__, subdomain_matching = True)

app.config["SERVER_NAME"] = "wiki-search.com:5000"

@app.route('/', subdomain='<search_term>', methods=['GET'])
def wiki(search_term):
    
    uri = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={search_term}"
    req = requests.get(uri)

    search_list = json.loads(req.content)

    # The last nested array contains the wikipedia links
    link_list = search_list[3]


    # checks if the first match from the list is "disambiguation page" from wikipedia then returns the data respectively
    site = requests.get(link_list[0])
    page = site.text
    list_page = "disambiguation page"
    if list_page in page:
        return jsonify(lists=link_list)
    else:
        return jsonify(link_list[0])
    
if __name__ == '__main__':
    app.run(debug=True)

