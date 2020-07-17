from flask import *
import psycopg2
#from flask.images import *

import  os
import csv

app=Flask(__name__)
app.secret_key="Dont Tell"
#images=images(app)


myconn=psycopg2.connect(
	database="Aditya",
	user="postgres",
	password="Jaya@2024")

@app.route("/")
def project():# coursel images
	return render_template("project.html")
@app.route("/home")
def home():# drp down to select clg and display details
	return render_template("index.html")


@app.route("/ace",methods=['GET','POST'])	
def aditya():# data display of clg1
	cur=myconn.cursor()
	cur.execute(""" select * from ace""")
	data=cur.fetchall()
	return render_template("ace.html",results=data)

@app.route("/acet")	
def aditya2():#clg2
	cur=myconn.cursor()
	cur.execute(""" select * from acet""")
	data=cur.fetchall()
	return render_template("acet.html",results=data)

@app.route("/acoe")	
def aditya3():#clg 3
	cur=myconn.cursor()
	cur.execute(""" select * from acoe""")
	data=cur.fetchall()
	return render_template("acoe.html",results=data)

@app.route("/about",methods=['GET','POST'])
def about():#check the login credentials
	if request.method== "POST":
		#results=[]
		uname=request.form['username']
		pwd=request.form['password']
		cur=myconn.cursor()
		cur.execute("""select * from aditya where sid=%s and pwd=%s""",(uname,pwd))
		data=cur.fetchall()
		if data:
			session['loggedin']=True
			flash("Login Sucessfull")
			return render_template("clgdrp.html")  #where it redirects to drp down to select clg
		else:
			flash("Invalid Login")
	return render_template("about.html") #login page

@app.route("/update",methods=['GET','POST'])
def ace1():
	if not session.get('loggedin'):
		return render_template("about.html")
		
	cur=myconn.cursor()
	cur.execute("""select * from ace""")
	data=cur.fetchall()
	#print(data)
	return render_template("update.html",results=data)  # where your data is stored refers to update page edit button page 	

@app.route("/update1",methods=['GET','POST'])
def acet1():
	if not session.get('loggedin'):
		return render_template("about.html") 
	cur=myconn.cursor()
	cur.execute("""select * from acet""")
	data=cur.fetchall()
	return render_template("update1.html",results=data)	   	#same for clg 2
@app.route("/update2",methods=['GET','POST'])
def acoe1():
	if not session.get('loggedin'):
		return render_template("about.html") 
	cur=myconn.cursor()
	cur.execute("""select * from acoe""")
	data=cur.fetchall()
	return render_template("update2.html",results=data)	   	#same for clg3				




@app.route("/change",methods=['GET','POST'])
def change():
	if request.method== "POST":
		#id=request.form['id']
		labno=int(request.form['labno'])
		labname=request.form['labname']
		syscount=int(request.form['syscount'])
		working=int(request.form['working'])
		#notworking=int(request.form['notworking'])
		problem=request.form['problem']
		incharge=request.form['incharge']
		floor=int(request.form['floor'])
		softwares=request.form['softwares']
		mycur=myconn.cursor()
		mycur.execute(""" update ace set labno=%s,labname=%s,syscount=%s,working=%s,problem=%s,
			incharge=%s,floor=%s,softwares=%s where labno=%s""",(labno,labname,syscount,working,problem,incharge,floor,softwares,labno
			))
		#data=mycur.fetchall()
		myconn.commit()
		cu=myconn.cursor()
		cu.execute("""select * from ace""")
		data=cu.fetchall()
		#print(data)
		return render_template("update.html",results=data) # returning into the same data  stored page 
	#return redirect(url_for("edit"))

