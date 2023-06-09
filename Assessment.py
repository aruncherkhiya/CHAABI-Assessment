#CHAABI Assessment Question & Answers


#######################################################################################

Q1. Get your basics right -

 Implement selection sort algorithm in python. The function accepts a
list in the input and returns a sorted list.
E.g.
Input f1([5,416,54,21,6135,15,741]) should
Return [5, 15, 21, 54, 416, 741, 6135]

SOLUTION:-

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted part of the list
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Test the function
input_list = [5, 416, 54, 21, 6135, 15, 741]
sorted_list = selection_sort(input_list)
print(sorted_list)



########################################################################################


Q2. Dictionary, what?

Write a program that returns the file type from a file name. The type of the file is determined
from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
png,image) will be input.
The program takes input in the following form:
1. Input extension and type values in the form of a string having the following format:
a. "extension1,type1;extension2,type2;extension3,type3"
b. E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
2. Input a list of filename.extension. E.g. an input list could be something like ["abc.html",
"xyz.xls", "text.csv", "123"]
The program should return a dict of filename: type pairs
E.g.
f("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg",
"xyz.xls", "text.csv", "123"]) should return
{
"abc.jpg": "image",
"xyz.xls": "spreadsheet",
"Text.csv": "unknown",
"123": "unknown"
}

SOLUTION:-

def get_file_type(extension_type_list, filenames):
    extension_type_pairs = extension_type_list.split(';')
    extension_type_dict = {}

    for pair in extension_type_pairs:
        extension, file_type = pair.split(',')
        extension_type_dict[extension] = file_type

    result_dict = {}
    for filename in filenames:
        file_extension = filename.split('.')[-1]
        file_type = extension_type_dict.get(file_extension, 'unknown')
        result_dict[filename] = file_type

    return result_dict


# Test the function
extension_type_list = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]
result = get_file_type(extension_type_list, filenames)
print(result)



################################################################################################



Q3. Column Sorting, yay!

Given a list of dicts, write a program to sort the list according to a key given in input.
E.g.
Input f([
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
], "fruit")
Should Output
[
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"},
{"fruit": "orange", "color": "orange"}
]
AND
Input f([
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
], "color")
Should Output
[
{"fruit": "blueberry", "color": "blue"},
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"}
]

SOLUTION:-

def sort_list_of_dicts(lst, key):
    sorted_list = sorted(lst, key=lambda x: x[key])
    return sorted_list


# Test the function
input_list = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sorted_list_by_fruit = sort_list_of_dicts(input_list, "fruit")
print(sorted_list_by_fruit)

sorted_list_by_color = sort_list_of_dicts(input_list, "color")
print(sorted_list_by_color)



############################################################################################


Q4. The power of one line -

Given a dictionary, switch position of key and values in the dict, i.e., value becomes the key and
key becomes value. The function's body shouldn't have more than one statement.
f({
"key1": "value1",
"key2": "value2",
"key3": "value3",
"key4": "value4",
"key5": "value5"
}) should return
{
"value1": "key1",
"value2": "key2",
"value3": "key3",
"value4": "key4",
"value5": "key5"
}

SOLUTION:-

def switch_key_value(dictionary):
    return {value: key for key, value in dictionary.items()}

# Test the function
input_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

result = switch_key_value(input_dict)
print(result)


#########################################################################################


Q5. Common, Not Common

