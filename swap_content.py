def swap_content():
    file_one = input("Enter the name of the first file: ")
    file_two = input("Enter the name of the second file: ")

    with open(file_one, 'r') as first:
        data_one = first.read()
    
    with open(file_two, 'r') as second:
        data_two = second.read()
    
    with open(file_one, 'w') as first:
        first.write(data_two)

    with open(file_two, 'w') as second:
        second.write(data_one)

swap_content()
