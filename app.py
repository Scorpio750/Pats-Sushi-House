from flask import Flask, render_template, request
import random
from twilio.rest import TwilioRestClient

app = Flask(__name__)

menu = [
		('california', 'California Roll'),
		('tuna', 'Tuna Roll'),
		('teriyaki', 'Teriyaki Roll'),
		('soft crab', 'Soft Crab Roll'),
		('tsunami', 'Tsunami Roll')
		]

@app.route('/')
def home():
	return render_template('index.html', menu=menu)

@app.route('/order')
def order():
	sushi = request.args['sushi']
	time = random.choice(range(5, 41, 5))
	return render_template('order.html', sushi=sushi, time=time)

if __name__ == '__main__':
	app.run('0.0.0.0', port=2000, debug=True)
