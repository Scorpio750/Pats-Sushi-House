from flask import Flask, render_template, request
import random
from twilio.rest import TwilioRestClient

app = Flask(__name__)

menu = [
		('california', 'California Roll','sushi1.gif'),
		('tuna', 'Tuna Roll','sushi2.png'),
		('teriyaki', 'Teriyaki Roll','sushi3.png'),
		('soft crab', 'Soft Crab Roll','sushi4.png'),
		('tsunami', 'Tsunami Roll','sushi5.jpeg')
		]

@app.route('/')
def home():
	return render_template('index.html', menu=menu)

@app.route('/order')
def order():
	sushi = request.args['sushi']
	time = random.choice(range(5, 41, 5))
	return render_template('order.html', sushi=sushi, time=time)

	from twilio.rest import TwilioRestClient 

	# credentials here 
	ACCOUNT_SID = "AC22f2a7b4bd38d88ed3c196a7e8b29b85" 
	AUTH_TOKEN = "e38445dfc0ae60cae15cc44b3734b9f2" 

	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

	client.messages.create( 
			from_="+18622608699",   
			)

if __name__ == '__main__':
	app.run('0.0.0.0', port=2000, debug=True)
