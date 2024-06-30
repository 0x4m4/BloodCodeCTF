from flask import Flask, render_template, request, redirect
import base64
app = Flask(__name__)


@app.route('/')
def index():
    user = request.cookies.get("username")
    admin = request.cookies.get('admin')
    return render_template("index.html", user=user, admin=admin)


@app.route('/submit', methods=["GET"])
def submit():

    redirect_to_index = redirect('/')
    response = app.make_response(redirect_to_index)
    response.set_cookie('username', value=request.args.get("username"))
    response.set_cookie('password', value=request.args.get("password"))
    if request.args.get('username') != '' and request.args.get('password') != '':
        response.set_cookie('admin', value="False")
    return response


if __name__ == '__main__':
    app.debug = False
    app.run(host="0.0.0.0")
