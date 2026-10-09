class Notification:
    def __init__(self,recipient:str,message:str)->None:
        self.recipient=recipient
        self.message=message

    def send(self)->str:
        raise NotImplementedError("Subclasses must implement send()")


class EmailNotification(Notification):
    def send(self)->str:
        return f"Email to {self.recipient}: {self.message}"


class SmsNotification(Notification):
    def send(self)->str:
        return f"SMS to {self.recipient}:{self.message}"



def broadcast(notifications:list[Notification])->list[str]:
  return [n.send()for n in notifications]


print(broadcast([
    EmailNotification("a@x.com","Hello"),
    SmsNotification("+254712453902","Hi"),
]))



    