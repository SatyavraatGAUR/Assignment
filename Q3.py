import sys
import operator
import pandas
word_frequency = {}
list_of_words = []
with open("dictionary.csv") as datafile:
    for each_row in datafile:
        word, frequency = each_row.split(',') #dividing it into word and frequency of occurence
        word_frequency[word] = int(frequency.strip()) # inserting into the wordcount dictionary key as word and value as frequency
        list_of_words.append(word) #inserting only the word in words

#Search function to search for the word in any word of words list.
def search(partial):
    search_results = []
    for item in list_of_words:
        if partial in item:
            search_results.append(item) 
    return search_results		

#this function is used to find out the edit distance between two strings 
def editDistance(str1, str2, m , n): 
  
    # If first string is empty, the only option is to 
    # insert all characters of second string into first 
    if m==0: 
         return n 
  
    # If second string is empty, the only option is to 
    # remove all characters of first string 
    if n==0: 
        return m 
  
    # If last characters of two strings are same, nothing 
    # much to do. Ignore last characters and get count for 
    # remaining strings. 
    if str1[m-1]==str2[n-1]: 
        return editDistance(str1,str2,m-1,n-1) 
  
    # If last characters are not same, consider all three 
    # operations on last character of first string, recursively 
    # compute minimum cost for all three operations and take 
    # minimum of three values. 
    return 1 + min(editDistance(str1, str2, m, n-1), editDistance(str1, str2, m-1, n),editDistance(str1, str2, m-1, n-1))



#putting priority in the resultant list of words
def prioritizing(search_results, partial):
    priority=[]
    for item in search_results:
        priority.append([item,item.find(partial),word_frequency[item],len(item)]) #creating a list of lists with words containing the partial word and their frequency, starting index and length 
    priority.sort(key=operator.itemgetter(1)) #sorting based on starting index
    priority.sort(key=operator.itemgetter(3)) #sorting based on length
    refined_search_results=[]
    count=0
    for item in priority:
        if(count<5):
            refined_search_results.append(item[0])
            count+=1
    return refined_search_results
l=search((sys.argv)[2])
valed={}
if l ==[]:	#This indicates that the word given as input is not present in any of the words in list of words given
    blank={}
    for item in list_of_words: #this returns a dictionary of words with their edit distance with the word given as input
        val=editDistance(sys.argv[2],item,len(sys.argv[2]),len(item))
        valed[item]=val
    blank=dict(sorted(valed.items(), key = lambda kv:(kv[1]))) 		#this create a dictionary which is sorted along its values i.e the edit distance	
    #print(list(blank.keys()),type(blank.keys()))
    l=list(blank.keys())
    l=l[:5]   #the list of top 5 closely matching words
else:
    l=prioritizing(search((sys.argv)[2]),sys.argv[2])
print(*l,sep=', ')