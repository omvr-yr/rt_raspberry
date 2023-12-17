from flask import Flask, render_template
# To comment when you're working on local
# import RPi.GPIO as GPIO
import time
import sys

# To comment when you're working on local
# GPIO.setmode(GPIO.BOARD)

doors_pin = 11
drawer_pin = 13

# To comment when you're working on local
# GPIO.setup(doors_pin, GPIO.OUT)
# GPIO.setup(drawer_pin, GPIO.OUT)

# To comment when you're working on local
#from interrupteur.py import ouverture, fermeture

print("H800X generator monitor app is running...")

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def door_closed():
    return render_template('door-closed.html')
    
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    
@app.route('/parameters')
def parameters():
    return render_template('parameters.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/help')
def help():
    return render_template('help.html')
    
@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/open_system')
def open_system():
    return render_template('open-system.html')

@app.route('/open', methods=['POST'])
def open():
	print("Opening doors ...")
# 	To comment when you're working on local
# 	GPIO.output(doors_pin, GPIO.HIGH)
	time.sleep(12)
	print("Opening drawer ...")
# 	To comment when you're working on local
# 	GPIO.output(drawer_pin, GPIO.HIGH)
	time.sleep(12)
	print("DOORS AND DRAWER ARE OPENED")
	return 'DOORS AND DRAWER ARE OPENED'

@app.route('/close', methods=['POST'])
def close():
	print("Closing drawer ...")
# 	To comment when you're working on local
# 	GPIO.output(drawer_pin, GPIO.LOW)
	time.sleep(12)
	print("Closing doors ...")
# 	To comment when you're working on local
# 	GPIO.output(doors_pin, GPIO.LOW)
	time.sleep(12)
	print("DOORS AND DRAWER ARE CLOSED")
	return 'DOORS AND DRAWER ARE CLOSED'

if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1')
