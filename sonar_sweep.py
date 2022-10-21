import numpy as np
from challenge_input import challenge_input

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
    uses numpy to convolve a list of integers by a sliding window of 3 nodes' sum
      - accepts: list of integers
      - inserts convolved list into linked list
      - returns: nothing
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


class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next = next_node


def convert_challenge_case(test_case):
  """
  * convert challenge case
    - accepts: a test case copied from https://adventofcode.com/2021/day/1/input
    - returns: a list of integers
  """

  # make a list of strings separted by lines
  converted = test_case.split('\n')

  # remove empty values
  while "" in converted:
    converted.remove("")

  # convert strings to numbers
  converted = list(map(int, converted))

  return converted


# ****************** SOLUTION DRIVER CODE ******************
#             to run: $ python sonar_sweep.py
if __name__ == "__main__":
  def sonar_sweep_part_1():
    linked_list = LinkedList()

    linked_list.insert_many(convert_challenge_case(challenge_input))
    linked_list.sweep()

    print(f"PART 1: There are {linked_list.count} measurements that are larger than the previous measurement")
    return linked_list.count


  def sonar_sweep_part_2():
    linked_list = LinkedList()

    linked_list.sliding_sum(convert_challenge_case(challenge_input))
    linked_list.sweep()

    print(f"PART 2: There are {linked_list.count} measurements that are larger than the previous measurement")
    return linked_list.count


  sonar_sweep_part_1()
  sonar_sweep_part_2()
