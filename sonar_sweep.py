"""
***** Linked List class *****

Functions:
 * Insert nodes
    - @param {value} any values
    - returns nothing

 * TODO: "scan" nodes for a count of increases inside
    Scan for Increases
      - returns nothing

 * __str__
    - returns string such as  "{ 199 } -> { 200 } -> { 208 } -> NULL"

"""


class LinkedList:

  def __init__(self):
    self.head = None
    self.value = None
    self.next = next

  def insert(self, value):
    new_node = Node(value)
    node = self.head
    new_node.next = node
    self.head = new_node

  def __str__(self):
    node = self.head
    nodes = []

    while node:
      nodes.append(node.value)
      node = node.next

    while nodes:
      return ' -> '.join('{ ' + str(node) + ' }' for node in nodes) + ' -> NULL'
    return "NULL"


class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next = next_node
