#import streamlit as st
from twilio.rest import Client
from order_management import *
import time

#def runSide():


#    st.sidebar.markdown("<h3 style='text-align:center; color:blue;'>Schedule</h3>",unsafe_allow_html=True)

#    st.markdown("<h1 style='text-align:center; color:blue;'>Work Oder Tracking System for Managers and Employees</h1>",unsafe_allow_html=True)
#    Worker_name=st.sidebar.text_area('Enter name of Worker: ')


#    st.write('Name of Worker is:'+Worker_name)

    #Time= Python Script
#    st.write('Time')

    #Start_Time= PythonScript
#    st.write('Start_Time')

    #To send SMS Python Script
#    text= message()
#    st.write(text)


def message(name, order_id, facility, start_time_hours, start_time_minutes, end_time_hours, end_time_minutes):
    account_sid = 'AC705f999c86a965d4f4a8db2f4f7fea8b'
    auth_token = '8756cbaaba1036256d0679cbc751d300'
    client = Client(account_sid, auth_token)
    full_message = "Hi, " + name+ "!"+ "Proceed to"+ facility + " to complete work order " + str(order_id) + " from "+ str(start_time_hours)+ ":" + str(start_time_minutes) + " to " + str(end_time_hours) + ":" + str(end_time_hours) + "."

    message = client.messages \
        .create(
            body= full_message,
            from_='+17163174817',
            to='+17158282001'
     )

    return(message.sid)


def main():
    framework = Delegate_Tasks()
    framework.generate_schedule()
    master_scheduler = framework.get_all_schedules()
    length = len(master_scheduler.values()[0])
    for day in range(length):
        for name, schedules in master_scheduler.items():
            schedule = schedules[day]
            for order in schedule:
                order_id = order[0]
                facility = order[1]
                start_time_hours = order[2]
                start_time_minutes = order[3]
                end_times_hours = order[4]
                end_time_minutes =order[5]
                message(name, order_id, facility, start_time_hours, start_time_minutes, end_time_hours, end_time_minutes)
                time.sleep(2)
        time.sleep(10)

if __name__ == '__main__':
    main()








    # runSide()
