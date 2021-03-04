
from twilio.rest import Client
import yaml


yaml.warnings({'YAMLLoadWarning': False})
conf = yaml.load(open('voice.yml'))
login = conf['user']['login']
pwd = conf['user']['password']
twilionum = conf['user']['phonenumber']
mynumber = conf['user']['myphonenumber']

client = Client(login, pwd)

message = ('Hello from Python!')

client.messages.create(to=mynumber, from_=twilionum, body=message)






#https://www.fullstackpython.com/blog/send-sms-text-messages-python.html