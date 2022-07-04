from  fastapi import FastAPI
from .schemas import UssdInfo

app = FastAPI()

@app.get('/')
def home():
    return 'home page'


@app.post('/')
def home(ussd_info: UssdInfo):
    if ussd_info.text == '':
        response ='CON welcome to airtime module \n'
        response +='enter phone number to buy aitime'

    return response