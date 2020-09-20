import streamlit as st
from twilio.rest import Client
from order_management import *
import time

def convert_time(hour, minutes):

    minutes = str(int(minutes))

    if len(minutes) == 1:
        minutes = "0" + minutes

    hour = int(hour)
    if hour < 12:
        tod = "AM"
    else:
        hour %= 12
        tod = "PM"

    return str(hour) + ":" + minutes + tod



def create_webpage():

   st.sidebar.markdown("<h3 style='text-align:center; color:blue;'>Schedule</h3>",unsafe_allow_html=True)

   st.markdown("<h1 style='text-align:center; color:blue;'>Work Order Tracking System for Managers and Employees</h1>",unsafe_allow_html=True)


def message(name, order_id, facility, start_time_hours, start_time_minutes, end_time_hours, end_time_minutes):
    account_sid = 'AC705f999c86a965d4f4a8db2f4f7fea8b'
    auth_token = '8756cbaaba1036256d0679cbc751d300'
    client = Client(account_sid, auth_token)
    full_message = "Hi, " + name + "! "+ "Please proceed to Facility " + facility[-1] + " to complete work order " + str(order_id) + " from " + convert_time(start_time_hours, start_time_minutes) + " to " + convert_time(end_time_hours, end_time_minutes) + "."

    message = client.messages \
        .create(
            body= full_message,
            from_='+17163174817',
            to='+15086850814'
     )

    return(message.sid)


def display_message(master_scheduler):

    for val in master_scheduler.values():
        length = len(val)
        break

    for day in range(length):
        for name, schedules in master_scheduler.items():
            schedule = schedules[day]
            for order in schedule:
                order_id = order[0]
                facility = order[1]
                start_time_hours = order[2]
                start_time_minutes = order[3]
                end_time_hours = order[4]
                end_time_minutes =order[5]
                message(name, order_id, facility, start_time_hours, start_time_minutes, end_time_hours, end_time_minutes)
                time.sleep(1.5)
        time.sleep(10)


def display_webpage(master_scheduler):

    create_webpage()

    for val in master_scheduler.values():
        length = len(val)
        break

    for day in range(length):
        st.write('\nDay %d\n' % day + 1)
        for name, schedules in master_scheduler.items():
            st.write("\nWorker Name: %s\n" % name)
            schedule = schedules[day]
            for order in schedule:
                st.write()
                order_id = order[0]
                facility = order[1]
                start_time_hours = order[2]
                start_time_minutes = order[3]
                end_time_hours = order[4]
                end_time_minutes = order[5]
                msg = "Order " + str(order_id) + " at facility" + str(facility[-1]) + " -- "
                duration = convert_time(start_time_hours, start_time_minutes) + " to " + convert_time(end_time_hours, end_time_minutes)
                st.write(time + duration)



def main():
    framework = Delegate_Tasks()
    framework.generate_schedule()
    master_scheduler = framework.get_all_schedules()

    # display_message(master_scheduler)

    display_webpage(master_scheduler)


if __name__ == '__main__':
    main()
