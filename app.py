from flask import Flask, request
from flask_cors import CORS, cross_origin

from services.leads_services import LeadsServices
from handlers.http_handlers import success_request, created_request, unprocessable_request

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/leads', methods=['GET'])
@cross_origin()
def all_leads():
   return success_request(LeadsServices.read_csv())

@app.route('/register', methods=['POST'])
@cross_origin()
def register_lead():
    req = request.get_json()
    register = LeadsServices.register(req)

    if register:
        return created_request()

    else:
        return unprocessable_request()
    
@app.route('/')
@cross_origin()
def index():
    return "<h1>Welcome to Rac Leads API</h1>"