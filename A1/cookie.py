from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/set_cookie', methods=['GET'])
def cookie_insertion():
	username = request.args.get('user')
	if username is None:
		username = 'default'
	response = app.make_response("<p>Cookie 'user' ({}) is set!</p>".format(username))
	response.set_cookie('user', username)
	return response

@app.route('/get_cookie')
def getcookie():
   name = request.cookies.get('user')
   return '<p>Value is: {}</p>'.format(name)

@app.route('/')
def root():
	template = "<p>{}</p>"
	ip = template.format(
		"IP Address: {}".format(request.remote_addr)
	)
	user_agent = template.format(
		"User Agent: {}".format(request.headers.get('User-Agent'))
	)

	return "".join([ip, user_agent])

app.run(host='0.0.0.0')