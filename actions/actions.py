# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List

from rasa_sdk.events import EventType
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction

import mysql.connector
import datetime
import numpy as np

class ActionHelloWorld(Action):
    
    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #msg={webbrowser.open ("C:\\Users\\kd\\Desktop\\test.html")}
        
        dispatcher.utter_message("Hello my name is kshitij")

        return []



class ActionCreateDatabase(Action):
    
    def name(self) -> Text:
        return "action_create_database"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")

        mycursor = mydb.cursor()
        dispatcher.utter_message("Enter your Secret Key: ")
        #s_k = input("Enter your Secret Key: ")

        s_k = next(tracker.get_latest_entity_values("id"),None)
        
        sql = f"select a.emp_id,a.emp_name,a.emp_mail,a.CL,a.PL from emp_info as a, emp_secret as b where b.secret_key='{s_k}' and a.emp_id=b.emp_id"
        
        mycursor.execute(sql)
        
        myresult = mycursor.fetchall()


        print(mycursor.rowcount,"RECORD")
        

        
        dispatcher.utter_message('\nCheck Your Information\n')
        #for x in myresult:
        #    dispatcher.utter_message(f"Employee id = {x[0]} \nEmployee Name = {x[1]} \nEmployee Email = {x[2]} \nAvailable CL = {x[3]} \nAvailable PL = {x[4]}\n")
        
        id = f"select a.emp_id from emp_info as a, emp_secret as b where b.secret_key='{s_k}' and a.emp_id=b.emp_id"
        mycursor.execute(id)
        empid = mycursor.fetchall()
        for y in empid:
            emp_id=y[0]
        
        print(emp_id)
        dispatcher.utter_message("Enter the type of leave = ")
        type_leave = input(next(tracker.get_latest_entity_values("id"),None))
        print(type_leave)
        dispatcher.utter_message("Hello my name is kshitij")

        return []



class ActionSecretKey(Action):
    
    def name(self) -> Text:
        return "action_secret_key"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")
        
        mycursor = mydb.cursor()
        global s_k
        
        s_k = next(tracker.get_latest_entity_values("sk"),None)

        sql = f"select a.emp_id,a.emp_name,a.emp_mail,a.CL,a.PL from emp_info as a, emp_secret as b where b.secret_key='{s_k}' and a.emp_id=b.emp_id"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        print(mycursor.rowcount,"RECORD")
        
        global y

        id = f"select a.emp_id from emp_info as a, emp_secret as b where b.secret_key='{s_k}' and a.emp_id=b.emp_id"
        mycursor.execute(id)
        empid = mycursor.fetchall()
        global emp_id
        for y in empid:
            emp_id=y[0]
        print(emp_id)

        dispatcher.utter_message('\nCheck Your Information\n')
        for x in myresult:
            y = x
            print(f"Hello {y}")
            dispatcher.utter_message(f"Employee id = {x[0]} \nEmployee Name = {x[1]} \nEmployee Email = {x[2]} \nAvailable CL = {x[3]} \nAvailable PL = {x[4]}\n")
        
        return []
    
class ActionLeaveType(Action):
    
    def name(self) -> Text:
        return "action_leave_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")
        mycursor = mydb.cursor()
        

        sql = f"select a.emp_id,a.emp_name,a.emp_mail,a.CL,a.PL from emp_info as a, emp_secret as b where b.secret_key='{s_k}' and a.emp_id=b.emp_id"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()
        
        for x in myresult:
            print(x)

        id = f"select a.emp_id from emp_info as a, emp_secret as b where b.secret_key='{s_k}' and a.emp_id=b.emp_id"
        mycursor.execute(id)
        empid = mycursor.fetchall()
        global emp_id
        for y in empid:
            emp_id=y[0]
        print(emp_id)
        global type_leave
        type_leave = next(tracker.get_latest_entity_values("l_type"),None)
        msg = f"Your selected Leave type is {type_leave}"
        dispatcher.utter_message(msg)

        return[]

class ActionStartDate(Action):
    
    def name(self) -> Text:
        return "action_start_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")
        mycursor = mydb.cursor()
        

        sql = f"select a.emp_id,a.emp_name,a.emp_mail,a.CL,a.PL from emp_info as a, emp_secret as b where b.secret_key='{s_k}' and a.emp_id=b.emp_id"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()
        
        for x in myresult:
            print(x)

        id = f"select a.emp_id from emp_info as a, emp_secret as b where b.secret_key='{s_k}' and a.emp_id=b.emp_id"
        mycursor.execute(id)
        empid = mycursor.fetchall()
        for y in empid:
            emp_id=y[0]
        print(emp_id)
        global start_date
        global sd 
        global start_dt
        start_date = next(tracker.get_latest_entity_values("st_dt"),None).split("/")
        print(start_date)
        s_year, s_month, s_day = [int(item) for item in start_date]
        sd = str(datetime.date(s_day,s_month,s_year))
        start_dt = str(sd)
        msg = f"Your Start Date is {start_date}"
        #insert_into_leave_info = f"""INSERT INTO leave_info(emp_id,start_date) VALUES({emp_id},'{start_dt}')"""
        #mycursor.execute(insert_into_leave_info)

        #mydb.commit()
        dispatcher.utter_message(msg)

        return[]
    
