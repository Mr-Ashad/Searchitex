# Project Name : Searchitex
# Author : Mahammad Ashad
# Github username : Mr-Ashad


import pypdf
import pandas as pd
import re
from tabulate import tabulate
import sys
from tqdm import tqdm


# Main Code
def main():
    attempts = 1
    headers = ["Options", "Operations"]
    operations = [
        ["a", "Pdf file Search"],
        ["b", "Csv file Search"],
        ["c", "Text file Search"],
        ["d", "Exit"],
    ]
    while True:
        # Exits program after three wrong attempts
        if attempts > 3:
            sys.exit("Too many wrong attempts program aborted")

        # Printing the menu of operations
        print(tabulate(operations, headers, tablefmt="grid"))

        if attempts > 1:
            print("Enter the correct option")
        choice = input("Enter your choice [a,b,c,d]: ")

        # Pdf Search
        if choice == "a":
            Type = ".pdf"
            file_name, search_text = check_input(Type)
            print(pdf_search(file_name, search_text))
            break

        # Csv Search
        elif choice == "b":
            Type = ".csv"
            file_name, search_text = check_input(Type)
            print(csv_search(file_name, search_text))
            break

        # Text Search
        elif choice == "c":
            Type = ".txt"
            file_name, search_text = check_input(Type)
            print(txt_search(file_name, search_text))
            break

        # Exit Program
        elif choice == "d":
            sys.exit("Program Aborted")
        else:
            attempts += 1


# Function to accept file name and text to search


def check_input(Type):
    # Checks for errors in input
    attempts = 1
    try:
     while True:
            file_name = input("Filename(with extension): ")
            if file_name.endswith(Type) and len(file_name) > 3:
                break
            else:
                attempts += 1
                if attempts > 1:
                    print(f"Enter a valid {Type} file")
                if attempts > 3:
                    raise ValueError
     prompt = 1
     while True:
                search_text = input("Enter the text you want to search: ")
                if len(search_text) > 0:
                    return file_name,search_text
                else:
                    print("Enter at least one character")
                    prompt += 1
                    if prompt > 3:
                        raise ValueError
    except ValueError:
            sys.exit("Too many wrong attempts")



# Function to perform the search on pdf


def pdf_search(pdf_file, search_text):
    try:
        with open(pdf_file, "rb") as pdf_obj:
            pdf_reader = pypdf.PdfReader(pdf_obj)
            found_page = []
            print("---------------------------------------------------------------")
            print(f"Searching '{search_text}' in {pdf_file}")
            for i, page in enumerate(tqdm(pdf_reader.pages)):
                text = page.extract_text()
                if match := re.search(rf"\b{search_text}\b", text, re.IGNORECASE):
                    found_page.append(i + 1)
            print("---------------------------------------------------------------")
            if found_page:
                return(f"Search Result: '{search_text}' found at Page number: {found_page}")
            else:
                return(f"Search Result: '{search_text}' not found in {pdf_file}")
                #print("---------------------------------------------------------------")
    except FileNotFoundError:
        sys.exit(f"{pdf_file} file not found")
    except pypdf.errors.PdfReadError as e:
        sys.exit(f"Error reading PDF: {e}")
    except re.error:
        sys.exit("Entered search text is not valid ")
# Function for searching inside csv file

def csv_search(csv_file, search_text):
    # Initializing pandas object
    try:
        data = pd.read_csv(csv_file)
    except FileNotFoundError:
        sys.exit(f" {csv_file} file not found")

    # Searching inside columns of csv file
    columns = list(data.columns)
    found_column = 0
    flag = False
    print("------------------------------------------------------------------------")
    print(f"Searching {search_text} in columns of {csv_file}:")
    for i,col in enumerate(tqdm(columns,total=len(columns))):
        if col == search_text:
            found_column=i+1

    if found_column > 0:
            print("--------------------------------------------------------------------")
            return(f"Search Result: '{search_text}' is a column name at column number {found_column}")
            #print("---------------------------------------------------------------------")
            #sys.exit()

    # Searching inside rows
    result_row_num = []
    result_columns = []
    print("---------------------------------------------------------------------")
    print(f"Searching {search_text} in rows of {csv_file}")

    # Looping rows in csv file
    for i, row in tqdm(data.iterrows(),total=len(data)):
        for col in columns:
            if row[col] == search_text:
                result_row_num.append(i)
                result_columns.append(row.index[row.values == search_text][0])

    # Checks for results and prints it
    print("---------------------------------------------------------------------")
    if result_row_num:
        for m, n in zip(result_row_num, result_columns):
            return(f"Search Result: {search_text} found at Row number :{m} \nColumn Name :{n}")

    else:
        return(f"Search Result: {search_text} not found in {csv_file}")
    print("---------------------------------------------------------------------")

# Function to search in txt file

def txt_search(txt_file, search_text):
    try:
        with open(txt_file) as text_file:
            text_file = open(txt_file, "r")
            lines = text_file.readlines()
            res_line_no = []
            print("--------------------------------------------------------------")
            print(f"Searching {search_text} in {txt_file}")
            for i, line in enumerate(tqdm(lines)):
                if match := re.search(rf"\b{search_text}\b", line, re.IGNORECASE):
                    res_line_no.append(i)

            # Printing Results
            print("--------------------------------------------------------------")
            if res_line_no:
                return(f"Search Result: '{search_text}' found at line number {res_line_no}")
            # Executes when no match is found
            else:
                return(f"Search Result: '{search_text}' not found in {txt_file}")
                print("---------------------------------------------------------------------")
    except FileNotFoundError:
        sys.exit(f"{txt_file} file not found")
    except re.error:
        sys.exit("Entered search text is not valid")
if __name__ == "__main__":
    main()
