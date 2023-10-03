# Problem No 6
'''
You get an array of numbers, and return the sum of all of the positive ones. Example
[1, -4, 7, 12] => 1+7+12 = 20. If there is nothing to sum return 0. You can not use the
if statement.'''
def sum_positive_numbers(numbers):
    # first uses a for loop to iterate over the list of numbers. For each number in the list, the function checks if the number is positive. If the number is positive. the function adds it to a list called positive_numbers.
    return sum([num for num in numbers if num > 0])
# Test the function
input_array = [1, -4, 7, 12]
result = sum_positive_numbers(input_array)
print("Sum : ", result)  

# Problem No 7
'''
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest
element ( by value, not by index! ). You can not use the if statement.
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
'''
def sum_except_highest_lowest(numbers):
    return sum(sorted(numbers)[1:-1]) # First we use sorted function after that we slice it because we don't want first and last index
#[1:-1] means to select all elements starting from the second element (index 1) up to, but not including, the last element (index -1).

# # Test the function
array1 = [6, 2, 1, 8, 10] # 1,2,6,8,10
result1 = sum_except_highest_lowest(array1)
print(result1)  

# Problem No 8
'''
Our football team has finished the championship. Our team's match results are
recorded in a collection of strings. Each match is represented by a string in the
format x:y, where x is our team and y is our opponents score. The rules to calculate
score is
a. If x > y: 3 points
b. If x < y: 0 point
c. If x = y: 1 point
We need to write a function that takes this collection and returns the number of points
our team (x) got in the championship by the rules given above.
'''
def calculate_points(matches): #The code defines a function named calculate_points that takes a list of match result strings (like "2:1") as input.
    total_points = 0 #we create a variable named total_points to keep track of the total points our team earned.
    
    for match in matches:
        #the split() function is used to split the match result string into two parts: the team's score and the opponent's score.
        x_str,y_str = match.split(":") #it splits the result into our team's score (x_str) and the opponent's score (y_str).
        x = int(x_str) # then we convert it into int
        y = int(y_str)
        
        if x > y: # simply now we use condition
            total_points+=3 # and increment points in case of wins
        else:
            total_points +=1 # in case of tie we increment point with 1
    return total_points # and eventually we return total points 
matches = ["2:1", "1:1", "3:2", "4:0"] # we take list of total matches points 
team_points = calculate_points(matches) # we store it into a variable
print("Total points:", team_points)


# Problem No 9
'''
Complete the function that accepts a string parameter, and reverses each word in the
string. All spaces in the string should be retained.
"This is an example!" ==> "sihT si na !elpmaxe"
"double spaces" ==> "elbuod secaps" '''
def reverse_words(sentence):
    if len(sentence) == 1: #checks if the length of the input string is equal to 1. 
     return sentence # then The String
    else:
        # if the length of the string is up to one then
        return ' '.join([word[::-1] for word in sentence.split(' ')])
        # We divide the input sentence into separate words whenever we see a space. 
        # after that we reversed each words using [::-1 ] this notation basically reverse the order of the element
        # at last the function joins the reversed words back together into a new string using join function 
        # overall, the code splits the sentence into words, reverses each word, and then puts them back together with spaces in between. 
user_input = input("Enter the string : ")
res = reverse_words(user_input)
print('Result : ', res)
'''
You are going to be given a word. Your job is to return the middle character of the
word. If the word's length is odd, return the middle character. If the word's length is
even, return the middle 2 characters.
test => es
testing => t
A => A'''
def get_middle_character(word):
    # first we check if the length of the word is an even number.
    if len(word) % 2 == 0:
        return word[len(word)//2 - 1:len(word)//2 + 1] 
    else:
        return word[len(word)//2]

str1 = input("Enter the String : ")
result2 = get_middle_character(str1)
print("Remaning : ", result2)
print("Hello world")