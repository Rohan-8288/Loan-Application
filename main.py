from flask import Flask,redirect,render_template,request,url_for,session,flash
from database import get_db_connection 
from registerpage import registerdata
from loanApplication import loanApp
from employments import employmentTypes
from admin import adminData
from login import loginpage
from repayloan import repay
from payment import verify_payment
from flask_mail import Mail, Message

app=Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Or use any SMTP service
app.config['MAIL_PORT'] = 587  # For Gmail
app.config['MAIL_USE_TLS'] = True  # Enable TLS
app.config['MAIL_USE_SSL'] = False  # Disable SSL
app.config['MAIL_USERNAME'] = 'rj84716@gmail.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'yvvuhyjguckcbysz'  # Your email password
app.config['MAIL_DEFAULT_SENDER'] = 'rj84716@@gmail.com'

mail=Mail(app)



app.secret_key="loanapp"

@app.route("/",methods=["GET","POST"])
def login():
    return loginpage(request)

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template('register.html')
    else:
        registerdata(request)
        return redirect(url_for('login')) 

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('loantype', None)
    session.pop('bname', None)
    session.pop('loanamt', None)
    return redirect('/') 


@app.route("/home")
def home():
    if 'username' in session:
        return render_template('home.html') 
    else:
        return redirect('/') 
    
@app.route("/admin",methods=["GET","POST"])
def admin():
    return adminData(request)

@app.route("/apply_loan",methods=["GET","POST"])
def apply_loan():
    if 'username' in session:
        if request.method == "GET":
            return render_template("loanHome.html")
    else:
        registerdata(request)
        return redirect('/') 


@app.route("/banks",methods=["GET","POST"])
def banks():
    if 'username' in session:
        if request.method == "GET":
            conn=get_db_connection()
            cur=conn.cursor()
            sql="select * from banks"
            cur.execute(sql)
            data=cur.fetchall()
            loantype = request.args.get('loantype')
            session['loantype']=loantype                    #Creating Session For Loantype
            return render_template('banks.html',data=data)
    else:
        return redirect('/') 


@app.route("/application/<int:bank_id>",methods=["GET","POST"])
def application(bank_id):
    return loanApp(request,bank_id)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        #save the data in database in future this for temporary
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))    
    return render_template('contact.html')

@app.route("/about")
def about():
    if 'username' in session:
        return render_template('about.html')
    
@app.route('/checkEligibility')
def checkEligibility():
    if 'username' in session:
        username = session['username']
        conn = get_db_connection()
        cur = conn.cursor()
        sql = 'select username from activeLoans where username=?;'
        val = (username,)
        cur.execute(sql, val)
        result = cur.fetchone()
        if result:
            return render_template('alreadyexits.html',username=username)
        else:
            return render_template('eligible.html',username=username)
    else:
        return redirect('/')
    
@app.route('/employment',methods=["GET","POST"])
def employment():
    return employmentTypes(request)

@app.route('/sanction',methods=["GET","POST"])
def sanction():
    loantype=session['loantype']
    loanamt=session['loanamt']
    if request.method=="GET":
        return render_template('loansanction.html',loantype=loantype,loanamt=loanamt)
    else:
        username=session['username']
        bname=session['bname']
        conn=get_db_connection()
        cur=conn.cursor()
        sql='insert into activeloans values(?,?,?,?)'
        val=(username,bname,loantype,loanamt)
        cur.execute(sql,val)
        conn.commit()
    return "You Amount Will Be Credited Shortly To Your Bank Account !!"

def send_email(subject, recipients, body):
    message = Message(subject, recipients=recipients)
    message.body = body
    mail.send(message)

@app.route("/send_email")
def send_email_route():
    conn=get_db_connection()
    cur=conn.cursor()
    username=session['username']
    sql='select email from register where username=?'
    val=(username,)
    cur.execute(sql,val)
    data=cur.fetchone()
    email=data[0]
    url=url_for('sanction',_external=True)  

    send_email(
        subject="Congrats ..Withdraw Your Loan Amount From EasyLend", 
        recipients=[email],  
        body=f"Congratulations! Your loan is approved. You can now withdraw your loan amount from EasyLend. Click On This Link And Fill The Bank Deatils.{url}"
    )
    return "Email sent!"

@app.route('/repayment',methods=["GET","POST"])
def repayment():
    return repay(request)

# @app.route('/carddetails',methods=["GET","POST"])
# def card():
#     return cardpay(request)

@app.route('/verify_payment', methods=['POST'])
def verify():
    return verify_payment(request)
            
if __name__ == "__main__":
    app.run(debug=True)