"""
Timecard Helper

Author: Kyri Lea

Helps do time math and work week scheduling.
"""
import datetime


def time_left():
    """
    Calculates how many hours you have left to work given how many
    you have worked so far.
    Allows you to set how many hours you work in a week, defaulting to 40.
    Prints out total remaining hours in two formats.
    """
    print("Calculate time left to work")
    print()
    total_hours = 40.00
    change_hours = input("Weekly requirement (Press enter for 40): ")
    if change_hours != "":
        total_hours = float(change_hours)
    this_week = float(input("How many hours have you worked this week?    "))
    remaining = total_hours - this_week
    print("You need to work ", round(remaining, 2), " more hours, or ", convert_helper(remaining, 1))
    cont = input("Press enter to continue.")


def convert_helper(time, form):
    """
    Converts a number of hours as a decimal into a written out form or a HH:MM form
    :param time: Number of hours as a decimal
    :param form: Formatting choice, 1 for long format, 2 for clock format
    :return: Time as a formatted string
    """
    hours = int(time)
    minutes = (time * 60) % 60
    formatted = ""
    if form == 1:
        formatted = str(hours) + " hours and " + str(int(minutes)) + " minutes"
    if form == 2:
        formatted = str(hours) + ":" + str(int(minutes))
    return formatted


def converter():
    """
    Gets user input to convert a time from a decimal to hours and minutes.
    Prints out the equivalent time in an easy-to-read format.
    """
    print("Calculate minutes from decimal")
    print()
    time = float(input("Enter time in decimal format: "))
    print()
    converted = convert_helper(time, 1)
    print("This is equivalent to ", converted)
    cont = input("Press enter to continue.")


def difference_helper(time1, time2):
    """
    Calculates the difference between two times.
    Time math has to be done with a full datetime object, so for the sake of this
    program, it is fine to use 1-1-22 as the date on all of them, the date is
    never used.
    :param time1: The first time as a HH:MM formatted string
    :param time2: The second time as a HH:MM formatted string
    :return: a timedelta object with the difference between the two times
    """
    t1 = time1.split(":")
    t2 = time2.split(":")
    h1, m1 = int(t1[0]), int(t1[1])
    h2, m2 = int(t2[0]), int(t2[1])
    start = datetime.datetime(2022, 1, 1, h1, m1)
    end = datetime.datetime(2022, 1, 1, h2, m2)
    diff = end - start
    return diff


def time_difference():
    """
    Takes user input tofind the difference between two times.
    Prints out the difference in the times.
    """
    print("Find the difference between two times")
    print()
    time1 = input("Enter start time (HH:MM): ")
    time2 = input("Enter end time (HH:MM): ")
    diff = difference_helper(time1, time2)
    print("The difference in these times is ", diff)
    cont = input("Press enter to continue.")


def scheduler():
    """
    Helps schedule the rest of the week, to be used on Thursday.
    Assumes that a work week is 40 hours.
    Assumes that you want to leave at 15:00 on Friday.
    Assumes that you will not check back in for lunch before 11 and that you will eat lunch every day.
    Assumes a 30 minute lunch.

    Can either tell you when to check out on Thursday given hours that you have to work
    on Friday, or when to check in on Friday given hours that you will work on Thursday.
    Prints out the time you should either start or leave.
    """
    print("Help schedule the rest of the week")
    print()
    day = input("What day do you want to schedule? (R or F): ")
    if day == "R" or day == "r":
        # Calculate Thursday end
        sum = float(input("How many hours have you worked so far? "))
        sum_format = convert_helper(sum, 2).split(":")
        sum_hours, sum_minutes = int(sum_format[0]), int(sum_format[1])
        checkin = input("What time did you check in? (HH:MM) ")
        fri_start = input("What time do you have to start on Friday? (HH:MM) ")
        fri_time = difference_helper(fri_start, "15:00") - datetime.timedelta(minutes=30)
        tot = datetime.timedelta(hours=sum_hours, minutes=sum_minutes) + fri_time
        left = datetime.timedelta(hours=40) - tot
        if int(checkin.split(":")[0]) < 11:
            left += datetime.timedelta(minutes=30)
        in_format = checkin.split(":")
        in_hours, in_minutes = int(in_format[0]), int(in_format[1])
        checkout = datetime.datetime(2022, 1, 1, in_hours, in_minutes) + left
        print("Check out today at {:d}:{:02d}".format(checkout.hour, checkout.minute))
    if day == "F" or day == "f":
        # Calculate Friday start
        sum = float(input("How many hours have you worked so far? "))
        sum_format = convert_helper(sum, 2).split(":")
        sum_hours, sum_minutes = int(sum_format[0]), int(sum_format[1])
        checkin = input("What time did you check in? (HH:MM) ")
        checkout = input("What time do you want to check out today? (HH:MM) ")
        today_hours = difference_helper(checkin, checkout)
        if int(checkin.split(":")[0]) < 11:
            # We have not eaten lunch yet, that will happen before our end time
            today_hours -= datetime.timedelta(minutes=30)
        tot = today_hours + datetime.timedelta(hours=sum_hours, minutes=sum_minutes)
        left = datetime.timedelta(hours=40) - tot + datetime.timedelta(minutes=30)
        fri_start = datetime.datetime(2022, 1, 1, 15, 0) - left
        print("Start on Friday at {:d}:{:02d}".format(fri_start.hour, fri_start.minute))
    cont = input("Press enter to continue.")


def print_menu():
    print("*************************")
    print("     Timecard Helper     ")
    print("*************************")
    print()
    print("Select an option:")
    print("   (1) How much time left?")
    print("   (2) Scheduler")
    print("   (3) Decimal to minute converter")
    print("   (4) Time difference")
    print("   (q) Quit")
    print()


def main():
    print_menu()
    selection = input("> ")
    while selection != "q":
        if selection == "1":
            time_left()
        elif selection == "2":
            scheduler()
        elif selection == "3":
            converter()
        elif selection == "4":
            time_difference()
        else:
            print("Invalid selection")

        print()
        print_menu()
        selection = input("> ")


if __name__ == '__main__':
    main()

