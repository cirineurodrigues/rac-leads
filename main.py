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