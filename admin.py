from flask import render_template,redirect,url_for
from database import get_db_connection
from werkzeug.utils import secure_filename

def adminData(request):
    if request.method == "GET":
        return render_template("admin.html")
    else:
        f=request.files['logo']
        filename=secure_filename(f.filename)
        filename="static/dbimages/"+filename
        f.save(filename)

        filename="dbimages/"+f.filename

        bname=request.form['bname']
        conn=get_db_connection()
        cur=conn.cursor()
        sql="insert into banks(logo,bankname) values(?,?)"
        val=(filename,bname)
        cur.execute(sql,val)
        conn.commit()
        return redirect(url_for('admin'))    