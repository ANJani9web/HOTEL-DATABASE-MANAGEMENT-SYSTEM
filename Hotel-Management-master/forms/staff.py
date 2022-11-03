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
def staff():
    if request.method == "POST":
        room_id=request.form.get('roomid')
        room_no=request.form.get('roomnumber')
        x=1

        
        flag=0

        
        cursor.execute("select * from room_book where roomid=%s and Rooms=%s;",(room_id,x))
        # cursor.execute("select * from room_book where roomid=%s;",(room_id,room_no))
        # print(user_id,password)
        myresult = cursor.fetchall()
        if len(myresult)==1:
            flag=1
        
        if flag==1:
            # cursor.execute("select * from room_book where roomid=(%s);",(room_id))
            cursor.execute("select * from room_book where roomid=%s and Rooms=%s;",(room_id,x))
            na=cursor.fetchall()
            c=na[0][1]
            cursor.execute("INSERT INTO rooms(roomid,roomnumber,User_Id) values(%s,%s,%s);",(room_id,room_no,c))
            db.commit()
        # db.close()
            return "enjoy your stay"
        else:
            return 'sorry no room booked with this id'
        # return f'{room_id}'
    return render_template("staff_service.html")
 
if __name__=='__main__':
   app.run(port=7307)


# "INSERT INTO room_book(User_Id,Room_name,Arrival,Departure,Rooms,Adults,Children) VALUES(user_id,room_name,arrival,departure,rooms,adults,children)";




