import tkinter as tk
import timecard_helper as th
import datetime


def switch_time_left():
    """
    Switch to the Time Left screen.
    """
    time_left_frame.pack()
    time_left(time_left_frame)
    menu_frame.forget()


def switch_convert():
    """
    Switch to the Convert screen
    """
    convert_frame.pack()
    converter(convert_frame)
    menu_frame.forget()


def switch_scheduler():
    """
    Switch to the Scheduler screen
    """
    scheduler_frame.pack()
    scheduler(scheduler_frame)
    menu_frame.forget()


def switch_time_difference():
    """
    Switch to the Time Difference screen
    """
    time_difference_frame.pack(fill='x')
    time_difference(time_difference_frame)
    menu_frame.forget()


def switch_sr():
    """
    Switch to the Scheduler screen for Thursday.
    """
    sr_frame.pack()
    sr(sr_frame)
    scheduler_frame.forget()


def switch_sf():
    """
    Switch for the Scheduler screen for Friday.
    """
    sf_frame.pack()
    sf(sf_frame)
    scheduler_frame.forget()


def time_left(frame):
    """
    Calculates the time left to work, given how many hours have been already worked.
    Assumes 40 hours a week.
    """
    txt = tk.Message(frame, text="Calculate time left to work", width=300)
    total_hours = 40.00

    def enter_click():
        this_week = float(hours.get())
        remaining = total_hours - this_week
        string = "Hours left to work: " + str(remaining)
        msg = tk.Message(frame, text=string, width=300)
        msg.pack()

    hours = tk.StringVar()
    textbox = tk.Entry(frame, textvariable=hours)
    ent = tk.Button(frame, text="Enter", command=enter_click)

    txt.pack(side=tk.TOP)
    textbox.pack()
    ent.pack()


def converter(frame):
    """
    The screen for converting minutes from a decimal.
    """
    txt = tk.Message(frame, text="Calculate minutes from decimal", width=300)

    def enter_click():
        time = float(entry.get())
        converted = th.convert_helper(time, 1)
        string = "This is equivalent to " + str(converted)
        msg = tk.Message(frame, text=string, width=300)
        msg.pack()

    entry = tk.StringVar()
    textbox = tk.Entry(frame, textvariable=entry)
    ent = tk.Button(frame, text="Enter", command=enter_click)

    txt.pack(side=tk.TOP)
    textbox.pack()
    ent.pack()


def scheduler(frame):
    """
    The starting screen for the Scheduler.
    """
    txt1 = tk.Message(frame, text="Schedule the rest of the week", width=300)
    txt2 = tk.Message(frame, text="Which day would you like to schedule?", width=300)

    r_button = tk.Button(frame, text="Thursday", command=switch_sr)
    f_button = tk.Button(frame, text="Friday", command=switch_sf)

    txt1.pack(side=tk.TOP)
    txt2.pack(side=tk.TOP)
    r_button.pack(side=tk.LEFT)
    f_button.pack(side=tk.RIGHT)


def sr(frame):
    """
    The scheduling screen for Thursday.
    """
    txt1 = tk.Message(frame, text="How many hours have you worked so far?", width=300)
    txt2 = tk.Message(frame, text="What time did you check in? (HH:MM) ", width=300)
    txt3 = tk.Message(frame, text="What time do you have to start on Friday? (HH:MM) ", width=300)
    var1 = tk.StringVar()
    var2 = tk.StringVar()
    var3 = tk.StringVar()

    def enter_click():
        sum = float(var1.get())
        checkin = var2.get()
        fri_start = var3.get()
        sum_format = th.convert_helper(sum, 2).split(":")
        sum_hours, sum_minutes = int(sum_format[0]), int(sum_format[1])
        fri_time = th.difference_helper(fri_start, "15:00") - datetime.timedelta(minutes=30)
        tot = datetime.timedelta(hours=sum_hours, minutes=sum_minutes) + fri_time
        left = datetime.timedelta(hours=40) - tot
        if int(checkin.split(":")[0]) < 11:
            left += datetime.timedelta(minutes=30)
        in_format = checkin.split(":")
        in_hours, in_minutes = int(in_format[0]), int(in_format[1])
        checkout = datetime.datetime(2022, 1, 1, in_hours, in_minutes) + left
        string = "Check out today at {:d}:{:02d}".format(checkout.hour, checkout.minute)
        msg = tk.Message(frame, text=string, width=300)
        msg.pack()

    textbox1 = tk.Entry(frame, textvariable=var1)
    textbox2 = tk.Entry(frame, textvariable=var2)
    textbox3 = tk.Entry(frame, textvariable=var3)
    ent = tk.Button(frame, text="Enter", command=enter_click)

    txt1.pack()
    textbox1.pack()
    txt2.pack()
    textbox2.pack()
    txt3.pack()
    textbox3.pack()
    ent.pack()


