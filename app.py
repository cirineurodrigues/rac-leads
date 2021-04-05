from flask import Flask, request
from http import HTTPStatus

from services.leads_services import LeadsServices

app = Flask(__name__)

@app.route('/leads', methods=['GET'])
def all_leads():
    return {
        'status': 'Ok!',
        'data': LeadsServices.read_csv()
    }

@app.route('/register', methods=['POST'])
def register_lead():
    req = request.get_json()
    LeadsServices.register(req)

    return 'Lead cadastrado com sucesso', HTTPStatus.OK


@app.route('/')
def index():
    return "<h1>Welcome to Rac Leads API</h1>"