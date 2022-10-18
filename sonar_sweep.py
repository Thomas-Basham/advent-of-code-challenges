"""
***** Linked List class *****

Functions:
 * Insert
    inserts a single node into the linked list
     with the Node class
      - @param {value} any values
      - returns nothing

 * sweep
    Scans for Increases on in the linked list
      - returns nothing

 * __str__
      - returns string such as  "{ 199 } -> { 200 } -> { 208 } -> NULL"
      - called with str(LinkedList())
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
