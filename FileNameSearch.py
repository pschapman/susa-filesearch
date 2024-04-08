'''
Build a program which will find filenames in a folder/directory structure based
on user input. Program must present a menu of files matching the search
criteria and display the contents of a user selected file.

Judges will provide a folder structure and generic text files for testing.

Python 3.10 needed for "switch...case" feature
Python 3.12 needed to identify Windows junctions.
'''

import argparse
import os
import sys
import time

if sys.version_info < (3, 12) and os.name == 'nt':
    print("Python 3.12 or later required to detect Windows junctions.")
    sys.exit()

def main():
    '''
    Core program logic
    '''
    # argparse module will provide auto-generated help for user when
    # --help specified on CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument('--path',
                        help="Base folder path for search.")
    parser.add_argument('--search',
                        help="Whole or partial file name.")
    parser.add_argument('--depth',
                        help="Search depth. >= -1 (-1 default)",
                        default=-1)
    args = parser.parse_args()

    # Use parameters from CLI if present, otherwise ask user.
    path = prompt_path(args.path)
    search = prompt_search(args.search)

    # Get initial results before going to User Menu
    file_list = run_search(path, search, args.depth)
    # print(file_list)
    user_menu(file_list, path, search, args.depth)


def user_menu(file_list, path, search, max_depth):
    '''
    User menu system. Run search if params collected from CLI, otherwise
    prompt as needed.
    '''
    user_done = None

    # Main loop to keep script running.
    while not user_done:
        list_text = ''
        file_list = run_search(path, search, max_depth)
        for item in file_list:
            list_text += f"\n\t{item}"

        main_menu = f'''
                PROGRAM SETTINGS
    Search Path: {path}
    Search Term: {search}
    Depth: {max_depth}

                SEARCH RESULTS{list_text}

                MAIN MENU

    P) Change Search Path
    S) Change Search Term
    D) Change Search Depth
    V) View File Content
    Q) Quit & Exit Program
'''

        print(main_menu)
        selection = input("Make Selection: ")
        match selection.lower():
            case 'p':
                path = prompt_path(None)
            case 's':
                search = prompt_search(None)
            case 'd':
                max_depth = prompt_depth(None)
            case 'v':
                view_contents(file_list)
            case 'q':
                user_done = True
            case _:
                print(f"{selection} is invalid. Try again.")
                time.sleep(3)

def view_contents(file_list):
    '''
    Provide menu to user. Read selected file.
    '''
    item_menu = ''
    for i, val in enumerate(file_list):
        item_menu += f"{i}) {val}\n"

    print(item_menu)
    selection = input("\nInput # to view item or any key to return to Main: ")
    if selection.isnumeric():
        # open file and print contents
        with open(file_list[int(selection)], 'r', encoding='utf-8') as file:
            print(file.read())
        input("\n\nHit any key to return to Main Menu")

def prompt_path(path):
    '''
    Get path string from user. Validate input.
    '''
    while not path:
        path = input("Enter base search folder: ")

        # Remove quotes from string if passed by user.
        path = path.replace('"', '').replace("'", '') if path else None

        if not os.path.exists(path):
            path = None
            print ("Requested path not found. Try again.")

    return path

def prompt_search(search):
    '''
    Get search string from user.
    '''
    while not search:
        search = input("Enter filename search term: ")
        if not search:
            print ("Empty search not allowed. Try again")

    return search

def prompt_depth(depth):
    '''
    Get search string from user.
    '''
    depth = input("Enter search depth (default = -1): ")
    # Set default if no input from user
    if not depth:
        depth = -1
    else:
        try:
            depth = int(depth)
        except ValueError:
            print("Non-numeric value entered. Setting depth to -1.")
            depth = -1
            time.sleep(3)

    return depth

def run_search(path, search, max_depth, curr_depth=0):
    '''
    Recursive function to search folders for whole / partial file names.
    '''
    found_list = []
    # Get directory object and iterate contents
    with os.scandir(path) as item:
        for entry in item:
            if entry.is_file():
                # Add file path to list if it matches search term
                if search in entry.path:
                    found_list.append(entry.path)
            elif not entry.is_symlink() and not entry.is_junction():
                # Increment depth counter and recurse if permitted.
                curr_depth += 1
                if curr_depth < max_depth or max_depth == -1:
                    more_paths = run_search(entry.path, search, max_depth,
                                            curr_depth)
                    if more_paths:
                        found_list.extend(more_paths)

    return found_list

if __name__ == "__main__":
    main()
