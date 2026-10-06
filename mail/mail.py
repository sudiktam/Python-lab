from mailerpy import Mailer

my_mailer = Mailer("smtp.gmail.com",587,"sudiktamthapa@gmail.com","icuf rydm abfm ojca")

content = "hello this is the test mail"
my_mailer.send_mail(
   "sudiktam57@gmail.com", #reciver 
   "test mail",#subject 
    content
)