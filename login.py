from flask import redirect,render_template,flash,session,url_for
from database import get_db_connection

def loginpage(request):
    if request.method == "GET":
        return render_template('login.html')
    else:
        usename_1=request.form['username']
        password_1=request.form['password']

        conn=get_db_connection()
        cur=conn.cursor()
        sql="select * from register where username=?"
        val=(usename_1,)
        cur.execute(sql,val)
        user = cur.fetchone()

        if usename_1 == user[4] and password_1 == user[5]:
            session['username']=user[4]                                #Creating Session For Username
            return render_template('home.html')
        else:
            flash("Invalid username or password")
            return redirect(url_for('login'))