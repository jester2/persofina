from app import create_app
from flask import request

app = create_app()

@app.route('/')
def index():
	user_agent = request.headers.get('User_Agent')
	return '<p>Your browser is %s</p>' % user_agent

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' % name

# The below line is used to ensure that the development
# web serveris started only when the script is executed
# directly.  When the script is imported by another script
# it is assumed that the parent script will launch a different
# server, so the app.run() call gets skipped
if __name__ == '__main__':
	app.run(debug=True)
