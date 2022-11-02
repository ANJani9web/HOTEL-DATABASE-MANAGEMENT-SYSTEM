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
def dine():
    if request.method == "POST":


       user_id=request.form.get('User_id')
       
       password=request.form.get('Password')
       table_name=request.form.get('Table_name')
       guest=request.form.get('Guest')
       dine_date=request.form.get('Date')
       dine_time=request.form.get('Time')
       request1=request.form.get('Request')
       flag=0
       cursor.execute("delete from dine_book where Event_date<CURDATE();")
       db.commit()

       cursor.execute("select * from register where User_id=%s and Password=%s;",(str(user_id),str(password)))
       myresult = cursor.fetchall()
       if len(myresult)==1:
            flag=1
       cursor.execute("select * from dine_book")
       myresult = cursor.fetchall()
       l=len(myresult)
       if l>100:
        return "sorry no tables available"
       max1=1

       for i in range(1,len(myresult)):
          max1=max(max1,myresult[i][0])
       c=max1+1
       
        
        # return render_template('dine.html',msg="Sorry! No tables available")

       if flag==1:
         cursor.execute("insert into dine_book(dineid,User_Id,Table_name,Guest,Event_date,Event_time,Request) values(%s,%s,%s,%s,%s,%s,%s);",(c,user_id,table_name,guest,dine_date,dine_time,request1))
         db.commit()
         # db.close()
         return "you are booked"

       else:
         return render_template("a.html")



      #  cursor.execute("insert into dine_book(User_Id,Table_name,Guest,Event_date,Event_time,Request) values(%s,%s,%s,%s,%s,%s);",(user_id,table_name,guest,dine_date,dine_time,request1))
      #  db.commit()
      #  db.close()
       
    return render_template("dine.html")
 
if __name__=='__main__':
   app.run(port=7306)


