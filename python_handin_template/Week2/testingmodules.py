from utils import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('path', help='The path where the file is')
    parser.add_argument('--file', help='Name of the file you want to print')
    
    args = parser.parse_args()
    
    #get_file_names(args.path, args.file)
    #print_line_one(args.path)
    #get_all_file_names(args.path, args.file)
    #print_emails(args.path)
    write_headlines(args.path, args.file)
    print(args.path)
    print(args.file)