Given 2 lists in input. Write a program to return the elements, which are common to both
lists(set intersection) and those which are not common(set symmetric difference) between the
lists.
Input:
Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword
Art Online","Bleach","Dragon Ball Z","One Piece"]
must_watch = ["Full Metal Alchemist","Code Geass","Death
Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack
On Titan"]
f(mainstream, must_watch) should return:
["One Piece", "Attack On Titan"], ["Dragon Ball Z", "Death Note",
"One Punch Man", "Stein's Gate", "The Devil is a Part Timer!", "Sword
Art Online","Full Metal Alchemist","'Bleach", "Code Geass"]

SOLUTION:-

def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    non_common_elements = list(set(list1) ^ set(list2))
    return common_elements, non_common_elements

# Test the function
mainstream = [
    "One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online",
    "Bleach", "Dragon Ball Z", "One Piece"
]
must_watch = [
    "Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate",
    "The Devil is a Part Timer!", "One Piece", "Attack On Titan"
]

common, non_common = compare_lists(mainstream, must_watch)
print(common)
print(non_common)


#######################################################################################


Q6. Every other sub-list

Given a list and 2 indices as input, return the sub-list enclosed within these 2 indices. It should
contain every second element.
E.g.
Input f([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9)
Return [5, 11, 17, 23]

SOLUTION:-

def get_sublist_with_every_other_element(lst, start_index, end_index):
    sub_list = lst[start_index+1:end_index:2]
    return sub_list

# Test the function
input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

result = get_sublist_with_every_other_element(input_list, start_index, end_index)
print(result)


########################################################################################


Q7. Calculate the factorial of a number using lambda function.

SOLUTION:-

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Test the lambda function
number = 5
result = factorial(number)
print(result)


########################################################################################


Q8. Some neat tricks up her sleeve:

Looking at the below code, write down the final values of A0, A1, ...An
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
A8 = map(lambda x: x*2, [1,2,3,4])
A9 = filter(lambda x: len(x) >3, [“I” , “want”, “to”, “learn”, “python”])


SOLUTION:-

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))

A1 = range(10)

A2 = sorted([i for i in A1 if i in A0])

A3 = sorted([A0[s] for s in A0])

A4 = [i for i in A1 if i in A3]

A5 = {i: i*i for i in A1}

A6 = [[i, i*i] for i in A1]

from functools import reduce
A7 = reduce(lambda x, y: x + y, [10, 23, -45, 33])

A8 = map(lambda x: x*2, [1, 2, 3, 4])

#####################################################################################

Q9.
Write a func that takes 3 args:
from_date - string representing a date in the form of 'yy-mm-dd'
to_date - string representing a date in the form of 'yy-mm-dd'
difference - int
Returns True if from_date and to_date are less than difference days away from each other, else
returns False.

SOLUTION:-from datetime import datetime, timedelta

def is_date_difference_less(from_date, to_date, difference):
    # Convert string dates to datetime objects
    from_datetime = datetime.strptime(from_date, '%y-%m-%d')
    to_datetime = datetime.strptime(to_date, '%y-%m-%d')
    
    # Calculate the difference in days
    date_difference = abs((to_datetime - from_datetime).days)
    
    # Check if the difference is less than the given number of days
    if date_difference < difference:
        return True
    else:
        return False

# Test the function
from_date = '21-05-01'
to_date = '21-05-10'
difference = 10
result = is_date_difference_less(from_date, to_date, difference)
print(result)

#########################################################################################

Q10. Of date and days

Write a func that takes 2 args:
date - string representing a date in the form of 'yy-mm-dd'
n - integer
Returns the string representation of date n days before 'date'
E.g. f('16-12-10', 11) should return '16-11-29'

SOLUTION:-from datetime import datetime, timedelta

def get_date_before(date, n):
    # Convert string date to datetime object
    date_obj = datetime.strptime(date, '%y-%m-%d')
    
    # Calculate the date before
    date_before = date_obj - timedelta(days=n)
    
    # Format and return the date as string
    return date_before.strftime('%y-%m-%d')

# Test the function
date = '16-12-10'
n = 11
result = get_date_before(date, n)
print(result)


########################################################################################

Q11. Something fishy there -

Find output of following:
def f(x,l=[]):
for i in range(x):
l.append(i*i)
print(l)
f(2)
f(3,[3,2,1])
f(3)

SOLUTION:-
[0, 1]
[3, 2, 1, 0, 1, 4]
[0, 1, 4, 0, 1, 4]
