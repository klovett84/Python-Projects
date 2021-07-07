import datetime
import pytz

# Setting time objects for different timezones, along with business hours.
portlandTime =(datetime.datetime.now(pytz.timezone('US/Pacific')))
newYorkTime = (datetime.datetime.now(pytz.timezone('US/Eastern')))
londonTime = (datetime.datetime.now(pytz.timezone('Europe/London')))
tokyoTime = (datetime.datetime.now(pytz.timezone('Asia/Tokyo')))
businessOpen = 9
businessClose = 17

# Function to check if current time in each time zone is between 9-5
# If yes, the branch is open, if no, the branch is closed
def openOrClosed():
    print("Portland: {}".format(portlandTime.strftime("{}:{}{}".format("%I", "%M", "%p"))))
    if portlandTime.hour > businessOpen and portlandTime.hour < businessClose:
        print("The Portland branch is open!\n")
    else:
        print("The Portland branch is closed.\n")

    print("New York: {}".format(newYorkTime.strftime("{}:{}{}".format("%I", "%M", "%p"))))
    if newYorkTime.hour > businessOpen and newYorkTime.hour < businessClose:
        print("The New York branch is open!\n")
    else:
        print("The New York branch is closed.\n")

    print("London: {}".format(londonTime.strftime("{}:{}{}".format("%I", "%M", "%p"))))
    if londonTime.hour > businessOpen and londonTime.hour < businessClose:
        print("The London branch is open!\n")
    else:
        print("The London branch is closed.\n")

    print("Tokyo: {}".format(tokyoTime.strftime("{}:{}{}".format("%I", "%M", "%p"))))
    if tokyoTime.hour > businessOpen and tokyoTime.hour < businessClose:
        print("The Tokyo branch is open!\n")
    else:
        print("The Tokyo branch is closed.\n")



if __name__ == "__main__":
    openOrClosed()
