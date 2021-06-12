import datetime
import winsound
#from winsound import Tr

alarmhours=int(input("At what time you want to wakeup?"))
alarmminute=int(input("enter the minutes:"))
ampm=str(input("am or pm::"))

if ampm == "pm":
    alarmhours=alarmhours+12

while(1==1):
    if (alarmhours==datetime.datetime.now().hour) and (alarmminute == datetime.datetime.now().minute):
        print("wake up! wake up!")
        winsound.Beep(2500,1000)
        break
print("reminder! wake up!!")




