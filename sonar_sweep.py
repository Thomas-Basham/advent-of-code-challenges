import numpy as np

"""
***** Linked List class *****

Functions:
 * insert
    inserts a single node into the linked list with the Node class
      - accepts: value
      - returns: nothing

 * insert_many
    inserts a a list of nodes into the linked list with the Node class
      - accepts: list of values
      - returns: nothing

 * sweep
    scans for Increases in the linked list, starting from the head
      - accepts: nothing
      - increments self.count
      - returns: nothing

 * sliding_sum
    https://stackoverflow.com/questions/38507672/summing-elements-in-a-sliding-window-numpy
    https://numpy.org/doc/stable/reference/generated/numpy.convolve.html
    uses numpy to convolve a list by a sliding window of 3 nodes' sum
      - accepts: list of integers
      - inserts convolved list into linked list
      - returns: nothing

 * __str__
    returns string representation of linked list such as  "{ 199 } -> { 200 } -> { 208 } -> NULL"
      - called with str(LinkedList())
"""


class LinkedList:
  def __init__(self):
    self.head = None
    self.value = None
    self.next = next
    self.count = 0

  def insert(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node

  def insert_many(self, values):
    for value in reversed(values):
      self.insert(value)

  def sweep(self):
    current = self.head

    while current.next:
      if current.next.value > current.value:
        self.count += 1
        current = current.next

      if not current.next:
        return

      if current.next.value <= current.value:
        current = current.next

    return

  def sliding_sum(self, nums_list):
    convolved_nums_list = np.convolve(nums_list, np.ones(3, dtype=int), 'valid')
    self.insert_many(convolved_nums_list)

  def __str__(self):
    current = self.head
    nodes = []

    while current:
      nodes.append(current.value)
      current = current.next

    while nodes:
      return ' -> '.join('{ ' + str(node) + ' }' for node in nodes) + ' -> NULL'

    return "NULL"


class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next = next_node
