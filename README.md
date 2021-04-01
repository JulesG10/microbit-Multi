# Microbit Multi

Radio message manager for several users for microbit.

## Usage

````python
import radio
from microbit import *

def demo():
    multi = Multi("doe",30,True) # Username , channel port, Save users messages (True/False)
    multi.set_access_key("my_secret_key") # Channel key
    multi.add_user("john") # Add to allowed users

    while True:
        data = multi.recieve(radio.recieve()) # listen for messages

        for new_user in multi.unknown_users: # check for unknown users
            multi.add_user(new_user)
            print("Add new user: {0}".format(new_user))
            multi.clear_unknown_users() 

        if data != None:
            if multi.get_active_user() == "john": # Last message sender
                print("John say: {0}".format(data))
        else:
            if button_a.is_pressed(): # button A click
                multi.send("I have {0} messages saved. ".format(multi.messages.count()))    # send message to users


demo() # Start
```