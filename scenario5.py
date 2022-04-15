from datetime import date
import unittest
from item import Item
from list import List

class TestScenario5(unittest.TestCase):
  def setUp(self) -> None:
    self.item = 'Item'
    self.list = List()
    item = Item(self.item)
    self.list.add_item(item)

    return super().setUp()

  def tearDown(self) -> None:
    return super().tearDown()

  def test_list(self):
    c1 = self.list.check_has_list()
    self.assertEqual(c1, True)

  def test_has_item(self):
    c2 = self.list.check_has_item(self.item)
    self.assertEqual(c2, True)

  def test_item_shown(self):
    out_string = self.list.print_list()
    a1 = self.item in out_string
    self.assertEqual(a1, True)

  def test_has_date_added(self):
    out_string = self.list.print_list()
    a1 = date.today().isoformat() in out_string
    self.assertEqual(a1, True)
    
if __name__ == '__main__':
    unittest.main()
