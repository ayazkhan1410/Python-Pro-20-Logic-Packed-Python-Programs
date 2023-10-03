# Problem No 11
'''
You are given an array(list) strarr of strings and an integer k. Your task is to return the
first longest string consisting of k consecutive strings taken in the array.
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
Concatenate the consecutive strings of strarr by 2, we get:
treefoling (length 10) concatenation of strarr[0] and strarr[1]
folingtrashy (" 12) concatenation of strarr[1] and strarr[2]
trashyblue (" 10) concatenation of strarr[2] and strarr[3]
blueabcdef (" 10) concatenation of strarr[3] and strarr[4]
abcdefuvwxyz (" 12) concatenation of strarr[4] and strarr[5]
Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so
longest_consec(strarr, 2) should return "folingtrashy".
'''
def longest_consec_strings(strarr, k):
    result = "" # This is where we'll store the longest string we find.
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index + k])
            if len(s) > len(result):
                result = s
    return result
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
k = 2
print(longest_consec_strings(strarr, k))

# Problem No 12
'''
Your task is to sort a given string. Each word in the string will contain a single
number. This number is the position the word should have in the result. Note:
Numbers can be from 1 to 9. So 1 will be the first word (not 0). If the input string is
empty, return an empty string. The words in the input String will only contain valid
consecutive numbers.
"is2 Thi1s T4est 3a" --> "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2" --> "Fo1r the2 g3ood 4of th5e pe6ople"
"" --> ""
'''
def order(sentence):
    if sentence == "":
        return ""
    else:
        sentence = sentence.split()
        sentence.sort()
        return ' '.join(sentence)

sentence = "is2 Thi1s T4est 3a"
print(order(sentence))

# scentence = "4of Fo1r pe6ople g3ood th5e the2"
# print(order(scentence))


# Problme No 13
from random import choice
count = 0
user_wins = 0
computer_wins = 0
cc = ["paper","rock","scissor"]
print("Welcome to our paper, rock and scissor game")
round1 = int(input("Enter how many rounds you wanted to  play : "))
for i in range(1,round1 + 1):
    print("Round : ", i)
    print("Paper")
    print("Rock")
    print("Scissor")
    user_input = input("Chose : ")
    computer_input = choice(cc)
    print("Computer choice : ", computer_input)
    print("User choice : ",  user_input)
    if user_input == computer_input:
        print("Match tied")
        count = count + 1
    elif user_input == 'paper'.lower() and computer_input == 'rock'.lower():
        print("User wins")
        user_wins = user_wins + 1
        count += 1
    elif user_input == 'rock'.lower() and computer_input == 'scissor'.lower():
        print("User wins")
        user_wins = user_wins + 1
        count = count + 1
    elif user_input == 'scissor'.lower() and computer_input == 'paper'.lower():
        print("User wins")
        user_wins = user_wins + 1
        count = count + 1
    else:
        print("Computer wins")
        computer_wins = computer_wins + 1
        count = count + 1
print("Total games played : ", count)
print("User win : ", user_wins)
print("Computer wins : ", computer_wins)

# Problem No 14
'''
Implement the function unique_in_order which takes as argument a sequence and
returns a list of items without any elements with the same value next to each other
and preserving the original order of elements.
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]
'''
def unique_in_order(sequence):
    if len(sequence) == 0:
        return []
    else:
        result = [sequence[0]] # First element is always unique
        for i in sequence[1:]: # then we iterate over the rest of the elements
            if i != result[-1]: # if the current element is not equal to the last element of the result
                result.append(i) # then we append it to the result
        return result # and return the result
print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))    
# Problem No 15
def atm_machine(password):
    if type(password) ==  str and len(password) == 5 or len(password) == 3:
        print("False")
    else:
        print("True")
atm_machine('12345')