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
def staffinsert():
    if request.method == "POST":
        name=request.form.get('name')
        designation=request.form.get('designation')
        salary=request.form.get('salary')
        number=request.form.get('number')
        cursor.execute("select * from staff")
        myresult = cursor.fetchall()
        max1=0
        for x in myresult:
            if x[0]>max1:
                max1=x[0]
        max1=max1+1
        cursor.execute("insert into staff(id,name,designation,salary,mobilenumber) values(%s,%s,%s,%s,%s)",(max1,name,designation,salary,number))
        db.commit()
        return "Staff Inserted"

        
        

        
        
        
       
        
    return render_template("staffinsert.html")
 
if __name__=='__main__':
   app.run(port=7307)


# "INSERT INTO room_book(User_Id,Room_name,Arrival,Departure,Rooms,Adults,Children) VALUES(user_id,room_name,arrival,departure,rooms,adults,children)";




