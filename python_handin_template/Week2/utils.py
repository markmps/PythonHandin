import os

def get_file_names(folderpath, out):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    with open(out, 'w') as file_object:
        for files in os.listdir(folderpath):
            file_object.write(files+"\n")
            
            
def get_all_file_names(folderpath, out):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    with open(out, 'w') as file_object:
        for root, subdirs, files in os.walk("."):
            for filesname in files:
                file_object.write(filesname+"\n")
                
                
def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    with open(file_names, 'r') as file_object:
            print(file_object.readline())
            

def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    with open(file_names, 'r') as file_object:
        lines = file_object.readlines()
        for line in lines:
            if '@' in line:
                print(line)
                
                
def write_headlines(md_files, out):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    with open (out, 'w') as md_writer:
        with open (md_files, 'r') as md_reader:
            for lines in md_reader:
                if lines.startswith('#'):
                    md_writer.write(lines+"\n")
                    print(lines)