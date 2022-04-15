from item import Item

class List():
  items: list[Item] = []
  name: str = ''

  def __init__(self, name: str = 'List') -> None:
    self.items = []
    self.name = name

  def add_item(self, item: Item) -> None:
    self.items.append(item)
  
  def delete_item(self, item_name: str) -> None:
    self.items = [item for item in self.items if item.name != item_name]
  
  def edit_item(self, item_name: str, new_name: str) -> None:
    if len(self.items) <= 0:
      return
    
    item_index = next((i for i, item in enumerate(self.items) if item.name == item_name), -1)
    self.items[item_index].name = new_name
  
  def print_list(self) -> str:
    out_string = self.name + '\n'

    for item in self.items:
      out_string += item.name + '\t'
      out_string += item.date_added.isoformat() + '\n'
    
    # print(out_string)
    
    return out_string

  def check_has_list(self) -> bool:
    return isinstance(self.items, list)
  
  def check_has_input(self, input: str) -> bool:
    return bool(input)

  def check_has_item(self, item_name: str) -> bool:
    return next((i for i, item in enumerate(self.items) if item.name == item_name), -1) != -1
