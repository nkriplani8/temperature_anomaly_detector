import conf, json, time 
from boltiot import Sms, Bolt

min_limit = 300
max_limit = 350

mybolt = Bolt(conf.akey, conf.did)
Sms = Sms(comf.sid, conf.token, conf.tno, conf.fno)

while True:
	print("Reading sensor value")
	response = mybolt.analogRead('A0')
	data = json.loads(response)
	print("Sensor value is: " + str(data['value']))
	try:
		sensor_value = int(data['value'])
		if sensor_value > max_limit or sensor_value < min_limit:
			print("Making quest to twilio to send sms")
			response = Sms.send_sms("The current temp value is "+str(sensor_value))
			print("Response recived from twilio is: "+str(response))
			print("Status of sms at twilio is: "+str(response.status))
	except Exception as e:
		print("Error occured: Below are the details")
		print(e)
	time.sleep(10)