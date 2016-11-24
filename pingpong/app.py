from rapidsms.apps.base import AppBase

class PingPong(AppBase):

    def handle(self, msg):
        
        
        if msg.text == "book":
            msg.respond('Hello user! May I know your zipcode for the booking?')
            return True
        elif msg.text == "lawrence":
            msg.respond('Hey Lawrence How are you doing?')
            return True
        elif  msg.text == "pratik":
            msg.respond('Hey Pratik How are you doing?')
            return True
        elif  msg.text == "shankar":
            msg.respond('Hey Shankar How are you doing?')
            return True
                
        return False
