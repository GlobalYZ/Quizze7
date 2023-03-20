"""
Nicole Hsu
Muyang Li
"""


def replace_all(input_file, output_file, search, replace):
    """
    Replace all given search word with the replaced word in the given input file.

    Generate the output content into the given output file.

    :param input_file: a string to indicate the input file name
    :param output_file: a string to indicate the output file name
    :param search: a string that needs to be replaced
    :param replace: a string that needs to replace the search parameter
    :precondition: the input file that input_file parameter points to can not be empty
    :precondition: the output file the input_file parameter points to must be empty before the function is called
    :postcondition: the content with all given search word replaced correctly, generated to the defined output file
    :postcondition: returns the correct number of replacements
    :return: number of times the searched word is replaced, as an integer
    """
    with open(input_file) as file_object_input:
        new_file = file_object_input.read()
    replace_count = new_file.count(search)
    new_file = new_file.replace(search, replace)
    with open(output_file, "w") as file_object_output:
        file_object_output.write(new_file)
    return replace_count


def main():
    """
    Drives the program.
    """
    print("Welcome to Quiz 7!")
    input_file_name = input("Enter the name of the input file: ")
    output_file_name = input("Enter the name of the output file: ")
    search_for = input("Enter the word to search for: ")
    replace_with = input("Enter the replacement word: ")

    count_replaced = str(replace_all(input_file_name, output_file_name, search_for, replace_with))
    print("Successfully replaced " + count_replaced + " occurances of '" + search_for + "'")


if __name__ == "__main__":
    main()
