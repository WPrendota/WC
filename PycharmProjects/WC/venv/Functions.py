import os

#Path to the script file:
script_path = os.path.dirname(os.path.realpath(__file__)) + "/"

#Function for lines counting:
def count_lines(arg):
    countLines = 0

    try:
        file = open(script_path + arg)
        print("Counting lines...")

        file = open(script_path + arg, 'r')

        file_data = file.read()

        lines = file_data.split("\n")

        file.close()

        print("Lines count:" + str(lines.__len__()))
    except IOError:
        print("Wrong file name or directory...")

#Function for characters counting:
def count_chars(arg):
    countChars = 0

    try:
        file = open(script_path + arg)
        print("Counting characters...")

        file = open(script_path + arg, 'r')

        file_data = file.read()

        file.close()

        print("Characters count:" + str(file_data.__len__()))
    except IOError:
        print("Wrong file name or directory...")

#Function for words counting:
def count_words(arg):
    countWords = 0

    try:
        file = open(script_path+arg)
        print("Counting words...")

        file = open(script_path + arg, 'r')

        file_data = file.read()

        words = file_data.split(" ")

        file.close()

        print("Words count:" + str(words.__len__()))
    except IOError:
        print("Wrong file name or directory...")
