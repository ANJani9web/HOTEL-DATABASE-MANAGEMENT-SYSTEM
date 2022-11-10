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
def staffdelete():
    if request.method == "POST":
        id=request.form.get('id')
        name=request.form.get('staffname')
        department=request.form.get('department')
        x=1

        
        flag=0

        
        cursor.execute("select * from staff where id=%s and name=%s;",(id,name))
        # cursor.execute("select * from room_book where roomid=%s;",(room_id,room_no))
        # print(user_id,password)
        myresult = cursor.fetchall()
        if len(myresult)==1:
            flag=1
        
        if flag==1:
            # cursor.execute("select * from room_book where roomid=(%s);",(room_id))
            
            cursor.execute("select * from department where deptname=%s",(str(department),))
            myresult = cursor.fetchall()
            t=myresult[0][1]
            cursor.execute("update department set countofemployee=%s where deptname=%s;",((t-1),str(department)))
            db.commit()
            cursor.execute("delete from staff where id=%s and name=%s;",(id,name))
           
            
            
            db.commit()
            
        # db.close()
            return "Staff Deleted"
        else:
            return 'sorry no staff with this id'
        # return f'{room_id}'
    return render_template("staffdelete.html")
 
if __name__=='__main__':
   app.run(port=7307)


# "INSERT INTO room_book(User_Id,Room_name,Arrival,Departure,Rooms,Adults,Children) VALUES(user_id,room_name,arrival,departure,rooms,adults,children)";




