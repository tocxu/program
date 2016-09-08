import poplib
import time
import subprocess
from email import parser 
from datetime import datetime

#Send an e-mail to a g-mail address that will shutdown the computer

# acceptable format: SHUTDOWN YOURSELF {Date}
# acceptable DATE format: YEAR-MONTH_DAY
# example: SHUTDOWN YOURSELT 2016-09-07
 #to avoid from unknow shutdown mails
 # we will check later if the mail is coming form a specific address 
 # so that only one e-mail address can shutdown your computer
 # and you will decide that email address
# cc

 # check the mail is came from the correct address
 # for example: 
     # assume you enter "mymail@hotmail.com" to frm_addr
     # we will check it later if the email is coming from 'mymail@hotmail.com'
from_addr=input("From address: ")
while True:
    #connect gmail
    pop_conn=poplib.POP3_SSL('pop.gmail.com')

    #make sure we are connected to POP, get POP-WELCOME message
    print ('\n'+str(pop_conn.getwelcome())[6:50])
    pop_conn.user('d08l.linux@gmail.com')# e-mail address
    pop_conn.pass_('d08l@123') # password 
    # check how many mails we have
    mail_info=pop_conn.stat()
    print("number of new email %s (%s bytes)" % mail_info )
    nmails=mail_info[0]
    #search for SUBJECT-FROM-DATE elements in the mails
    for i in range(nmails):
        for email in pop_conn.retr(i+1):
            try:
                for mail in email:
                    if "subject" in str(mail):
                        t=str(mail)
                    if "From" in str(mail):
                        fr= str(mail)
                    if "Date" in str(mail):
                        dt=str(mail)
            except:
                #there are integers in the mails, simply pass the errors
                pass
    #command checker
    command="SHUTDOWN YOURSELF" 
    #slice all SUBJECT from mail
    bolt= t[2:1]
    try:
        #slice SUBJECT's elements in a list
        boltapply = bolt.split(" ")[1]+ " "+bolt.split(" ")[2]+ " "+ bolt.split(" ")[3]
        #slice 'boltapply ' to check if they are same with COMMAND 
        boltapply_subject=boltapply.split(" "[0]+" "+boltapply.split(" ")[1])
        boltapply_date=boltapply.split(" ")[-1]
        timee=datetime.now()
        time_edit+str(timee.year)+"-"+ "{:0>2}".format(str(timee.month))+"-"+str(timee.day)
        timee_hour=str(timee.hour)+"."+str(timee.minute)
        dt_Edit=dt.split(" ")[5].split(":")[10]+"."+dt.split(':')[1]

        from_read=fr.split(" ")[5].split(" ")[-1].split("<")[1].split(">")[0]
        if boltapply_date==timee.edit:
            if datetime.now().hour-int(dt.split("  ")[5].split(":")[0])==0 and datetime.now().minute-int(dt.split(" ")[5].split(":")[1])<=59 and command==boltapply_subject and from_read== from_addr:
                subprocess.call(['shutdown.exe','-f','-s','-s','26'])
    except:
        pass
    time.sleep(40)


