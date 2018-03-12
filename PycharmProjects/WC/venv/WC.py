import argparse
import Functions

class WC:
    parser = argparse.ArgumentParser(description="WC - print newline, character and word counts.")
    parser.add_argument("-l", help="Print the newline counts. Input: text file name.")
    parser.add_argument("-m", help="Print the character counts. Input: text file name.")
    parser.add_argument("-w", help="Print the word counts. Input: text file name.")

    args = parser.parse_args()

    if args.l:
        Functions.count_lines(args.l)
    elif args.m:
        Functions.count_chars(args.m)
    elif args.w:
        Functions.count_words(args.w)