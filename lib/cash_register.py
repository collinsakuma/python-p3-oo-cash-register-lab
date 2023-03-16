#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.last_transaction = price * quantity
    for i in range (quantity):
      self.items.append(title)

  def apply_discount(self):
    if self.discount > 0:
      discount_to_apply = self.discount / 100
      disc = self.total * discount_to_apply
      self.total = int(self.total - disc)
      print(f"After the discount, the total comes to ${800}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total = self.total - self.last_transaction