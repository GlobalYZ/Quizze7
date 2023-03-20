"""
Nicole Hsu
Muyang Li
"""


def replace_all(input_file, output_file, search, replace):
    """


    :param input_file:
    :param output_file:
    :param search:
    :param replace:
    :return:
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

if __name__ == "__main__":
    main()
