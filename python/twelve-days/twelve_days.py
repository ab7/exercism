def recite(start_verse, end_verse):
    days = (
        'first',
        'second',
        'third',
        'fourth',
        'fifth',
        'sixth',
        'seventh',
        'eighth',
        'ninth',
        'tenth',
        'eleventh',
        'twelfth',
    )
    verses = (
        'a Partridge in a Pear Tree.',
        'two Turtle Doves, ',
        'three French Hens, ',
        'four Calling Birds, ',
        'five Gold Rings, ',
        'six Geese-a-Laying, ',
        'seven Swans-a-Swimming, ',
        'eight Maids-a-Milking, ',
        'nine Ladies Dancing, ',
        'ten Lords-a-Leaping, ',
        'eleven Pipers Piping, ',
        'twelve Drummers Drumming, ',
    )
    result = []
    for i in range(start_verse - 1, end_verse):
        verse_range = [v for v in verses[i::-1]]
        if len(verse_range) > 1:
            verse_range[-1] = f'and {verse_range[-1]}'
        verse = f'On the {days[i]} day of Christmas my true love gave to me: '
        verse += ''.join(verse_range)
        result.append(verse)
    return result
