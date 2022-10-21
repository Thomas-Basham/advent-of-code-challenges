from sonar_sweep import LinkedList
from challenge_input import challenge_input, test_case, edge_case_same_number


def test_linked_list_exists():
  assert LinkedList()


def test_add_one():
  linked_list = LinkedList()

  linked_list.insert(test_case[0])

  actual = str(linked_list)
  expected = '{ 199 } -> NULL'
  assert actual == expected


def test_add_test_case():
  linked_list = LinkedList()

  linked_list.insert_many(test_case)

  actual = str(linked_list)
  expected = '{ 199 } -> { 200 } -> { 208 } -> { 210 } -> { 200 } -> { 207 } -> { 240 } -> { 269 } -> { 260 } -> { 263 } -> NULL'
  assert actual == expected


def test_sweep():
  linked_list = LinkedList()

  linked_list.insert_many(test_case)
  linked_list.sweep()

  actual = linked_list.count
  expected = 7
  assert actual == expected


def test_sweep_edge_case_same():
  linked_list = LinkedList()

  linked_list.insert_many(edge_case_same_number)
  linked_list.sweep()

  actual = linked_list.count
  expected = 7
  assert actual == expected


def test_sweep_challenge_case():
  linked_list = LinkedList()

  linked_list.insert_many(challenge_case())
  linked_list.sweep()

  actual = linked_list.count
  expected = 1215
  assert actual == expected


def test_sweep_sliding_sum():
  linked_list = LinkedList()

  linked_list.sliding_sum(test_case)
  linked_list.sweep()

  actual = linked_list.count
  expected = 5
  assert actual == expected


def test_sweep_sliding_sum_challenge_case():
  linked_list = LinkedList()

  linked_list.sliding_sum(challenge_case())
  linked_list.sweep()

  actual = linked_list.count
  expected = 1150
  assert actual == expected


def test_found_part_2_solution():
  # someone else wrote this solution, linked below.
  # I liked this solution, for how simple it is and how clean it looks
  # I wanted to see how the solution I wrote measured against it in speed.
  # run $ pytest --durations=1 to see
  # https://github.com/YokiDiabeul/advent_of_code/blob/a296b7efc58d309722048667b978ad5f87edd770/day%201/1.py

  # part one
  def count_bigger_in_list(inputs):
    return sum([inputs[i - 1] < inputs[i] for i in range(1, len(inputs))])

  part_two = [challenge_case()[i - 2] + challenge_case()[i - 1] + challenge_case()[i] for i in range(2, len(challenge_case()))]

  actual = count_bigger_in_list(part_two)
  expected = 1150
  assert actual == expected


def challenge_case():

  # make a list of strings separted by lines
  converted = challenge_input.split('\n')

  # remove empty values
  while "" in converted:
    converted.remove("")

  # convert strings to numbers
  converted = list(map(int, converted))

  return converted
