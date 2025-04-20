from flask import redirect,render_template,session,url_for,request
from database import get_db_connection
import hmac
import hashlib

# def cardpay(request):
#     if 'username' in session:
#         if request.method == "GET":
#             amount=session['loanamt']
#             return render_template('card.html',amount=amount)
#         else:
#             username=session['username']
#             conn=get_db_connection()
#             cur=conn.cursor()

#             sql='delete from activeLoans where username=?'
#             val=(username,)
#             cur.execute(sql,val)
#             conn.commit()
#             return redirect('/apply_loan')
#     else:
#         return redirect('/')


def verify_payment():
    data = request.form
    order_id = data.get('razorpay_order_id')
    payment_id = data.get('razorpay_payment_id')
    signature = data.get('razorpay_signature')

    generated_signature = hmac.new(
        bytes("RvoLosmtN5LnL2vCm8LjCadu", 'utf-8'),  # your Razorpay secret
        bytes(f"{order_id}|{payment_id}", 'utf-8'),
        hashlib.sha256
    ).hexdigest()

    if generated_signature == signature:
        return "Payment successful and verified!"
    else:
        return "Payment verification failed.", 400
