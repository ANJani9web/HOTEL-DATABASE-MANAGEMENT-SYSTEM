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
def room():
    if request.method == "POST":
        user_id=request.form.get('User_id')
        password=request.form.get('Password')
        room_name=request.form.get('Room_name')
        arrival=request.form.get('Arrival')
        departure=request.form.get('Departure')
        rooms=request.form.get('Rooms')
        adults=request.form.get('Adults')
        children=request.form.get('Children')
        flag=0
        cursor.execute("delete from room_book where Departure<CURDATE();")
        db.commit()
        cursor.execute("select * from register where User_id=%s and Password=%s;",(str(user_id),str(password)))
        myresult = cursor.fetchall()
        if len(myresult)==1:
            flag=1
        cursor.execute("select * from room_book")
        myresult = cursor.fetchall()
        l=len(myresult)
        if l>100:
         return "sorry no rooms available"
        max1=1
        for i in range(1,len(myresult)):
          max1=max(max1,myresult[i][0])
        c=max1+1
        if flag==1:
            cursor.execute("INSERT INTO room_book(roomid,User_Id,Room_name,Arrival,Departure,Rooms,Adults,Children) values(%s,%s,%s,%s,%s,%s,%s,%s);",(c,user_id,room_name,arrival,departure,rooms,adults,children))
            db.commit()
        # db.close()
            return "room booked"
        else:
            return render_template("a.html")
    return render_template("room.html")
 
if __name__=='__main__':
   app.run(port=5000)


# "INSERT INTO room_book(User_Id,Room_name,Arrival,Departure,Rooms,Adults,Children) VALUES(user_id,room_name,arrival,departure,rooms,adults,children)";