@app.route("/change1",methods=['GET','POST'])
def change1():
	if request.method== "POST":
		#id=request.form['id']
		labno=int(request.form['labno'])
		labname=request.form['labname']
		syscount=int(request.form['syscount'])
		working=int(request.form['working'])
		#notworking=int(request.form['notworking'])
		problem=request.form['problem']
		incharge=request.form['incharge']
		floor=int(request.form['floor'])
		softwares=request.form['softwares']
		mycur=myconn.cursor()
		mycur.execute(""" update acet set labno=%s,labname=%s,syscount=%s,working=%s,problem=%s,
			incharge=%s,floor=%s,softwares=%s where labno=%s""",(labno,labname,syscount,working,problem,incharge,floor,softwares,labno
			))
		#data=mycur.fetchall()
		myconn.commit()
		cu=myconn.cursor()
		cu.execute("""select * from acet""")
		data=cu.fetchall()
		#print(data)
		return render_template("update1.html",results=data)


@app.route("/change2",methods=['GET','POST'])
def change2():
	if request.method== "POST":
		#id=request.form['id']
		labno=int(request.form['labno'])
		labname=request.form['labname']
		syscount=int(request.form['syscount'])
		working=int(request.form['working'])
		#notworking=int(request.form['notworking'])
		problem=request.form['problem']
		incharge=request.form['incharge']
		floor=int(request.form['floor'])
		softwares=request.form['softwares']
		mycur=myconn.cursor()
		mycur.execute(""" update acoe set labno=%s,labname=%s,syscount=%s,working=%s,problem=%s,
			incharge=%s,floor=%s,softwares=%s where labno=%s""",(labno,labname,syscount,working,problem,incharge,floor,softwares,labno
			))
		#data=mycur.fetchall()
		myconn.commit()
		cu=myconn.cursor()
		cu.execute("""select * from acoe""")
		data=cu.fetchall()
		#print(data)
		return render_template("update2.html",results=data)
			

@app.route("/delete",methods=['GET','POST'])
def delete():#delete
	if request.method== "POST":
		id=request.form['delete']
		cur=myconn.cursor()
		cur.execute("""delete from ace where labno=%s""",(id))
		myconn.commit()
		cu=myconn.cursor()
		cu.execute("""select * from ace""")
		d1=cu.fetchall()
		return render_template("update.html",results=d1)
	#return redirect(url_for('about'))
@app.route("/delete1",methods=['GET','POST'])
def delete1():#delete
	if request.method== "POST":
		id=request.form['delete1']
		cur=myconn.cursor()
		cur.execute("""delete from acet where labno=%s""",(id))
		myconn.commit()
		cu=myconn.cursor()
		cu.execute("""select * from acet""")
		d1=cu.fetchall()
		return render_template("update1.html",results=d1)

@app.route("/delete2",methods=['GET','POST'])
def delete2():#delete
	if request.method== "POST":
		id=request.form['delete2']
		cur=myconn.cursor()
		cur.execute("""delete from acoe where labno=%s""",(id))
		myconn.commit()
		cu=myconn.cursor()
		cu.execute("""select * from acoe""")
		d1=cu.fetchall()
		return render_template("update2.html",results=d1)

@app.route("/edit",methods=['GET','POST'])
def edit():
	if request.method== "POST":
		id=request.form['edit']
		cur=myconn.cursor()
		cur.execute(""" select * from ace where labno=%s""",(id))
		data2=cur.fetchall()
		#print(data2)
		return render_template("edit.html",data=data2)
	# render_template("lab.html")


@app.route("/edit1",methods=['GET','POST'])
def edit1():
	if request.method== "POST":
		id=request.form['edit1']
		cur=myconn.cursor()
		cur.execute(""" select * from acet where labno=%s""",(id))
		data2=cur.fetchall()
		#print(data2)
		return render_template("edit1.html",data=data2) #form page it will redirect


@app.route("/edit2",methods=['GET','POST'])
def edit2():
	if request.method== "POST":
		id=request.form['edit2']
		cur=myconn.cursor()
		cur.execute(""" select * from acoe where labno=%s""",(id))
		data2=cur.fetchall()
		#print(data2)
		return render_template("edit2.html",data=data2)

@app.route("/logout")
def logout():
	session['loggedin']=False
	return render_template("project.html")


if __name__=="__main__":
	app.run(debug=True)