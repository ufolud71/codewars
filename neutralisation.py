#Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

#When positives and positives interact, they remain positive.
#When negatives and negatives interact, they remain negative.
#But when negatives and positives interact, they become neutral, and are shown as the number 0.
def neutralise(s1, s2):
    stringList = []
    for i in range(len(s1)):
        if (s1[i] == "+" and s2[i] == "+"):
            stringList.append("+")
        elif (s1[i] == "-" and s2[i] == "-"):
            stringList.append("-")
        else:
            stringList.append("0")
    return "".join(stringList)


neutralise("++--", "+--+")