import fileinput
from collections import Counter

lines = [x.strip() for x in fileinput.input(files = 'input.txt')] 

def part_1():
    two_counter = 0 
    three_counter = 0 
    for line in lines:
        # Counter returns a dictionary containing keys and counts
        # values() returns a list of all the values available in a given dictionary.
        charCounter = Counter(line).values()
        if 2 in charCounter:
            two_counter += 1
        if 3 in charCounter:
            three_counter += 1
    print(two_counter * three_counter)
    
def part_2():
    # Collects the commonString and its appearance count
    dict = {} 
    
    # Need to check all other lines for each line: Nested Loops 
    # This should be modified if the actual apperance count is asked.
    for line1 in lines:
        diffSum = 0
        commonStr = ""
        for line2 in lines:
            diffCounter = 0
            for i in range(len(line1)):
                if line1[i] != line2[i]:
                    diffCounter += 1
            # Check two strings are differed by a single character
            if diffCounter == 1:
                diffSum += 1
                # This part can be improved to avoid reptition 
                for i in range(len(line1)):
                    if line1[i] != line2[i]:
                        # To avoid repetition of assigning same string
                        if not commonStr:
                            commonStr = line1[0 : i : ] + line1[i+1 : : ]
        # Check if commonStr is not empty
        if commonStr:
            # Assign the common string and its appearance count to the dictionary
            dict[commonStr] = diffSum
            
    # Print the common string with the highest appearance
    print(max(dict, key = dict.get))
    
part_1()     
part_2()
