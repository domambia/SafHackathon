from app import app 
from flask import jsonify, request
from app.models.sim import SimCard 
from app.models.sim  import Account 
from app.helpers import generators


@app.route('/')
def home():
    return  "Welcome to the Mpesa Api Test"


@app.route('/api/v1/query-subscriber-info/<MSISDN>', methods  = ["GET"])
def querySubscrberInfo(MSISDN):
    sim  = SimCard.query.filter(SimCard.MSISDN == MSISDN).first()
    if sim is None:
        results  = {
            message: "No records found",
            content: {
                "No Records"
            },
            "status_code": 1}
        return jsonify(results), 404

    results  = {
        message: "Success"
        content:{
            "ICCID": sim.ICCID,
            "MSISDN":sim.MSISDN ,
            "IMSI": sim.IMSI,
            "Ki": sim.Ki,
            "PIN1": sim.PIN1 ,
            "PUC": sim.PUC ,
            "status":sim.status ,
            "balance":sim.balance  
        },
        "status_code": 0
    }
    return jsonify(results), 200

@app.route('/api/v1/provision-of-sim-card/', methods  = ["POST"])
def provideSim():
    data  = request.get_json()
    if data['name'] is None:
        results  = {
            message: "Error",
            content: {
                "Name Cannot be empty",
            },
            "status_code": 1}
        return jsonify(results), 404
        MSISDN = generators.get_MSSIDN()
        ICCID = generators.get_ICCID()
        IMSI  = generators.get_IMSI()
        PUC  = generators.get_puc()
        PIN1 = generators.get_pin()
        Ki   = generators.get_Ki()
        
        sim   =SimCard(
            MSISD = 
        )
        
        results  = {
            message"
        }


    pass


@app.route('/api/v1/activation-of-simcard/<MSISDN>/<ICCID>/<IMSI>/', methods  = ['PUT'])
def activateSim(MSISDN, ICCID, IMSI):
    pass 


@app.route('api/v1/maintain-account<MSISD>/', methods = ["PUT"])
def maintainAcccount(MSISDN):
    pass 

@app.route('api/v1/adjust-account-balance/<amount>', methods = ["PUT"])
def adjustAccountBalance(amount):
    pass 




