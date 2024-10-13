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