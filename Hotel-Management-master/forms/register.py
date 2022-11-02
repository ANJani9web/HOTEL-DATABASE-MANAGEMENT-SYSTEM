import mysql.connector

db=mysql.connector.connect(host='localhost',
                           database='dine',
                           user='root',
                           password='Yash@123')

cursor=db.cursor()


# importing Flask and other modules
from flask import Flask, request, render_template
 
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def register():
    if request.method == "POST":
        name=request.form.get('Name')
        gender=request.form.get('Gender')
        mob_no=request.form.get('Phone')
        email=request.form.get('Email_id')
        password=request.form.get('Password')
        age=request.form.get('Age')
        bdate=request.form.get('Birthdate')
        country=request.form.get('Country')
        state=request.form.get('State')
        city=request.form.get('City')
        locality=request.form.get('Locality')
        cursor.execute("select * from register")
        myresult = cursor.fetchall()
        max1=myresult[0][0]

        for i in range(1,len(myresult)):
            max1=max(max1,myresult[i][0])
        c=max1+1

        cursor.execute("INSERT INTO Register(User_Id,Name,Gender,Mob_no,Email,Password,Age,Country,State,City,Locality,Birth_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(c,name,gender,mob_no,email,password,age,country,state,city,locality,bdate))
        db.commit()
        db.close()
        return "you are booked your userid is {}".format(c)
    return render_template("register.html")
 
if __name__=='__main__':
   app.run(port=8000)
   