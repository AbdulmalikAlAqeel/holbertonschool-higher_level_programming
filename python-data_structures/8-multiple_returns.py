#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with string length and its first character."""
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
