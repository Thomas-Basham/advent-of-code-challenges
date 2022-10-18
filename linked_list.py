
"""
***** Linked List class *****

Functions:
 * Insert nodes
    - @param {value} any values
    - returns nothing

 * TODO: "scan" nodes for a count of increases inside
    Scan for Increases
      - returns nothing
"""


class LinkedList:
  """

  """
  def __init__(self):
    self.head = None
    self.value = None
    self.next = next

  def insert(self, value):
    new_node = Node(value)
    node = self.head
    new_node.next = node
    self.head = new_node


class Node:
  def __init__(self):
    self.value = None
    self.next = None
