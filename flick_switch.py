#Create a function that always returns True/true for every item in a given list.
#However, if an element is the word 'flick', switch to always returning the opposite boolean value.

#NOTES:
#"flick" will always be given in lowercase.
#A list may contain multiple flicks.
#Switch the boolean value on the same element as the flick itself.

def flick_switch(lst):
    flick_list = []
    flick = True
    for word in lst:
        if word == 'flick':
            flick = not flick
        flick_list.append(flick)
    print(flick_list)
    return flick_list

flick_switch(['codewars', 'flick', 'code', 'wars', 'flick'])