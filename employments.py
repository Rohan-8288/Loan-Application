from flask import redirect,render_template,session,url_for
import math
from database import get_db_connection

def employmentTypes(request):
    employment_type=request.form['employment_type']
    loantype=session['loantype']

    if employment_type == "Student":
        if loantype in ["Home Loan","Car Loan"]:
            return render_template('notEligible.html')
        else:
            year = request.form['year'].lower()
            college=request.form['college'].lower()
            print(college)

            if college in ['iit','nit','coep','iim','bhu']:
                conn=get_db_connection()
                cur=conn.cursor()
                sql=f'select "{loantype}" from topcollege_student where year=?'
                val=(year,)
                cur.execute(sql,val)
                loanamt=cur.fetchone()
                print(loanamt[0])
                session['loanamt']=loanamt[0]
                return redirect(url_for('send_email_route'))
            else:
                conn=get_db_connection()
                cur=conn.cursor()

                sql=f'select "{loantype}" from student_employment where year=?'
                val=(year,)
                cur.execute(sql,val)

                loanamt=cur.fetchone()
                session['loanamt']=loanamt[0]

                return redirect(url_for('send_email_route'))

    elif employment_type == "Self-Employed":
        try:
            annual_income = int(request.form['income'])
            income=math.floor(annual_income)
        except ValueError:
            return "Invalid income input"
        conn=get_db_connection()
        cur=conn.cursor()
        if 500000 <= income <= 1000000:
            sql=f'select "{loantype}" from self_employed where anualincome=?'
            val=(income,)
            cur.execute(sql,val)
            loanamt=cur.fetchone()
            session['loanamt']=loanamt[0]
            return redirect(url_for('send_email_route'))
        elif income >= 1000000:
            sql=f'select "{loantype}" from slef_employed where anualincome=?'
            val=(1000000,)
            cur.execute(sql,val)
            loanamt=cur.fetchone()
            session['loanamt']=loanamt[0]
            return redirect(url_for('send_email_route'))
        else:
            return render_template('notEligible.html')


    elif employment_type == "Salaried":
        try:
            monthly = int(request.form['monthly'])
            income=math.floor(monthly)
        except ValueError:
            return "Invalid income input"
        conn=get_db_connection()
        cur=conn.cursor()
        if 40000 <= income <= 100000:
            sql=f'select "{loantype}" from salaried where monthlyincome=?'
            val=(income,)
            cur.execute(sql,val)
            loanamt=cur.fetchone()
            session['loanamt']=loanamt[0]
            return redirect(url_for('send_email_route'))
        elif income >= 100000:
            sql=f'select "{loantype}" from salaried where monthlyincome=?'
            val=(100000,)
            cur.execute(sql,val)
            loanamt=cur.fetchone()
            session['loanamt']=loanamt[0]
            return redirect(url_for('send_email_route'))
        else:
            return render_template('notEligible.html')