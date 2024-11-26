class Phone:
    def __init__(self,name):
        self.name = name
    def call(sef,to):
        print("Dialing", to, "...")

class iPhone(Phone):
    def airdrop(self, to, file):
        print("Sending", file, "to", to, "...")

class Android(Phone):
    def ok_google(self):
        print("Ok Google")

phone = iPhone("ME")
phone.call('123-123-123')
phone.airdrop("You", "2.pdf")

phone2 = Android("YOU")
phone.call('123-123-123')
phone.okay_google()

