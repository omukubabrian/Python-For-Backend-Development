from datetime import date,timedelta
class LibraryItem:
    kind="item"
    loan_days=14
    late_fee_per_day=0.25

    def __init__(self,item_id:int,title:str,borrower:str|None=None,due_date:date|None=None)->None:
        self.item_id=item_id
        self.title=title
        self._borrower=borrower
        self._due_date=due_date

    @property
    def is_available(self)->bool:
        return self._borrower is None

    @property
    def borrower(self)->str|None:
        return self._borrower

    @property
    def due_date(self)->date|None:
        return self._due_date

    def check_out(self,member:str,today:date|None=None)->None:
        if not self.is_available:
            raise ValueError(f"'{self.title}' is already borrowed")

        if not member.strip():
            raise ValueError("Member name is required.")

        today=today or date.today()
        self._borrower=member.strip()
        self._due_date=today + timedelta(days=self.loan_days)


    def return_item(self,today:date|None=None)->float:
        if self.is_available or self._due_date is None:
            raise ValueError(f"'{self.title}' is not currently borrowed.")
        today=today or date.today()
        days_late=max(0,(today-self._due_date).days)
        fee=round(days_late * self.late_fee_per_day,2)


        self._borrower=None
        self._due_date=None
        return fee

    def details(self)->str:
        return ""

    def to_dict(self)->dict:
        return{"kind":self.kind,"item_id":self.item_id,"title":self.title,"borrower":self._borrower,"due_date":self._due_date.isoformat() if self._due_date else None
        }



    def __str__(self)->str:
        status="available"if self.is_available else f"borrowed,due {self._due_date}"
        return f"#{self.item_id} [{self.kind}] {self.title} {self.details()} ({status})"

class Book(LibraryItem):
    kind="book"
    loan_days=21
    late_fee_per_day=0.25

    def __init__(self,item_id:int,title:str,author:str,**kwargs)->None:
        super().__init__(item_id,title,**kwargs)
        self.author=author

    def details(self)->str:
        return f"by {self.author}"

    def to_dict(self)->dict:
        data=super().to_dict()
        data["author"]=self.author
        return data


class Magazine(LibraryItem):
    kind="magazine"
    loan_days=7
    late_fee_per_day=0.50


    def __init__(self,item_id:int,title:str,issue:str,**kwargs)->None:
        super().__init__(item_id,title,**kwargs)
        self.issue=issue

    def details(self)->str:
        return f",issue {self.issue}"

    def to_dict(self)->dict:
        data=super().to_dict()
        data["issue"]=self.issue
        return data

ITEM_TYPES={"book":Book, "magazine":Magazine }
def item_from_dict(data: dict)->LibraryItem:

    data=dict(data)
    item_class=ITEM_TYPES[data.pop("kind")]
    if data.get("due_date"):
        data["due_date"]=date.fromisoformat(data["due_date"])
    return item_class(**data)

    
    
