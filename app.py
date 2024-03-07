from flask import Flask, render_template,request,flash, redirect, url_for
from registration_form import UserForm
from server_connect import User_model

app = Flask(__name__)
app.secret_key= "private_key"

@app.route("/")
def home():
    return render_template('home.html')



    
@app.route("/login")
def login():
    reg_form = UserForm()
    return render_template('login.html', form = reg_form)
    



@app.route("/registration", methods=['POST', 'GET'])
def registration():
    reg_form = UserForm()
    obj = User_model()

    if request.method == 'POST':
        if reg_form.validate():
            obj.server_upload(reg_form)
            return redirect(url_for('successful'))
        else:
            flash("Please fill out all fields")
            return render_template("register.html", form=reg_form)

    elif request.method == 'GET':
        return render_template("register.html", form=reg_form)



@app.route('/successful')
def successful():
    name = request.args.get("name")
    return render_template('success_page.html')

    if __name__ == "__main__":
        app.run(debug=True)