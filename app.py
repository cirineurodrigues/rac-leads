from flask import Flask
from http import HTTPStatus

from services.leads_services import LeadsServices

app = Flask(__name__)

@app.route('/leads', methods=['GET'])
def all_leads():
    return {
        'status': 'Ok!',
        'data': LeadsServices.read_csv()
    }

@app.route('/')
def index():
    return "<h1>Welcome to Rac Leads API</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)