from tkinter import Tk, Canvas #import canvas from tkinter
from datetime import datetime

# def update_clock():
#    now = datetime.now()
#    current_time = now.strftime('%H:%M:%S')
#    current_date = now.strftime('%d/%m/%Y')
#    c.itemconfig(clock_text, text=f"Date: {current_date}\nTime: {current_time}")
#    root.after(1000, update_clock)  #1000ms = 1 second

def get_events():
   list_events = []
   with open('m11_events.txt') as file: #get txt file 
       for line in file:
           line = line.rstrip('\n')
           current_event = line.split(',')
           event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
           current_event[1] = event_date
           list_events.append(current_event)
   print(list_events)
   return list_events

# def days_between_dates(date1, date2): #to find out the number of days between the current date and the dates in the loaded
#     time_between = date1 - date2
# #    number_of_days = time_between.split(' ')
# #    return number_of_days[0]
#     number_of_days = time_between.days
#     return number_of_days


# root = Tk()
# c = Canvas(root, width=800, height=500, bg='green') #create canvas
# c.pack()
# c.create_text(100, 50, anchor='w', fill='orange', font='Arial 28 bold underline', text='My Countdown Calendar')


# events = get_events() #call function get_events
# today = datetime.now().date() # to find out the current date information
# vertical_space = 100
# events.sort(key=lambda x: x[1])
# # print(today)

# for event in events:
#    event_name = event[0]
#    days_until = days_between_dates(event[1], today)
#    display = f"It is {days_until} days until {event_name}"
#    #if int(days_until) <= 7:
#    if days_until <= 7:
#         text_col = 'red'
#    else:
#         text_col = 'lightblue'
#    c.create_text(100, vertical_space, anchor='w', fill=text_col, font='Arial 28 bold', text=display)
#    vertical_space += 30

# clock_text = c.create_text(750, 400, anchor='e', fill='white', font='Arial 18 bold')
# update_clock()  # Start the live clock update


# root.mainloop()

c.create_text(100, 50, anchor='w', fill='orange', font='Arial 28 bold underline', text='My Countdown Calendar')
# add code below
events = get_events()
# add code above
root.mainloop()