class ActionEndDate(Action):
    
    def name(self) -> Text:
        return "action_end_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")
        mycursor = mydb.cursor()
        

        sql = f"select a.emp_id,a.emp_name,a.emp_mail,a.CL,a.PL from emp_info as a, emp_secret as b where b.secret_key='{s_k}' and a.emp_id=b.emp_id"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()
        
        for x in myresult:
            print(x)

        id = f"select a.emp_id from emp_info as a, emp_secret as b where b.secret_key='{s_k}' and a.emp_id=b.emp_id"
        mycursor.execute(id)
        empid = mycursor.fetchall()
        for y in empid:
            emp_id=y[0]
        print(emp_id)
        global end_date
        global ed
        global end_dt
        end_date = next(tracker.get_latest_entity_values("ed_dt"),None).split("-")
        print(end_date)
        e_year, e_month, e_day = [int(item) for item in end_date]
        ed = datetime.date(e_day,e_month,e_year)
        end_dt = str(ed)
        msg = f"Your End Date is {end_date}"
        #insert_into_leave_info = f"""update leave_info set end_date='{end_dt}' where emp_id = {emp_id};"""
        #mycursor.execute(insert_into_leave_info)

        #mydb.commit()
        dispatcher.utter_message(msg)

        return[]

    
class ActionReasonType(Action):
    
    def name(self) -> Text:
        return "action_reason_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")

        mycursor = mydb.cursor()
        
        s_k = next(tracker.get_latest_entity_values("sk"),None)

        sql = f"select a.emp_id,a.emp_name,a.emp_mail,a.CL,a.PL from emp_info as a, emp_secret as b where b.secret_key='{s_k}' and a.emp_id=b.emp_id"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        global x
        for x in myresult:
            print(x)
        
        

        #id = f"select a.emp_id from emp_info as a, emp_secret as b where b.secret_key='{s_k}' and a.emp_id=b.emp_id"
        #mycursor.execute(id)
        #empid = mycursor.fetchall()
        #for y in empid:
        #    emp_id=y[0]
        #print(emp_id)
        #type_leave = next(tracker.get_latest_entity_values("l_type"),None)
        #start_date = tracker.get_latest_entity_values("st_dt")
        #dispatcher.utter_message(emp_id)
        #insert_into_leave_info = f"""INSERT INTO leave_info(emp_id,start_date) VALUES({emp_id},'{start_date}')"""
        #mycursor.execute(insert_into_leave_info)

        #mydb.commit()
        #x = start_date
        #end_date = tracker.get_latest_entity_values("ed_dt")
        reason = next(tracker.get_latest_entity_values("reason"),None)
        print(reason)

        '''start_date = next(tracker.get_slot("st_dt"),None).split(" ")
        end_date = next(tracker.get_slot("ed_dt"),None).split(" ")
        reason = next(tracker.get_slot("reason"),None)'''

        #dispatcher.utter_message(start_date)
        #dispatcher.utter_message(end_date)
        #dispatcher.utter_message(reason)

        #s_year, s_month, s_day = [int(item) for item in start_date]
        #e_year, e_month, e_day = [int(item) for item in end_date]

        #start_dt = str(datetime.date(s_day,s_month,s_year))
        #end_dt = str(datetime.date(e_day,e_month,e_year))
        current_time = str(datetime.datetime.now())

        no_of_days = np.busday_count(sd,ed,weekmask='1111110')
        no_of_days = no_of_days + 1
        print(no_of_days)

        #dispatcher.utter_message(f"Start date : {start_dt} \nEnd date : {end_dt} \nReason for Leave: {reason} \nPlease Check.")

        insert_into_leave_info = f"""INSERT INTO leave_info(emp_id,start_date,end_date,reason_for_leave,leave_apply_date,total_days_of_leave) VALUES({emp_id},'{start_dt}','{end_dt}','{reason}','{current_time}',{no_of_days})"""

        mycursor.execute(insert_into_leave_info)

        mydb.commit()

        
        if type_leave=='cl':
            cl = y[3]
            cl = cl - no_of_days

            cl_qury = f"UPDATE emp_info SET CL={cl} WHERE emp_id={emp_id};"
            mycursor.execute(cl_qury)
            mydb.commit()

        elif type_leave=='pl':
            pl = y[4]
            pl = pl - no_of_days

            pl_qury = f"UPDATE emp_info SET PL={pl} WHERE emp_id={emp_id};"
            mycursor.execute(pl_qury)
            mydb.commit()
        
        return []


