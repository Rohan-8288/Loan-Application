import sqlite3

def get_db_connection():
    conn = sqlite3.connect('loanapp.db')
    return conn


def create_tables():
    conn=get_db_connection()
    cur=conn.cursor()

    cur.execute('create table if not exists register(fname varchar(20),lname varchar(20),email varchar(50) unique,phoneno varchar(10) unique,username varchar(20) primary key,password varchar(15));')

    cur.execute('create table if not exists banks(id integer primary key autoincrement,logo varchar(100),bankname varchar(50));')


    cur.execute('create table if not exists loan_applications(id integer primary key autoincrement,fname varchar(20) not null,lname varchar(20) not null,fathername varchar(20) not null,mothername varchar(20) not null,username varchar(30) not null,bname varchar(20) not null,loantype varchar(30) not null,email varchar(30) not null,phoneno varchar(10) not null,dob date,caddress varchar(300),paddress varchar(300),adhar varchar(12) unique,pan varchar(10) unique,passportimage varchar(50));')

    cur.execute('create table if not exists activeLoans(username varchar(30) primary key,bname varchar(20),loantype varchar(20),amount int);')



def employment():
    conn=get_db_connection()
    cur=conn.cursor()

    sql='create table if not exists student_employment(year varchar(20),"Personal Loan" int,"Education Loan" int);'
    cur.execute(sql)

    sql='insert into student_employment values(?,?,?);'
    val=('1st year',10000,100000)
    cur.execute(sql,val)
    conn.commit()

    val=('2nd year',20000,150000)
    cur.execute(sql,val)
    conn.commit()

    val=('3rd year',30000,200000)
    cur.execute(sql,val)
    conn.commit()

    val=('4th year',40000,250000)
    cur.execute(sql,val)
    conn.commit()

    sql='create table if not exists topcollege_student(year varchar(20),"Personal Loan" int,"Education Loan" int);'
    cur.execute(sql)

    sql='insert into topcollege_student values(?,?,?);'
    val=('1st year',15000,120000)
    cur.execute(sql,val)
    conn.commit()

    val=('2nd year',25000,170000)
    cur.execute(sql,val)
    conn.commit()

    val=('3rd year',35000,230000)
    cur.execute(sql,val)
    conn.commit()

    val=('4th year',40000,300000)
    cur.execute(sql,val)
    conn.commit()


    sql='create table if not exists self_employed(anualincome int,"Personal Loan" int,"Education Loan" int,"Home Loan" int,"Car Loan" int);'
    cur.execute(sql)

    sql="insert into self_employed values(?,?,?,?,?)"
    val=(500000,15000,150000,1000000,200000)
    cur.execute(sql,val)
    conn.commit()

    val=(600000,20000,200000,1500000,300000)
    cur.execute(sql,val)
    conn.commit()

    val=(700000,25000,250000,2000000,350000)
    cur.execute(sql,val)
    conn.commit()

    val=(800000,30000,300000,2500000,400000)
    cur.execute(sql,val)
    conn.commit()

    val=(900000,35000,350000,3000000,500000)
    cur.execute(sql,val)
    conn.commit()

    val=(1000000,40000,400000,3500000,600000)
    cur.execute(sql,val)
    conn.commit()


    sql='create  table if not exists salaried(mothlyincome int,"Personal Loan" int,"Education Loan" int,"Home Loan" int,"Car Loan" int);'
    cur.execute(sql)

    sql="insert into salaried values(?,?,?,?,?)"

    val=(40000,12000,120000,900000,150000)
    cur.execute(sql,val)
    conn.commit()

    val=(50000,15000,150000,1000000,200000)
    cur.execute(sql,val)
    conn.commit()

    val=(60000,20000,200000,1500000,300000)
    cur.execute(sql,val)
    conn.commit()

    val=(70000,25000,250000,2000000,350000)
    cur.execute(sql,val)
    conn.commit()

    val=(80000,30000,300000,2500000,400000)
    cur.execute(sql,val)
    conn.commit()

    val=(90000,35000,350000,3000000,500000)
    cur.execute(sql,val)
    conn.commit()

    val=(100000,40000,400000,3500000,600000)
    cur.execute(sql,val)
    conn.commit()
