from flask import session,render_template,redirect
from database import get_db_connection
from werkzeug.utils import secure_filename

def loanApp(request,bank_id):
    if 'username' in session:
        username = session['username']
        conn = get_db_connection()
        cur = conn.cursor()
        sql = 'select username from activeLoans where username=?;'
        val = (username,)
        cur.execute(sql, val)
        result = cur.fetchone()
        if result:
            return render_template('notEligible.html',username=username)
        else:   
            if request.method == "GET":
                conn=get_db_connection()
                cur=conn.cursor()
                sql="select * from banks where id=?"
                val=(bank_id,)
                cur.execute(sql,val)
                data=cur.fetchone()
                bankname=data[2]
                username=session['username']                                      
                loantype=session['loantype']
                return render_template('application.html',bname=bankname,username=username,loantype=loantype)
            else:
                try:
                    fname=request.form['fname']
                    lname=request.form['lname']
                    fathername=request.form['fathername']
                    mothername=request.form['mothername']
                    user=request.form['uname']
                    bname=request.form['bname']
                    loantype=request.form['loantype']
                    email=request.form['email']
                    phoneno=request.form['mobileno']
                    dob=request.form['dob']
                    caddress=request.form['caddress']
                    paddress=request.form['paddress']
                    adhar=request.form['adhar']
                    pan=request.form['pan']

                    passport=request.files['passportimage']
                    passportfile=secure_filename(passport.filename)
                    passportfile="static/passportphotos/"+passportfile
                    passport.save(passportfile)
                    passportfile="passportphotos/"+passport.filename

                    session['bname']=bname                                    #creating session for Bank Name


                    conn=get_db_connection()
                    cur=conn.cursor()
                    sql="insert into loan_applications(fname,lname,fathername,mothername,username,bname,loantype,email,phoneno,dob,caddress,paddress,  adhar,pan,passportimage) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

                    val=(fname,lname,fathername,mothername,user,bname,loantype,email,phoneno,dob,caddress,paddress,adhar,pan,passportfile)

                    cur.execute(sql,val)
                    conn.commit()
                    return redirect('/checkEligibility')
                except:
                    return "Error 404"
    else:
        return redirect('/')
    




    #     if request.method == "GET":
    #     conn=get_db_connection()
    #     cur=conn.cursor()
    #     sql="select * from banks where id=?"
    #     val=(bank_id,)
    #     cur.execute(sql,val)
    #     data=cur.fetchone()
    #     bankname=data[2]
    #     username=session['username']                                      
    #     loantype=session['loantype']
    #     return render_template('application.html',bname=bankname,username=username,loantype=loantype)
    # else:
    #     fname=request.form['fname']
    #     lname=request.form['lname']
    #     fathername=request.form['fathername']
    #     mothername=request.form['mothername']
    #     user=request.form['uname']
    #     bname=request.form['bname']
    #     loantype=request.form['loantype']
    #     email=request.form['email']
    #     phoneno=request.form['mobileno']
    #     dob=request.form['dob']
    #     caddress=request.form['caddress']
    #     paddress=request.form['paddress']
    #     adhar=request.form['adhar']
    #     pan=request.form['pan']

    #     passport=request.files['passportimage']
    #     passportfile=secure_filename(passport.filename)
    #     passportfile="static/passportphotos/"+passportfile
    #     passport.save(passportfile)
    #     passportfile="passportphotos/"+passport.filename

    #     session['bname']=bname                                    #creating session for Bank Name


    #     conn=get_db_connection()
    #     cur=conn.cursor()
    #     sql="insert into loan_applications(fname,lname,fathername,mothername,username,bname,loantype,email,phoneno,dob,caddress,paddress,  adhar,pan,passportimage) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

    #     val=(fname,lname,fathername,mothername,user,bname,loantype,email,phoneno,dob,caddress,paddress,adhar,pan,passportfile)

    #     cur.execute(sql,val)
    #     conn.commit()
    #     return redirect('/checkEligibility')