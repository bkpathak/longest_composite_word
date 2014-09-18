The program finds the composite words (words composed of other words).It prints the first and second longest such words and total number of such words present in the file.

##### Program Implementation

The words are read from file one at at a time and dictionary is created as words are read.The key of the dictionary is word itself and values are set as none.Once the file is read, each word is checked to see whether it is composite or not.

To check whether the word is composite or not **Dynamic Programming** is used since while breaking the word it exhibits the overlapping sub-problems.The __word_break() functions returns boolean value of either each word is composite or not with updating separate dictionary for memoization. The memoization sppeds up the process while checking for words which exhibits the overlapping sub-problem.The __value_update function updates the value accordingly when the composite word is found.

##### 