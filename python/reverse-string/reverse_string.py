def reverse_using_builtin(text: str) -> str:
    """
    Return reversed string using Python builtin.
    """
    return text[::-1]


def reverse(text: str) -> str:
    """
    Return reversed string without magic methods using mirror.
    """
    text_list = [c for c in text]
    start = 0
    end = len(text) - 1
    while start < end:
        start_saved = text_list[start]
        text_list[start] = text_list[end]
        text_list[end] = start_saved
        start += 1
        end -= 1
    return ''.join(text_list)
