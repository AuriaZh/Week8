# Object
# -> Specific intance of a class

# Class
# -> General deffinition
import datetime

class Message:
    def __init__(self, content, timestamp):
        self.content = content
        self.timestamp = timestamp

class iPhone:
    def __init__(self, name, version, phone_number, color, model): # constructor
        self.name = name
        self.ios_version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model
        self.messages = []

    def send_message(self, to, content):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = Message(content, timestamp)
        to.receive(msg)
    
    def receive(self, msg):
        self.messages.append(msg)
        print(f"{self.name} has received a message at {msg.timestamp}: {msg.content}")

    def check_messages(self):
        print(f"Messages for {self.name}:")
        for msg in self.messages:
            print(f" - {msg.timestamp}: {msg.content}")


    def set_name(self, new_name):
        if len(new_name) < 3:
            print("Name must be longer than 3 characters")
        else:
            self.name = new_name
            print(f"The phone's name has been updated to {self.name}")


# Create instances of the iPhone class
phone1 = iPhone(
    name="iPhone1", 
    version="15", 
    phone_number="123-456-789", 
    color="White", 
    model="15 Pro"
)
phone2 = iPhone(
    name="iPhone2", 
    version="15", 
    phone_number="123-123-123", 
    color="Purple", 
    model="16"
)

# Change names of the phones
phone1.set_name("Auria's iPhone")
phone2.set_name("Yu Shi's iPhone")

# Send an iMessage from phone1 to phone2
phone1.send_message(phone2, "Hello!")

# Check messages on phone2
phone2.check_messages()






