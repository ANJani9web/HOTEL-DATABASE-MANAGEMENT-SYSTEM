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
def event():
    if request.method == "POST":
        user_id=request.form.get('User_id')
        password=request.form.get('Password')
        hall_name=request.form.get('Hall_name')
        event_name=request.form.get('Event_name')
        guest=request.form.get('Guest')
        event_date=request.form.get('Event_date')
        start_time=request.form.get('Start_time')
        end_time=request.form.get('End_time')
        flag=0
        cursor.execute("delete from dine_book where Event_date<CURDATE();")
        db.commit()
        cursor.execute("select * from register where User_id=%s and Password=%s;",(str(user_id),str(password)))
        myresult = cursor.fetchall()
        if len(myresult)==1:
            flag=1
        cursor.execute("select * from event_book")
        myresult = cursor.fetchall()
        l=len(myresult)
        if l>100:
         return "sorry no space available"

        max1=1

        for i in range(0,len(myresult)):
          max1=max(max1,myresult[i][0])
        c=max1+1
        if flag==1:
            cursor.execute("INSERT INTO event_book(eventid,User_Id,Hall_name,Event_name,Guest,Event_date,Start_time,End_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(c,user_id,hall_name,event_name,guest,event_date,start_time,end_time))
            
            db.commit()
            return "you are booked your eventid is "+str(c) 
            


        else:
            return render_template("a.html")




        # cursor.execute("INSERT INTO event_book(User_Id,Hall_name,Event_name,Guest,Event_date,Start_time,End_time) VALUES(%s,%s,%s,%s,%s,%s,%s)",(user_id,hall_name,event_name,guest,event_date,start_time,end_time))
        # db.commit()
        db.close()

	

       	
       
        # return "you are booked"
    return render_template("event.html")
 
if __name__=='__main__':
   app.run(port=7312)



