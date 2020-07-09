def slices(series: str, length: int) -> list:
    if length <= 0 or length > len(series):
        raise ValueError('Length must be between 1 and the length of the series.')
    return [series[i:i + length] for i in range(len(series) - length + 1)]
