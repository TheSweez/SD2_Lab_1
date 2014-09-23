def printMatching(s1, s2):
#determining which string is shorter or longer
    if len(s1) < len(s2):
        longer = s2
        shorter = s1
    else:
        shorter = s2
        longer = s1
#where the new strings will be stored
    s1_equals = []
    s2_equals = []

    s1_case = []
    s2_case = []

#looking in the shorter string (only need to go to end of shortest strng)   
    for i in range(len(shorter)):
#going through each letter in the strings to see if they match.
#the results are put into the lists above.
        if s1[i] == s2[i]:
            s1_equals.append(True)
            s2_equals.append(True)
        else:
            s1_equals.append(False)
            s2_equals.append(False)
#the next two loops stop the previous loop once "i" has reached a specific value
    for i in range(len(s1)):
        if len(s1_equals) > i and s1_equals[i] == True:
            s1_case.append((s1[i]).upper())               
        else:
            s1_case.append(s1[i])
            
    for i in range(len(s2)):
        if len(s2_equals) > i and s2_equals[i] == True:
            s2_case.append((s2[i]).upper())
        else:
            s2_case.append(s2[i])

#eliminates quotes and commas from what's being printed
    print (''.join(s1_case))
    print (''.join(s2_case))



def main():
    s1 = "abaababb"
    s2 = "aabbaababa"
    printMatching(s1, s2)

if __name__ == "__main__":
    main()
