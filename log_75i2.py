"""Quick helpers."""

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

def flatten(xs):
    return [y for x in xs for y in x]

def clamp(value, low, high):
    return max(low, min(value, high))
