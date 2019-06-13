from app import app 
from app import db 
from flask import jsonify, request
from app.models.sim import SimCard 
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
        "message": "Success",
        "content":{
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
    data  = request.get_json(silent=True)
    if data is None:
        print("Omambia")
        results  = {
            "message": "Error",
            "content": {
                "Name Cannot be empty",
            },
            "status_code": 1}
        return jsonify({"omambia": "jen"})

    MSISDN = generators.get_MSISDN()
    ICCID = generators.get_ICCID()
    IMSI  = generators.get_IMSI()
    PUC  = generators.get_puc()
    PIN1 = generators.get_pin()
    Ki   = generators.get_pin()

    try: 
        sim   = SimCard(MSISDN = MSISDN, ICCID = ICCID, IMSI = IMSI, PUC = PUC,PIN1 = PIN1, Ki = Ki)
        db.session.add(sim)
        db.session.commit()

        # print(data["name"])
        results  = {
            "message": "Success",
            "content": {
                "MSISDN": MSISDN,
                "PIN1": PIN1,
                "ICCID": ICCID,
                "Ki": Ki,
                "IMSI": IMSI,
                "PUC": PUC,
                "status": 0 },"status_code": 0
        }
        return jsonify(results)

    except Exception as e:
        print(e)
        return jsonify({"message": "server Error", "status_code": 500, "content": "Error happened"})


@app.route('/api/v1/activation-of-simcard/<MSISDN>/<ICCID>/<IMSI>/', methods  = ['PUT'])
def activateSim(MSISDN, ICCID, IMSI):
    if MSISDN is None or ICCID is None or IMSI is None:
        return jsonify(
                    {"message": "Error coccurred", 
                    "content": {"ICCID or MSISD or IMSI cannot be empty"}, 
                    "status_code": 1}), 404

    sim  = SimCard.query.filter(SimCard.ICCID == ICCID, SimCard.IMSI == IMSI, SimCard.MSISDN = MSISDN).first()
    if sim is None:
        return jsonify(
                        {"message": "No record found", 
                        "content": {"No records found "}, 
                        "status_code": 0}), 200
    return jsonify(
         {
            "message": "Success",
            "content": {
                "MSISDN": sim.MSISDN,
                "PIN1": sim.PIN1,
                "ICCID": sim.ICCID,
                "Ki": sim.Ki,
                "IMSI": sim.IMSI,
                "PUC": sim.PUC,
                "status": 0 },"status_code": 0
        }
    ), 200


@app.route('/api/v1/maintain-account<MSISD>/', methods = ["PUT"])
def maintainAcccount(MSISDN):
    if MSISDN is None:
        return jsonify({"message": "no record was found by the MSISDN", "content": {"None"}, "status_code": 1}), 404
    sim  = SimCard.query.filter(SimCard.MSISDN == MSISDN).first()
    if sim:
        return jsonify(
                {"message": "MSISDN found",
                "content": {
                "MSISDN": sim.MSISDN,
                "PIN1": sim.PIN1,
                "ICCID": sim.ICCID,
                "Ki": sim.Ki,
                "IMSI": sim.IMSI,
                "PUC": sim.PUC,
                "status": 0 },
                "status_code": 0 }), 200

    return jsonify({"message": "no record was found by the MSISDN", "content": {"None"}, "status_code": 1}), 404 

@app.route('/api/v1/adjust-account-balance/<amount>', methods = ["PUT"])
def adjustAccountBalance(amount):
    pass 




