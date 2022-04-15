from datetime import date

class Item():
  name: str = 'Item'
  date_added: date = date.today()

  def __init__(self, name: str) -> None:
    self.name = name
    self.date_added = date.today()
