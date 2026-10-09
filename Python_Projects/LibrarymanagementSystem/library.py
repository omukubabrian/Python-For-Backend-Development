import json
from pathlib import Path

from models import Book,LibraryItem,Magazine,item_from_dict


class Library:
    def __init__(self,path:Path)->None:
        self.path=path
        self._items:dict[int,LibraryItem]={}
        self.load()

    def load(self)->None:

        try:
            raw=json.loads(self.path.read_text(encoding="utf-8"))
            self._tems={i["item_id"]:item_from_dict(i)for i in raw}

        except(json.JSONDecodeError,KeyError,TypeError):
            print("Warning:catalog file is damaged.Starting empty.")
            self._items={}


    def save(self)->None:
        self.path.parent.mkdir(parents=True,exist_ok=True)
        data=[item.to_dict()for item in self._items.values()]
        self.path.write_text(json.dumps(data, indent=2),encoding="utf-8")

    def _next_id(self)->int:
        return max(self._items,default=0)+1

    def _require_text(self,*values:str)->None:
        if any(not v.strip() for v in values):
            raise ValueError("All fields are required.")


    def add_book(self,title:str,auther:str)->Book:
        self._require_text(title,author)

        book=Book(self._next_id(),title.strip(),auther.strip())
        self._items[book.item_id]=book
        self.save()
        return book

    def add_magazine(self,title:str,issue:str)->Magazine:
        self._require_text(title,issue)
        magazine=Magazine(self._next_id(),title.strip(),issue.strip())
        self._items[magazine.item_id]=magazine
        self.save()
        return magazine

    def get(self,item_id:int)->LibraryItem:
        try:
            return self._items[item_id]
        

        except KeyError:
            raise KeyError(f"No item with id {item_id}")from None


    def check_out(self,item_id:int,member:str)->None:
        self.get(item_id).check_out(member)
        self.save()

    def return_item(self,item_id:int)->float:
        fee=self.get(item_id).return_item()
        self.save()
        return fee

    def search(self,term:str)->list[LibraryItem]:
        term=term.lower().strip()
        return[i for i in self._items.values() if term in f"{i.title}{i.details()}".lower()]


    def available(self)->list[LibraryItem]:
        return[i for i in self._items.values() if i.is_available]

    def all_items(self)->list[LibraryItem]:
        return list(self._items.values())

    