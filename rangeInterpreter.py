'''
Build a function named rangeInterpreter, which will accept one input:
    A string which is a comma and/or hyphen-separated range description.

A comma in the input separates individual numbers or groups of numbers. A
hyphen indicates a range of numbers within a comma group (e.g., 1-3 = 1,2,3).
Expansion of a hyphenated group should only include integers between the first
and last number of the range.
'''

def main():
    '''
    Simple main wrapper to execute test cases.
    '''
    # Extensible sample case list.
    sample_io = {
        "1,2,3,5": [1,2,3,5],
        "1,2,3.14,b": [1,2,3],
        "1,2,6-12": [1,2,6,7,8,9,10,11,12],
        "4,8-11,6-9,4": [4,6,7,8,9,10,11],
        "1-3,0,-2-1,-3--2": [-3,-2,-1,0,1,2,3]
    }
    # Iterate sample cases and provide friendly output.
    for i, key in enumerate(sample_io):
        print(f"Test Case: {i+1}")
        output = rangeInterpreter(key)
        if output == sample_io[key]:
            print(f"Success: {output}")
        else:
            print(f"Failed: {output}\nCorrect: {sample_io[key]}")

def rangeInterpreter(user_input): #pylint: disable=invalid-name
    '''
    Main code logic. Take string input and output array (or language
    equivalent).
    '''
    return_list = []
    for segment in user_input.split(','):
        # Handle negative last number
        if segment.find('--') > 1:
            last_num = segment[segment.find('--')+1:]
        else:
            last_num = segment.split("-")[-1]

        # Extract first number from known last number string
        first_num = segment.replace(f"-{last_num}", '')

        # Validate characters are numbers and drop fractions
        try:
            first_int = int(float(first_num))
        except ValueError:
            first_int = None
            print(f"Discarding bad input, '{first_num}'")
        try:
            last_int = int(float(last_num))
        except ValueError:
            last_int = None
            print(f"Discarding bad input, '{last_num}'")

        # Process single digits, ranges and invalid inputs.
        if first_int == last_int:
            new_range = [first_int]
        elif first_int < last_int:
            new_range = range(first_int,last_int+1, 1)
        else:
            new_range = []
            print("Discarding range. Last number greater than first.")

        return_list.extend(new_range)

    # Remove remove duplicates from list
    return_list = list(set(return_list))
    # Remove null value from list if present
    if None in return_list:
        return_list.remove(None)

    # Return sorted data
    return sorted(return_list)

if __name__ == "__main__":
    main()
