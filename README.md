# Assignment# Assignment
I have used Python 3.7.0 .<br>
To execute code user needs to have python 3.x installed in the system and he needs to save the .py file and the data file(.csv file) in the same directory.
While using CLI, he needs to navigate to the directory where the above are stored and simply run the code as per instructions provided.<br>
file name Q1 is solution of Permutations problem<br>
Discription:<br>
Permutations<br>
Goal: Create permutations of strings from a dynamic array of array, taking a single element from each array. <br>
Input: A CSV file, which can be loaded into an array of array. <br>
Expected output: Comma separated strings of all permutations <br>
Language: Any<br>
Input CSV file:<br>
Content of input.csv<br> 
‘a’, ‘b’, ‘c’<br>
‘i’, ‘j’<br>
‘x’, ‘y’<br>
Output strings:<br>
aix, aiy, ajx, ajy, bix, biy, bjx, bjy, cix, ciy, cjx, cjy<br>
Expected CLI Input<br>
./python Q1.py input.csv<br><br>

and Q3 is solution of Word suggestion problem<br>
Word Suggestion <br>
Goal: Given a list of words (say dictionary) in a csv file along with its frequency. Take a word as input and suggest five closest words from dictionary sorted in order of relevance. 
Assume that user is trying to type a dictionary word which they misspelled, and you have to suggest the correct word. <br>
Language: Any<br>
Example Input file:<br> 
Content of dictionary.csv <br>
Hello, 300<br>
World, 50<br>
Hi, 600<br>
How, 500<br>
Are, 900<br>
You, 200<br>
Expected CLI Input:<br>
./python Q3.py dictionary.csv hellp<br> 
Hello, word2, word3, word4, word5<br>
