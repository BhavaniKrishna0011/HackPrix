import os

def print_hierarchy(directory, indent=0):
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isfile(path):
            print('  ' * indent + '|--', item)
        elif os.path.isdir(path):
            print('  ' * indent + '|--', item)
            print_hierarchy(path, indent+1)

# Replace 'path_to_your_directory' with the path to the directory you want to print
print_hierarchy('../Hackathin')
