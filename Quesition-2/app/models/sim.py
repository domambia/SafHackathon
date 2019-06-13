from  app import db 
import datetime 

class SimCard(db.Model):
    id         = db.Column(db.Integer, primary_key  = True,  unique = True, index  = True)
    ICCID      = db.Column(db.String(20), unique = True)
    IMSI       = db.Column(db.String(15), unique  = True) 
    Ki         = db.Column(db.String(15), unique  = True) 
    PIN1       = db.Column(db.String(15), unique  = True) 
    PUC        = db.Column(db.String(15), unique  = True)   
    status     = db.Column(db.Integer, default  = 0)
    MSISDN     = db.Column(db.String(12), unique = True)
    joined     = db.Column(db.DateTime, default = datetime.datetime.now)

    def __str__(self):
        return self.MSISDN     