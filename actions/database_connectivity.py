import mysql.connector
def DataUpdate(FirstName,LastName,Feedback): 
    mydb = mysql.connector.connect( host="localhost", user="root",  
    passwd="root", database="Rasa_feedback") 
    mycursor = mydb.cursor() 
    sql='INSERT INTO FeedBack_rasa_date (firstName, lastName, feedback) VALUES ("{0}","{1}", "{2}");'.format(FirstName,LastName,Feedback) 
    mycursor.execute(sql) 
    mydb.commit()