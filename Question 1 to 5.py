# Problem No 1
'''
Write a function which will take an integer as input and print each digit in a separate
line. You are not allowed to use str or any other method will convert the integer into
string.
Input: 1011
Output:
1
1
0
1
'''
def func1():
    user_input = int(input("Enter the number : "))
    while user_input > 0:
            # to separate the digits of the number and process them one by one.
            # The modulus operation gives you the remainder when you divide one number by another
            # When you do user_input % 10, you are getting the last digit of the user_input numbe
        print(user_input%10)
            # this operation helps you remove the last digit from the number, 
            # making the number smaller each time the loop runs.
        user_input = user_input//10
            # if we divided this with 10 then it give us infinte loop
            # Dividing by 10 gives the next digit,
            # and taking the modulus by 10 gives the last digit of a number
            # allowing us to separate and display each digit.
# func1()
#Problem No 2
'''
You are given words. Some words may repeat. For each word, output its number of
occurrences. The output order should correspond with the input order of appearance
of the word. See the sample input/output for clarification.
Input format: two parameters: first number of words, second list of words to process
Output format: Output two lines
First line: Number of unique words
Second line: Number of occurrences for each distinct word according to their
appearance in the input.
Input:
4, [“bcdef”, “abcdefg”, “bcde”, “bcdef”]
Output:
3
2 1 1
Output explanation:
First output distinct words.
Second line shows the count for each word which occurred in the list
'''
def word_count(word_list): #The def word_count(word_list): line defines a function named word_count that takes a list of words as input. 
    count = {} #there's an empty dictionary called count
    for word in word_list: #It goes through each word in the given list of words.
        if word in count:#This checks if the current word is already a key
            #in the count dictionary.
            count[word] += 1 #If the word is already in the dictionary,
            #it means we've seen it before. So, count[word] += 1
        else:
            count[word] = 1 #If the word is not in the dictionary (it's new), then else: part runs. It means we haven't seen this word before, so we add it to the count dictionary with a value of 1.
    return count #Finally, when the loop ends, the function returns the count
word_list = ["bcdef", "abcdefg", "bcdef", "bcdef","ayaz"]
# print(word_count(word_list))

# # Problem No 03
'''
You are given a positive integer. You can only use one for loop and one print
statement. Print a numerical triangle of height like the one below:
Input:
5
Output:
1
22
333
4444
'''
# var1 = int(input("Enter the number: ")) # First we take number as a int
# for i in range(1, var1): # then we iterate a loop
#     print(str(i) * i) # after that we cast this string same as "5" * 5

# Problem No 04
'''
You are given a string. Suppose a character ‘c’ occurs 4 times in the string. Replace
these consecutive occurrences of the character 'c' with (4, c) in the string.
Input format: A single line of input consisting of string s
Output format: A single line of output consisting of the modified string.
Input:
1222311
Output:
(1, 1) (3, 2) (1, 3) (2, 1)
'''
def string_manipulation(string):
    count = 1 # there's a variable called count that is initially set to 1.
    #for i in range(len(string)): "By doing this, our loop will go up to the last, 
    # but after the last, it won't find any character, 
    # which will cause it to throw an error."
    for i in range(len(string)-1): #A for loop starts, which goes through the characters in the input string one by one.
        if string[i] and string[i+1]: # If the current character is the same as the next one, it means they are consecutive and repeating
            count += 1 # we increase the count
            print("(",count,",",string[i],")",end=" ") # and print it
        else:
            print("(",count,",",string[i],")",end=" ") #in this case words are not repeating so we simply printing the word
            count = 1 # and setting count value to 1
    # to print last character we need to print out this using negative slicing
    print("(", count, ",", string[-1], ")")
str1 = "abbas"
string_manipulation(str1)

# Problem No 5

'''
You are given a N x M grid of strings. It consists of alphanumeric spaces and
characters, spaces, and symbols (!,@,#,$,%,&). To decode a string, you need to read
each column and select only alphanumeric characters and concatenate them. If there
are symbols between two alphanumeric characters of the decoded script, then
replace them with empty string ‘’. You need to do this without using the if condition.
Input:
7 3
Tsi
h%x
i #
sM
$a
#t%
ir!
Output
This is Matrix# %!'''
def decode_grid(grid):
    b = []
    c = []
    grid = list(zip(*grid))
    print(grid)
    for word in grid:
        for j in word:
            if j.isalpha():
                b.append(j)
            else:
                c.append(j)
    
    d =''.join(b)
    e = ''.join(c)    
    return f"{d} : {e}"
grid = [
    
    ["T", "s", "i"],
    ["h", "%", "x"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["i", "r", "!"]
]
# print(decode_grid(grid))

