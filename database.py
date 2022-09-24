import mysql.connector
#import python_database_add_time as timer
#import python_alert_message as alert_message



mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="trojencure",
	database ="test" 
	)	  

#function to create a database
def create_database():
	mycursor=mydb.cursor()
	mycursor.execute("Create database test")

#fubnction to create a table and display everything inside the table
def create_table():
	mycursor=mydb.cursor()

	mycursor.execute("Create table data2(id varchar(20),aadhar varchar(12),name varchar(20),number varchar(20))")
	mycursor.execute("use test")
	mycursor.execute("select * from new")

	myresult=mycursor.fetchall()
	mydb.commit()

	for fetch in myresult:
	    print(fetch)

#create columns in the created table  
def create_column():
	mycursor = mydb.cursor()

	print("enter details of people")
	print("type no to stop entering")
	print("------------------------------------------------------------------")
	sql = "INSERT INTO data(id,aadhar ,name, number) VALUES (%s, %s, %s, %s)"

	change="yes"
	while(change == "yes"):
	    id = input(str("enter id here"))
	    aadhar = input(str("enter aadhar number here"))
	    name=input(str("enter name here"))
	    number=input(str("enter number here"))
	    change=input("want to add more (type yes or no)")
	    print("--------------------------------------------------------------")
	    val=(id,aadhar ,name,number)
	    mycursor.execute(sql, val)
	    mydb.commit()

	print(mycursor.rowcount, "record inserted.")

#add extra columns to out table
def alter_table():
	query = "alter table data add time varchar(20)"
	mycursor.execute(query)

#check for a aadhar card in our database
def aadhar_check(id_user):
	#id_user = input("enter aadhar to check")
	#timenow = timer.timer()

	mycursor = mydb.cursor()

	mycursor.execute("select aadhar from data")

	myresult = mycursor.fetchall()

	check = False
	flag=0
	for x in myresult:
	    for i in x:
	        if str(id_user) == str(i):
	            print("aadhar found in the database")
	            #sql = "update data set time=(%s) where id=(%s)"
	            #val = (str(timenow),str(id_user))
	            #print(val)
	            check = True #to use in the main function 
	            #mycursor.execute(sql,val)
	            #mydb.commit()

	            flag=1
	        else:
	            pass
	#alert_message.send_message(918129769065)
	if flag == 0:
	    print("no id found")
	return check


def aadhar_check_fin(aadhar_id,num): # for authentication with mobile number

	mycursor = mydb.cursor()
	mycursor.execute("select * from data")

	myresult = mycursor.fetchall()
	check = False
	for x in myresult:
		if str(aadhar_id) == str(x[1]) and str(num) == str(x[3]):
			check = True
		else:
			pass
	return check 

#updates the id of the user in datewise tables for future analysis
def update_status(date_var,id_user):
	mycursor=mydb.cursor()
	'''
	query = """alter table test2 add ` %s ` varchar(20)"""
	tuple1 = date_var
	mycursor.execute(query,tuple1) 
	'''


	#query = (f"insert into `{date_var}` values(\"{id_user}\")")

	#mycursor.execute(query)
	mycursor.execute(f"""insert into `{date_var}` values({id_user})""")
	#mycursor.execute("""insert into data1(id) values(23233)""")
	#print(f"insert into `{date_var}` values(\"{id_user}\");")
	mydb.commit()




def main():
	print("")
	#id = "111111111111"
	#print(aadhar_check(id))
	#print("")
	#warmup()
	#create_column()
	#aadhar = aadhar_check()
	#aadhar_check_fin(222222222222,2222222222)

if __name__ == '__main__':
	main()