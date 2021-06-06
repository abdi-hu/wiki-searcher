from flask import Flask, Blueprint
from flask.json import jsonify
from werkzeug.utils import redirect
import requests

app = Flask(__name__, subdomain_matching = True)

app.config["SERVER_NAME"] = "wiki-search.com:5000"

# Blueprint declaration
# bp = Blueprint('subdomain', __name__, subdomain="<search_term>")

@app.route('/', subdomain='<search_term>', methods=['GET'])
def wiki(search_term):
    uri = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={search_term}&format=json"
    req = requests.get(uri)
    data = req.content
    print('data')
    print(data)
    # return data
   




    return redirect(f"https://en.wikipedia.org/w/api.php?action=opensearch&search={search_term}&format=json")
    



if __name__ == '__main__':
    app.run(debug=True)



# curl command to test subdomain
# curl --resolve 'dogs.wiki-search.com:5000' 127.0.0.1:5000