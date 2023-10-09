#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    first = ""
    if (lenght == 0):
        return (lenght, None)
    else:
        return (lenght, sentence[0])
