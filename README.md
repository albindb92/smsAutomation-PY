# smsAutomation-PY

1: Create account in twilio - (www.twilio.com)
2: Go to sms dashboard in twilio and click on whatsapp
3: To begin testing, send a message from your whatsapp number to the whatsapp number provided by twilio with sandbox text messsage .
4: Once successfully done.
5: In the smsAuto.py give the token generated by twilio (NOte: In twilio switch to python code to get the token).
6: In smsAuto.py give sender and reciever number
7: Create scheduler file named scheduler.py and use python app schduler
8: Create requiremenst.py by command ( pip freeze > requirements.txt)
9: Create Procfile with no extension so that heroku can perform the actions need to be done
10:Then run the scheduler.py from Visual studio python run plugin
11: You should successfully recieve the messages on your whatsapp number configured with sandbox.
12: Then deploy to heroku by below command: a) heroku login
                                            b) git init
                                            c) git add .
                                            d) git commit -m "YOUR MESSAGE"
                                            e) git push heroku master
                                            
Follow below link for more details:
https://youtu.be/pQeFxdT3FGY

Cheers....
