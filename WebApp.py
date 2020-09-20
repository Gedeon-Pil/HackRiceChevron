import streamlit as st
from twilio.rest import Client

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
    

def message():
    account_sid = 'AC705f999c86a965d4f4a8db2f4f7fea8b'
    auth_token = '8756cbaaba1036256d0679cbc751d300'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body='Put the message here',
            from_='+17163174817',
            to='+17158282001'
     )

    return(message.sid)
    
    
runSide()
