# advent-of-code-challenges

--- Day 1: Sonar Sweep ---

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

## Approach

My approach to solving this problem is to use a linked list class.
I iterated over the lined list while maintaining reference to the
current and next nodes. I used a counter and incremented it as there
were an increase, and kept iterating if there wasn't. When the last node
is reached, the loop ends.
