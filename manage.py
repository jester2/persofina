from app import create_app
from flask import redirect, abort

app = create_app()

@app.route('/')
def index():
	return redirect("http://www.google.com")

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' % name

@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello, %s</h1>' % user.name
	
# The below line is used to ensure that the development
# web serveris started only when the script is executed
# directly.  When the script is imported by another script
# it is assumed that the parent script will launch a different
# server, so the app.run() call gets skipped
if __name__ == '__main__':
	app.run(debug=True)
