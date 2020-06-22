from datetime import datetime
from threading import Timer
import smtplib, ssl

birthdays = {   
                #input birthdays here as key:value pairs
                '12/20' : ['Santa Claus'],
                }

todaysdate = datetime.date(datetime.now())
formattedDate = str(todaysdate).split('-')
monthDay = formattedDate[1]+ '/' + formattedDate[2]

if monthDay in birthdays:
    todaysBirthdays = birthdays[monthDay]
    nameList = ''
    for name in todaysBirthdays:
        nameList += '\n' + name 
        message = 'Todays birthdays are: ' + nameList
else:
    message = 'No Birthdays Today.'


sender_email = '#sender email here'
receiver_email = '#receiever email here'

#standard port for emailing on SMTP
port = 465
password = input("Type your password: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    #first arguement is email address of the sender
    #followed by the password input 
    server.login(" ", password)
    server.sendmail(sender_email,receiver_email,message)
    
