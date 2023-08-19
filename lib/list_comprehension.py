#!/usr/bin/env python3

def return_evens(num_list):
    list_even = [num for num in num_list if (num % 2  == 0)]
    return list_even
    pass

def make_exclamation(sentence_list):
    list_string = [f"{string}!" for string in sentence_list]
    return list_string
    pass