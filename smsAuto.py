from twilio.rest import Client 
 
account_sid = 'AC75407e030fb9405e780cd17d52c9bd78' 
auth_token = 'dbac067579efcaa7b6e6d3eaae7ee26d' 
client = Client(account_sid, auth_token) 
def sendMessage():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Send Message',      
                              to='whatsapp:+918373905132' 
                          ) 
    print(message.sid)

    