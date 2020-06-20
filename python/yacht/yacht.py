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
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12

SINGLES_MAP = {
    ONES: 1,
    TWOS: 2,
    THREES: 3,
    FOURS: 4,
    FIVES: 5,
    SIXES: 6,
}


def _score_yacht(dice: list, *args, **kwargs) -> int:
    return 50 if len(set(dice)) == 1 else 0


def _score_singles(dice: list, category: int, *args, **kwargs) -> int:
    count = dice.count(SINGLES_MAP[category])
    return SINGLES_MAP[category] * count if count else 0


def _score_full_house(dice: list, *args, **kwargs) -> int:
    counts = {}
    for num in dice:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return sum(dice) if set(counts.values()) == {2, 3} else 0


def _score_four_of_a_kind(dice: list, *args, **kwargs) -> int:
    counts = {}
    for num in dice:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for k, v in counts.items():
        if v >= 4:
            return k * 4
    return 0


def _score_little_straight(dice: list, *args, **kwargs) -> int:
    return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0


def _score_big_straight(dice: list, *args, **kwargs) -> int:
    return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0


def _score_choice(dice: list, *args, **kwargs) -> int:
    return sum(dice)


def score(dice: list, category: int) -> int:
    return {
        YACHT: _score_yacht,
        ONES: _score_singles,
        TWOS: _score_singles,
        THREES: _score_singles,
        FOURS: _score_singles,
        FIVES: _score_singles,
        SIXES: _score_singles,
        FULL_HOUSE: _score_full_house,
        FOUR_OF_A_KIND: _score_four_of_a_kind,
        LITTLE_STRAIGHT: _score_little_straight,
        BIG_STRAIGHT: _score_big_straight,
        CHOICE: _score_choice,
    }[category](dice, category)
