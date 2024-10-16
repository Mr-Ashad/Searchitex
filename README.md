# Searchitex
**A text searcher for Pdf, Csv, Text files**
#### Project Video Demo URL: https://youtu.be/3BNO2dgrMfU?feature=shared

### Description:
This project takes search text input from the user and searches it inside the type of file selected by the user.

This program displays a menu of operations which are

1. Pdf Search
2. Csv Search
3. Text Search
4. Exit Program

### Functions
This programs consists for four functions :

1. main
2. check_input
3. pdf_search
4. csv_search
5. txt_search

1.main : The main function handles the menu part and calls the respective functions based on the user's choice. It exits the program after three wrong attempts.

2.check_input : This function asks for file name of the respective type of file and text to search ,it exits  after 3 wrong attempts with either wrong extension or less than one character to search

2.pdf_search : This function searchs the pdf file given by the input of user and displays a progress bar and outputs the page number of the text is found inside the pdf or displays a message

3.csv_search : This function searchs inside the csv file given as input from user and displays a progress bar indicating the proccess of search and displays the column number if the given text is a column name or displays the row number and column name if the given test is a row under first column.

4.txt_search : This function takes a filename as parameter and text to search  it also displays a progress bar and gives the search result as line number in which the given text is found.
