"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = (1, 50)
ONES = (2, 1)
TWOS = (3, 2)
THREES = (4, 3)
FOURS = (5, 4)
FIVES = (6, 5)
SIXES = (7, 6)
FULL_HOUSE = (8, None)
FOUR_OF_A_KIND = (9, 4)
LITTLE_STRAIGHT = (10, 30)
BIG_STRAIGHT = (11, 30)
CHOICE = (12, None)
LOSE = (13, 0)


def score(dice, category):
    if category[0] == YACHT[0]:
        return YACHT[1] if len(set(dice)) == 1 else LOSE[1]
    elif category[0] in {ONES[0], TWOS[0], THREES[0], FOURS[0], FIVES[0], SIXES[0]}:
        count = dice.count(category[1])
        return category[1] * count if count else LOSE[1]
    elif category[0] == FULL_HOUSE[0]:
        counts = {}
        for num in dice:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        return sum(dice) if set(counts.values()) == {2, 3} else LOSE[1]
    elif category[0] == FOUR_OF_A_KIND[0]:
        counts = {}
        for num in dice:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for k, v in counts.items():
            if v >= category[1]:
                return k * category[1]
        return LOSE[1]
    elif category[0] == LITTLE_STRAIGHT[0]:
        return category[1] if sorted(dice) == [1, 2, 3, 4, 5] else LOSE[1]
    elif category[0] == BIG_STRAIGHT[0]:
        return category[1] if sorted(dice) == [2, 3, 4, 5, 6] else LOSE[1]
    elif category[0] == CHOICE[0]:
        return sum(dice)
