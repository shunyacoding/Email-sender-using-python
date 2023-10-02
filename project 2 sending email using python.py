# send email using python
import smtplib
email=input("SENDER EMAIL")
password =input("PASSWORD")
reciever =input("RECIVER")
subject = input("SUBJECT")
message = input("MESSAGE")

text =f"subject: {subject}\n\n{message}"

my_email ="meenakshigautam86438@gmail.com"
password  ="abcdefgh"
reciever ="mahigautam1234@gmail.com"

server = smtplib.SMTP("smtp.gmail.com",587)
server.login(user=my_email,password=passcode)
server.starttls() # transfer layer secuirty

# try:
     #  connection.sendermail(from_addr=my_email,to_addr="reciever@gmail.com")
    #vexcept Exception as e:
      # print("something went wrong when sending the mail",e)
 
      # connection.close()

    