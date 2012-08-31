#!/usr/bin/env python

from flask import *

# The WSGI configuration on Elastic Beanstalk requires 
# the callable be named 'application' by default.
application = Flask(__name__)

# Setup the root route of the website, and render the 'index.html' template
@application.route("/")
def default():
	#display welcome page
	return render_template('index.html')

@application.route("/page2")
def page2():
	return render_template('page2.html')

if __name__ == '__main__':
	application.debug = True
	application.run(host='0.0.0.0')
