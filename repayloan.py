from flask import session,redirect,render_template
from database import get_db_connection
import razorpay

def repay(request):
    if 'username' in session:
        try:
            if request.method == "GET":
                username=session['username']
                conn=get_db_connection()
                cur=conn.cursor()
                sql='select * from activeLoans where username=?'
                val=(username,)
                cur.execute(sql,val)
                data=cur.fetchone()
                bname=data[1]
                loantype=data[2]
                amount=data[3]
                client=razorpay.Client(auth=("rzp_test_EQcdLLLhDGxxyz","RvoLosmtN5LnL2vCm8LjCadu"))
                payment=client.order.create({'amount':int(amount)*100,'currency':'INR','payment_capture':'1'})
                return render_template('repay.html',bname=bname,loantype=loantype,amount=amount,payment=payment)
        except:
            return "User Not Have Any Active Loans"
    else:
        redirect('/')