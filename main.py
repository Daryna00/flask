from flask import Flask, render_template, request, json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registerPage')
def register():
    return render_template('form.html')



@app.route('/signUp', methods=['POST'])
def register_ajax():
    form_login = request.form['login']
    form_email = request.form['email']
    form_password = request.form['password']

    print(form_login, form_email, form_password)
    if form_login and form_email and form_password:
        return json.dumps({'html': '<span class="text-success">Registration is fine</span>'})
    else:
        return json.dumps({'html': '<span class="text-success">Registration failed</span>'})



if __name__ == '__main__':
    app.run(debug=True)