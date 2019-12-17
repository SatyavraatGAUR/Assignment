# Assignment
I have used Python 3.7.0 .
To execute code user needs to have python 3.x installed in the system and he needs to save the .py file and the data file(.csv file) in the same directory.
While using CLI, he needs to navigate to the directory where the above are stored and simply run the code as per instructions provided.
file name Q1 is solution of Permutations problem
Discription:
Permutations
Goal: Create permutations of strings from a dynamic array of array, taking a single element from each array. 
Input: A CSV file, which can be loaded into an array of array. 
Expected output: Comma separated strings of all permutations 
Language: Any
Input CSV file:
Content of input.csv 
‘a’, ‘b’, ‘c’
‘i’, ‘j’
‘x’, ‘y’
Output strings:
aix, aiy, ajx, ajy, bix, biy, bjx, bjy, cix, ciy, cjx, cjy
Expected CLI Input
./python Q1.py input.csv

and Q3 is solution of Word suggestion problem
Word Suggestion 
Goal: Given a list of words (say dictionary) in a csv file along with its frequency. Take a word as input and suggest five closest words from dictionary sorted in order of relevance. 
Assume that user is trying to type a dictionary word which they misspelled, and you have to suggest the correct word. 
Language: Any
Example Input file: 
Content of dictionary.csv 
Hello, 300
World, 50
Hi, 600
How, 500
Are, 900
You, 200
Expected CLI Input:
> ./python Q3.py dictionary.csv hellp 
Hello, word2, word3, word4, word5
