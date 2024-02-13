import smtplib
my_email = ""
password = ""


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
    #connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg= "Subject:Hello\n\nThis is the body")
    
#Gmail: smtp.gmail.com
#Hotmail: smtp.live.com
#Outlook: outlook.office365.com
#Yahoo: smtp.mail.yahoo.com