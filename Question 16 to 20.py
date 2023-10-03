# Problem No 16
'''Complete the solution so that the function will break up camel casing, using a space
between words.
"camelCasing" => "camel Casing"
"identifier" => "identifier"
"" => ""
'''
def break_camelCase(string):
    new_string = ''
    for i in string: # Loop through each character in the input string.
        if i.isupper():  #Check if the current character is uppercase (a capital letter).
            new_string = new_string + ' ' + i  # If it's uppercase, add a space and the uppercase letter to the new string.
        else:
            new_string = new_string +  i  #If it's not uppercase, just add the character to the new string.
    return new_string # After processing all characters, return the modified string.
# print(break_camelCase('camelCasing'))
# print(break_camelCase('identifier'))
# print(break_camelCase('ayazKhan'))

# Problem No 17
#skip
'''
Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive
integer p. we want to find a positive integer k, if it exists, such that the sum of the
digits of n taken to the successive powers of p is equal to k * n.
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵+ 8⁶+ 8⁷= 2360688 = 46288 * 51
'''
def dig_pow(n, p):
    num_str = str(n)  # Convert the number to a string, 
    total = 0         # Initialize the total sum
    
    # Loop through each digit's index and value
    for i in range(len(num_str)):
        digit = int(num_str[i])  # Convert the character to an integer
        total = total + digit ** (p + i)  # Add the powered digit to the total
    
    # Check if total is divisible by n
    if total % n == 0:
        return total // n
    else:
        return -1
print(dig_pow(695, 2))   
# print(dig_pow(46288, 3))


# Problem No 18
'''
Write a function that takes a string of parentheses, and determines if the order of the
parentheses is valid. The function should return true if the string is valid, and false if
it's invalid.
"()" => true
")(()))" => false
"(" => false
"(())((()())())" => true
'''    
def valid_parentheses2(scetence):
    if (scetence.count("(") == scetence.count(")")):
        return True
    else:
        return False
print(valid_parentheses2("()"))
print(valid_parentheses2(")"))
print(valid_parentheses2("(")) 
print(valid_parentheses2("(())((()())())"))
print(valid_parentheses2(")(()))"))
print(valid_parentheses2("())("))
print(valid_parentheses2("(()()))("))
print(valid_parentheses2("(()()))"))
print(valid_parentheses2("(()())("))
print(valid_parentheses2("(()())")) 

# Problem No 19
'''
Write a function that accepts a fight string consisting of only small letters and return
who wins the fight. When the left side wins, the Left side wins!, when the right side
wins, the Right side wins!, in other cases, Let's fight again!.
Left side letters
w - 4
p - 3
b - 2
s - 1
t - 0 (pretty word)
Right side letters
m - 4
q - 3
d - 2
z - 1
j - 0 (pretty word)
The other letters don't have power and are only victims.
The priest units t and j change the adjacent letters from hostile letters to friendly
letters with the same power.
alphabet_war("z") #=> "z" => "Right side wins!"
Explanation:
Letter z belongs to the right side letters and the left side has no letter so the right side
wins.
alphabet_war("tz") #=> "ts" => "Left side wins!"
Explanation:
Letter t is a pretty letter belonging to the left side. Pretty letters convert hostile letters
to friendly letters with the same power. Z is a hostile letter with power 1. T will convert
it to s a friendly letter with the same power.
'''
def alphabet_war(string):
    left_side = {'w':4,'p':3,'b':2,'s':1}
    right_side = {'m':4,'q':3,'d':2,'z':1}
    preety_word = {'t':0,'j':0}
    left_side_sum = 0
    right_side_sum = 0
    for i in string:
        if i in left_side:
            left_side_sum += left_side[i]
        elif i in right_side:
            right_side_sum += right_side[i]
    if left_side_sum > right_side_sum:
        return 'Left side wins'
    elif right_side_sum > left_side_sum:
        return 'Right side wins'
    elif preety_word:
        return "Let's become friends"
    else:
        return "Let's figth again !!!! "
i = True
while i:
    input1 = input("Enter the string : ")
    print(alphabet_war(input1))
    choice = input("Do you want to play again : y/n :")
    if choice == 'N'.lower():
        i = False
        break
    else:
        True
# Problem No 20
'''
Given two positive integers m (width) and n (height), fill a two-dimensional list (or
array) of size m-by-n in the following way:
a. All the elements in the first and last row and column are 1.
b. All the elements in the second and second-last row and column are 2,
excluding the elements from step 1.
c. All the elements in the third and third-last row and column are 3, excluding the
elements from the previous steps.
d. And so on ...
Given m = 10, n = 9, your function should return
[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
[1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
[1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
'''
def fill_2D_list(m, n): 
    result = [] # Define an empty list called 'result' to store the 2D list.
    for i in range(m): # 3
        result.append([])
        for j in range(n): #4
            result[i].append(min(i + 1, j + 1, m - i, n - j))
    return result

m = int(input("Enter the rows: "))
n = int(input("Enter the columns: "))
# print(fill_2D_list(m, n))
for row in fill_2D_list(m, n):
    print(row)