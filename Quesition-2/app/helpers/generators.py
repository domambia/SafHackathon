import random 
import os 
import binascii

# Main Helper to convert 

def convert(num_list):
    s  = [str(i) for i in num_list]
    res  = int("".join(s))
    return res 


def MSISDN(num_list):
    s  = [str(i) for i in num_list]
    res  = str("".join(s))
    return "2547" + str(res)

def IMSI(num_list):
    s  = [str(i) for i in num_list]
    res  = str("".join(s))
    return "63902" + str(res)

def ICCID(num_list):
    s  = [str(i) for i in num_list]
    res  = int("".join(s))
    return "8925402" + str(res)
#get the pin foru digits 
def get_pin():
    number  = []
    for x in range(5):
        number.append(random.randint(0, 9))
    code  = convert(number)
    return code


def get_puc():
    number  = []
    for x in range(7):
        number.append(random.randint(0, 9))
    code  = convert(number)
    return code


def get_ICCID():
    number  = []
    for x in range(16):
        number.append(random.randint(0, 9))
        code  = ICCID(number)
    return code


def get_IMSI():
    number  = []
    for x in range(16):
        number.append(random.randint(0, 9))
        code  = IMSI(number)
    return code


def get_Ki():
    data  = binascii.b2a_hex(os.urandom(20))
    return str(data.decode("utf-8"))

def get_MSISDN():
    number  = []
    for x in range(8):
        number.append(random.randint(0, 9))
        code  = MSISDN(number)
    return code


