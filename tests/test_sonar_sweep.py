from sonar_sweep import LinkedList


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

  for value in reversed(test_case):
    linked_list.insert(value)

  actual = str(linked_list)
  expected = '{ 199 } -> { 200 } -> { 208 } -> { 210 } -> { 200 } -> { 207 } -> { 240 } -> { 269 } -> { 260 } -> { 263 } -> NULL'
  assert actual == expected


def test_sweep():
  linked_list = LinkedList()

  for value in reversed(test_case):
    linked_list.insert(value)

  linked_list.sweep()

  actual = linked_list.count
  expected = 7
  assert actual == expected


test_case = [
  199,
  200,
  208,
  210,
  200,
  207,
  240,
  269,
  260,
  263
]
