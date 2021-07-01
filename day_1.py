import fileinput

# To avoid repetition, it is possible to create the list variable containing lines from the txt file.
directory = 'input.txt'

def part_1():
    frequency = 0 
    for line in fileinput.input(files = directory):
        frequency += int(line.strip())
        # Can be shortened by using Python one-liner: map() and sum() functions
        # ex) sum(map(int, fileinput.input(files = directory)))
    return frequency

def part_2():
    frequency = 0
    # {} confusingly creates an empty dictionary (hash array), NOT a set;
    # Initialize with the values(s) in it, or just use set() to create an empty set. 
    frequencies_checked = set()

    while True:
        for line in fileinput.input(files = directory):
            frequency += int(line.strip())

            # The loop breaks if the condition below is True
            if frequency in frequencies_checked:
                return frequency

            frequencies_checked.add(frequency)

print(part_1())
print(part_2())
    
    



