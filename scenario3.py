from datetime import date
import unittest
from item import Item
from list import List

class TestScenario1(unittest.TestCase):
  def setUp(self) -> None:
    self.input = 'New Item'
    self.list = List()

    return super().setUp()

  def tearDown(self) -> None:
    return super().tearDown()

  def test_list(self):
    c1 = self.list.check_has_list()
    self.assertEqual(c1, True)

  def test_input(self):
    c2 = self.list.check_has_input(self.input)
    self.assertEqual(c2, False)

  def test_add_item(self):
    item = Item(self.input)
    self.list.add_item(item)
    a1 = self.list.check_has_item(self.input)
    self.assertEqual(a1, False)

  def replace_item(self):
    self.list.edit_item('Item', 'item')
    a1 = self.list.check_has_item(self.input)
    self.assertEqual(a1, True)

  def test_item_shown(self):
    item = Item(self.input)
    self.list.add_item(item)
    out_string = self.list.print_list()
    a2 = self.input in out_string
    self.assertEqual(a2, True)

  def test_hide_input(self):
    self.input = ''
    a3 = self.input == ''
    self.assertEqual(a3, True)
    
if __name__ == '__main__':
    unittest.main()