class ActionDate(Action):
    
    def name(self) -> Text:
        return "action_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")
        
        

        #print(emp_id)
        global date
        global dt_of_eg
        global dt
        date = next(tracker.get_latest_entity_values("date"),None).split(" ")
        print(date)
        year, month, day = [int(item) for item in date]
        
        dt = str(datetime.date(day,month,year))
        #dt = str(dt_of_eg)
        msg = f"Your selected Date is {dt}"
        #insert_into_leave_info = f"""INSERT INTO leave_info(emp_id,start_date) VALUES({emp_id},'{start_dt}')"""
        #mycursor.execute(insert_into_leave_info)

        #mydb.commit()
        dispatcher.utter_message(msg)

        return[]


class ActionStartTime(Action):
    
    def name(self) -> Text:
        return "action_start_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")
        
        

        #print(emp_id)
        global start_time
        start_time = next(tracker.get_latest_entity_values("st_time"),None)
        print(start_time)
        msg = f"Your start time is {start_time}"
        #insert_into_leave_info = f"""INSERT INTO leave_info(emp_id,start_date) VALUES({emp_id},'{start_dt}')"""
        #mycursor.execute(insert_into_leave_info)

        #mydb.commit()
        dispatcher.utter_message(msg)

        return[]

class ActionEndTime(Action):
    
    def name(self) -> Text:
        return "action_end_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")
        
        

        #print(emp_id)
        global end_time
        global t
        end_time = next(tracker.get_latest_entity_values("ed_time"),None).split("-")
        t = end_time[0]+':'+end_time[1]
        print(end_time)
        msg = f"Your start time is {t}"
        #insert_into_leave_info = f"""INSERT INTO leave_info(emp_id,start_date) VALUES({emp_id},'{start_dt}')"""
        #mycursor.execute(insert_into_leave_info)

        #mydb.commit()
        dispatcher.utter_message(msg)

        return[]
    
class ActionLocation(Action):
    
    def name(self) -> Text:
        return "action_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")
        
        

        #print(emp_id)
        global location 
        location = next(tracker.get_latest_entity_values("location"),None)
        print(location)

        return[]
    
class ActionReason(Action):
    
    def name(self) -> Text:
        return "action_reason"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")
        
        

        print(emp_id)
        global reason_123
        reason_123 = next(tracker.get_latest_entity_values("reason"),None)
        print(reason_123)

        return[]
    
class ActionEarlyGoing(Action):
    
    def name(self) -> Text:
        return "action_early_going"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")
        mycursor = mydb.cursor()
        
        
        qurey = f"""insert into early_going_info(em_id,date_eg,start_time_eg,end_time_eg,location_eg,reason_eg) values({emp_id},'{dt}','{start_time}','{t}','{location}','{reason_123}')"""
        mycursor.execute(qurey)
        mydb.commit()
        


        return[]
    

class ActionLateComing(Action):
    
    def name(self) -> Text:
        return "action_late_coming"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")
        mycursor = mydb.cursor()
        
        
        qurey = f"""insert into late_coming_info(emp_id,date_lc,start_time_lc,end_time_lc,location,reason_lc) values({emp_id},'{dt}','{start_time}','{t}','{location}','{reason_123}');"""
        mycursor.execute(qurey)
        mydb.commit()
    

        return[]
    
class ActionODTour(Action):
    
    def name(self) -> Text:
        return "action_od_tour"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")
        mycursor = mydb.cursor()
        
        
        qurey = f"""insert into od_tour_info(emp_id,start_date_od,end_date_od,start_time_od,end_time_od,location_od,reason) values({emp_id},'{start_dt}','{end_dt}','{start_time}','{t}','{location}','{reason_123}');"""
        mycursor.execute(qurey)
        mydb.commit()
        


        return[]
    
class ActionODOnly(Action):
    
    def name(self) -> Text:
        return "action_od_only"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="new")
        mycursor = mydb.cursor()
        
        
        qurey = f"""insert into od_only_info(emp_id,date_od,start_time_od_only,end_time_od_only,location_od_only,reason_od_only) values({emp_id},'{dt}','{start_time}','{t}','{location}','{reason_123}');"""
        mycursor.execute(qurey)
        mydb.commit()
        


        return[]
    