from database import get_db_connection
from flask import redirect, url_for, flash

def registerdata(request):
    fname=request.form['fname']
    lname=request.form['lname']
    email=request.form['email']
    phoneno=request.form['phoneno']
    username=request.form['username']
    password=request.form['password']

    conn=get_db_connection()
    cur=conn.cursor()

    cur.execute("SELECT * FROM register WHERE username=?", (username,))
    existing_user = cur.fetchone()

    if existing_user:
        flash("Username already taken.")
        return redirect(url_for('register'))
    else:
        sql="insert into register(fname,lname,email,phoneno,username,password)values(?,?,?,?,?,?)"
        val=(fname,lname,email,phoneno,username,password)
        cur.execute(sql,val)
        conn.commit()
        flash("Registration successful! Please log in.")
