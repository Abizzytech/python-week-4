def file_read_write():
    # Ask the user for the input file name
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening and reading the file
        with open(filename, "r") as infile:
            content = infile.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Create a new filename for the output
        new_filename = "modified_" + filename

        # Write the modified content to a new file
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to '{new_filename}'")