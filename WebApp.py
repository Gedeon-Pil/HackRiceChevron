import streamlit as st
from twilio.rest import Client
from order_management import *

def runSide():
    
    
    st.sidebar.markdown("<h3 style='text-align:center; color:blue;'>Schedule</h3>",unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center; color:blue;'>Work Oder Tracking System for Managers and Employees</h1>",unsafe_allow_html=True)
    Worker_name=st.sidebar.text_area('Enter name of Worker: ')
    

    st.write('Name of Worker is:'+Worker_name)

    #Time= Python Script
    st.write('Time')

    #Start_Time= PythonScript
    st.write('Start_Time')

    #To send SMS Python Script
    text= message()
    st.write(text)
    

def message(order_id, facility, start_time_hours, start_time_minutes, end_time_hours, end_time_minutes):
    account_sid = 'AC705f999c86a965d4f4a8db2f4f7fea8b'
    auth_token = '8756cbaaba1036256d0679cbc751d300'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body='Proceed to '+ facility + " to complete work order " + str(order_id) + " from "+ str(start_time_hours)+ ":" + str(start_time_minutes) + " to " + str(end_time_hours) + ":" + str(end_time_hours)+".",
            from_='+17163174817',
            to='+17158282001'
     )

    return(message.sid)
    
    
def main():
    framework = Delegate_Tasks()
    framework.generate_schedule()
    master_scheduler = framework.get_all_schedules()
    runSide()
    
