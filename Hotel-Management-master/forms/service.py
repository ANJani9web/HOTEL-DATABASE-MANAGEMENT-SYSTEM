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


       service=request.form.get('Service')
       roomid=request.form.get('roomid')
       serviceneeded=request.form.get('serviceneeded')
       roomnumber=request.form.get('roomnumber')
       
       
     #   flag=0
     #   flag2=0
     #   cursor.execute("delete from dine_book where Event_date<CURDATE();")
     #   db.commit()

       cursor.execute("select * from rooms where roomid=%s and roomnumber=%s;",(str(roomid),str(roomnumber)))
       myresult = cursor.fetchall()
       if len(myresult)==1:
            flag=1
     
       max1=1
       for i in range(0,len(myresult)):
          max1=max(max1,myresult[i][0])
       c=max1+1
       if flag==1:
            cursor.execute("INSERT INTO services(serviceid,id,service,servicedetail,roomid) values(%s,%s,%s,%s,%s);",(c,2,service,serviceneeded,roomid))
            db.commit()
        # db.close()
            return "service booked and your serviceid is "+str(c)
       else:
            return render_template("your room id is not valid or your roomnumber is not valid")


       
        # return render_template('dine.html',msg="Sorry! No tables available")

      
         
         # db.close()
            

     


      
       
    return render_template("service.html")
 
if __name__=='__main__':
   app.run(port=7306)


