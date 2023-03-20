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
    with open(input_file) as file_object:
        new_file = file_object.read()
    print(new_file)

def main():
    """
    Drives the program.
    """


if __name__ == "__main__":
    main()
