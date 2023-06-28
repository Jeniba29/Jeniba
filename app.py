from flask import Flask,render_template,request
import mysql.connector
user_dict={'admin':'1234','user':'5678'}
conn = mysql.connector.connect(host='localhost',user='root',password='',database='sms')
mycursor=conn.cursor()
#create a flask application
app = Flask(__name__)

#Define the route 

@app.route('/')
def hello():
    return render_template('first.html')
@app.route('/student')
def student():
    return render_template('stu.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/About_Us')
def About_Us():
    return render_template('about.html')

@app.route('/home',methods=['POST'])

def home():
    uname=request.form['username']
    pwd=request.form['password']

    if uname not in user_dict:
        return render_template('login.html',msg='Invalid User')
    elif user_dict[uname] != pwd:
        return render_template('login.html',msg='Invalid Password')
    else:
        return render_template('home.html')
@app.route('/view')
def view():
    query="SELECT * FROM student"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)

@app.route('/search')
def searchpage():
    return render_template('search.html')


@app.route('/searchresult',methods=['POST'])
def search():
    stu_id = request.form['stu_id']
    query="SELECT * FROM student WHERE stu_id="+stu_id
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)
    
@app.route('/add')
def add():
    return render_template('stu.html')

@app.route('/read',methods=['POST'])
def read():
    stu_id = request.form['stu_id']
    stu_name = request.form['stu_name']
    gender= request.form['gender']
    dob= request.form['dob']
    email = request.form['email']
    query = "INSERT INTO student(stu_id,stu_name,gender,dob,email) VALUES (%s,%s,%s,%s,%s)"
    data = (stu_id,stu_name,gender,dob,email)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('stu.html',msgdata='Added Successfully')

#Run the flask app
if __name__=='__main__':
    app.run(port=5003,debug = True)