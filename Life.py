class Life:
    def __init__(self):
        self.tough_times = True
        self.helper = "God"
        self.hope = True

    def keep_going(self):
        if self.helper=="God":
            self.strength="renewed"
            self.faith="unshaken"
            self.joy="coming soon"

        return "Keep trusting God.Never give up!"
me = Life()
print(me.keep_going())
print(me.strength)
print(me.faith)
print(me.joy)