import radio
from microbit import *

class Multi:

    key = ""
    user_name = ""

    users = []
    unknown_users = []

    active_user = ""
    save_messages = False
    messages = []


    def __init__(self,username,channel,saveMessages = False):
        radio.on()
        radio.config(power=7)
        radio.config(channel=channel)

        self.user_name = username   
        self.save_messages = saveMessages

    def set_access_key(self,key=""):
        valid_key = ""
        allowed = ['_','@','.',',','?','"','\'','%','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        for i in range(0,len(key)):
            if key[i] in allowed:
                valid_key += key[i]

        self.key = valid_key

    def add_user(self, user):
        if not user in self.users:
            self.users.append(user)
            return True
        return False

    def get_active_user(self):
        return self.active_user

    def clear_unknown_users(self):
        for user in self.users:
            if user in self.unknown_users:
                self.unknown_users.remove(user)

    def recieve(self,data=""):
        if data:
            message = data.split(':')
            if len(message) >= 3:
                if message[0] == self.key and message[1] in self.users:
                    self.active_user = message[1]
                    
                    message.pop(0)
                    message.pop(0)
                    result = ":".join(message)
                    if self.save_messages:
                        self.messages.append(result)
                    return result
                elif not message[1] in self.users:
                    if message[1] in self.unknown_users:
                        self.unknown_users.append(message[1])
        return None


    def send(self,data):
        message = self.key+":"+self.user_name+":"+str(data)
        radio.send(message)
        if self.save_messages:
            self.messages.append(data)
        return message

    