def sf(frame):
    """
    The scheduler screen for Friday.
    """
    txt1 = tk.Message(frame, text="How many hours have you worked so far?", width=300)
    txt2 = tk.Message(frame, text="What time did you check in? (HH:MM) ", width=300)
    txt3 = tk.Message(frame, text="What time do you want to check out today? (HH:MM) ", width=300)
    var1 = tk.StringVar()
    var2 = tk.StringVar()
    var3 = tk.StringVar()

    def enter_click():
        sum = float(var1.get())
        checkin = var2.get()
        checkout = var3.get()
        sum_format = th.convert_helper(sum, 2).split(":")
        sum_hours, sum_minutes = int(sum_format[0]), int(sum_format[1])
        today_hours = th.difference_helper(checkin, checkout)
        if int(checkin.split(":")[0]) < 11:
            # We have not eaten lunch yet, that will happen before our end time
            today_hours -= datetime.timedelta(minutes=30)
        tot = today_hours + datetime.timedelta(hours=sum_hours, minutes=sum_minutes)
        left = datetime.timedelta(hours=40) - tot + datetime.timedelta(minutes=30)
        fri_start = datetime.datetime(2022, 1, 1, 15, 0) - left
        string = "Start on Friday at {:d}:{:02d}".format(fri_start.hour, fri_start.minute)
        msg = tk.Message(frame, text=string)
        msg.pack()

    textbox1 = tk.Entry(frame, textvariable=var1)
    textbox2 = tk.Entry(frame, textvariable=var2)
    textbox3 = tk.Entry(frame, textvariable=var3)
    ent = tk.Button(frame, text="Enter", command=enter_click)

    txt1.pack()
    textbox1.pack()
    txt2.pack()
    textbox2.pack()
    txt3.pack()
    textbox3.pack()
    ent.pack()


def time_difference(frame):
    """
    The screen for finding the difference between two times.
    """
    txt = tk.Message(frame, text="Find the difference between two times", width=300)

    def enter_click():
        time1 = var1.get()
        time2 = var2.get()
        diff = th.difference_helper(time1, time2)
        string = "The difference in these times is " + str(diff)
        msg = tk.Message(frame, text=string, width=300)
        msg.pack()

    var1 = tk.StringVar()
    var2 = tk.StringVar()
    textbox1 = tk.Entry(frame, textvariable=var1)
    textbox2 = tk.Entry(frame, textvariable=var2)
    ent = tk.Button(frame, text="Enter", command=enter_click)

    txt.pack(fill='x')
    textbox1.pack()
    textbox2.pack()
    ent.pack()


def make_menu(menu_frame):
    """
    The menu screen.
    """
    txt = tk.Message(menu_frame, text="Select an option:", width=300, font="courier")
    one = tk.Button(menu_frame, text="(1) How much time left?        ", width=35, font="courier", command=switch_time_left)
    two = tk.Button(menu_frame, text="(2) Scheduler                  ", width=35, font="courier", command=switch_scheduler)
    thr = tk.Button(menu_frame, text="(3) Decimal to minute converter", width=35, font="courier", command=switch_convert)
    fou = tk.Button(menu_frame, text="(4) Time difference            ", width=35, font="courier", command=switch_time_difference)

    txt.pack(fill='x')
    one.pack(side=tk.TOP)
    two.pack(side=tk.TOP)
    thr.pack(side=tk.TOP)
    fou.pack(side=tk.TOP)


# Set up the window
win = tk.Tk()
win.title("Timecard Helper")
win.geometry("700x500")

# Create all the frames used throughout the application
menu_frame = tk.Frame(win)
time_left_frame = tk.Frame(win)
convert_frame = tk.Frame(win)
time_difference_frame = tk.Frame(win)
scheduler_frame = tk.Frame(win)
sr_frame = tk.Frame(win)
sf_frame = tk.Frame(win)


menu_frame.pack(fill='x')
make_menu(menu_frame)

win.mainloop()

