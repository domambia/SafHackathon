from  app import db 
import datetime 

class SimCard(db.Model):
    id         = db.Column(db.Integer, primary_key  = True, index  = True)
    ICCID      = db.Column(db.String(255), unique = True)
    IMSI       = db.Column(db.String(255))
    Ki         = db.Column(db.String(255))
    PIN1       = db.Column(db.String(255))
    PUC        = db.Column(db.String(255))  
    status     = db.Column(db.Integer, default  = 0)
    joined     = db.Column(db.DateTime, default = datetime.datetime.now)
    MSISDN      = db.Column(db.String(12), unique = True)
    balance     = db.Column(db.Integer, default  = 0)
    

    def __str__(self):
        return self.ICCID     


