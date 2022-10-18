from sonar_sweep import LinkedList


def test_linked_list_exists():
  assert LinkedList()


def test_add_one():
  LL = LinkedList()

  LL.insert(test_case[0])

  expected = '{ 199 } -> NULL'

  assert str(LL) == expected


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
