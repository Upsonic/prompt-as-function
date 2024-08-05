import os




def generate_file_tree_(path, indent):

    # Prefix for each line (based on depth)
    prefix = '|  ' * (indent - 1) + '|--' if indent > 0 else ''
    
    tree_str = prefix + os.path.basename(path) + '\n'  # Add current directory/file to the string
    
    if os.path.isdir(path):  # If path is a directory, explore it
        for item in os.listdir(path):
            item_path = os.path.join(path, item)

            # Recursively generate the tree for each item, increasing the indent by 1
            tree_str += generate_file_tree_(item_path, indent + 1)
            
    return tree_str



def generate_file_tree():
    """
    Generate a file tree for a directory.

    Returns:
    A string forming a tree structure of the directory and its files.
    """
    path = "." 
    indent = 0
    # Prefix for each line (based on depth)
    prefix = '|  ' * (indent - 1) + '|--' if indent > 0 else ''
    
    tree_str = prefix + os.path.basename(path) + '\n'  # Add current directory/file to the string
    
    if os.path.isdir(path):  # If path is a directory, explore it
        for item in os.listdir(path):
            item_path = os.path.join(path, item)

            # Recursively generate the tree for each item, increasing the indent by 1
            tree_str += generate_file_tree_(item_path, indent + 1)
            
    return tree_str