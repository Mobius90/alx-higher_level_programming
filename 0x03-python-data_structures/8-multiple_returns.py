#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return sentence
    return (len(sentence), sentence[0])
