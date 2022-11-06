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
def service():
    if request.method == "POST":


       user_id=request.form.get('User_id')
       
       password=request.form.get('Password')
       roomid=request.form.get('Room_id')
       request1=request.form.get('Request')
       rnum=request.form.get('Rnum')
       flag=0
       flag2=0
       cursor.execute("delete from dine_book where Event_date<CURDATE();")
       db.commit()

       cursor.execute("select * from register where User_id=%s and Password=%s;",(str(user_id),str(password)))
       myresult = cursor.fetchall()
       if len(myresult)==1:
            flag=1
       cursor.execute("select * from room_book where roomid={};".format(str(roomid)))

       myresult = cursor.fetchall()
       l=len(myresult)
       if l==1:
        
        flag2=1
       max1=1
       for i in range(0,len(myresult)):
          max1=max(max1,myresult[i][0])
       c=max1+1
       if flag==1 and flag2==1:
            cursor.execute("INSERT INTO services(serviceid,id,service,roomid,User_Id,Password) values(%s,%s,%s,%s,%s,%s);",(c,2,request1,roomid,user_id,password))
            db.commit()
        # db.close()
            return "room booked and your serviceid is "+str(c)
       else:
            return render_template("your room id is not valid or your userid and password is not valid")


       
        # return render_template('dine.html',msg="Sorry! No tables available")

      
         
         # db.close()
            

     


      
       
    return render_template("service.html")
 
if __name__=='__main__':
   app.run(port=7306)


