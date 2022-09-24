import mysql.connector
#import python_database_add_time as timer
#import python_alert_message as alert_message
import datetime



mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="trojencure",
	database ="test" 
	)	  


def  fetch_details(id):
	mycursor = mydb.cursor()
	mycursor.execute(f"""select * from data""")
	myresult = mycursor.fetchall()

	for x in myresult:
		if x[1] == id:
			return (x[2],x[3])
			
		

def call_id():
	date_now = datetime.date.today()
	datenow = str(date_now)

	mycursor = mydb.cursor()

	mycursor.execute(f"""select id from `{datenow}`""")

	myresult = mycursor.fetchall()	

	for x in myresult:
		for i in x:
			res = fetch_details(i)
			print(f"{res[0]}  :  {res[1]}")

def main():
	call_id()

if __name__ == '__main__':
	main()