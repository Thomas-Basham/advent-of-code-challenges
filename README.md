# Advent of Code Challenge

[![Python application](https://github.com/Thomas-Basham/advent-of-code-challenges/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/Thomas-Basham/advent-of-code-challenges/actions/workflows/python-app.yml)

### [Solution](sonar_sweep.py)

### [Tests](tests/test_sonar_sweep.py)

## Challenge: Day 1: Sonar Sweep

This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and
so on.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with

- you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no
measurement before the first measurement.) In the example above, the changes are as follows:

    199 (N/A - no previous measurement)
    200 (increased)
    208 (increased)
    210 (increased)
    200 (decreased)
    207 (increased)
    240 (increased)
    269 (increased)
    260 (decreased)
    263 (increased)

In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?

    Input:
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263

    Output:
    7

-------- Part Two --------

Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

    199  A
    200  A B
    208  A B C
    210    B C D
    200  E   C D
    207  E F   D
    240  E F G
    269    F G H
    260      G H
    263        H

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (
199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The
sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous
sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements
left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

    A: 607 (N/A - no previous sum)
    B: 618 (increased)
    C: 618 (no change)
    D: 617 (decreased)
    E: 647 (increased)
    F: 716 (increased)
    G: 769 (increased)
    H: 792 (increased)

In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

    Input:
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263

    Output:
    5

## Approach

I used Python to solve this challenge.

My approach to solving this was to use a linked list class.
I created a method within the linked list class called sweep() that iterated over the linked list
while maintaining reference to the current and next nodes. I used a counter and incremented it as there
were an increase, and kept iterating if there wasn't. When the last node
is reached, the loop ends.

Another task was retrieving the challenge inputs and converting them
into a list. There were a number of ways I thought of doing this. I could have created
a text file and iterated through each line to make a list. I decided to use a docstring with the
challenge inputs copied inside. I cleaned up the list by removing empty strings and converting any strings
to integers.

For part two I added another method to the linked list class and used numpy to make a new convolved list
of integers, and then used the same sweep() method to return the count of increases. I learned about
the numpy.convolve()
method [here](https://stackoverflow.com/questions/38507672/summing-elements-in-a-sliding-window-numpy)
from a google search "python sliding sum".

## Installation

To install:

- clone this repo into your machine
- create and activate a virtual environment
  - Run these scripts:

        $ python -m venv .venv
        $ source .venv/bin/activate
- Install dependencies
  - Run:

        $ pip install -r requirements.txt

## Tests

To run all tests use:

        $ pytest

To run part 1 challenge test use:

        $ pytest tests/test_sonar_sweep.py::test_sweep_challenge_case

To run part 2 test use:

        $ pytest tests/test_sonar_sweep.py::test_sweep_sliding_sum_challenge_case

## Resources

[adventofcode.com/2021/day/1](https://adventofcode.com/2021/day/1/)

[adventofcode.com/2021/day/1/input](https://adventofcode.com/2021/day/1/input)

[numpy.org/doc/stable/reference/generated/numpy.convolve.html](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html)
