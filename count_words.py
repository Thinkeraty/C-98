def count_words():
    file_name = input("Enter the name of the file: ")
    file = open(file_name, 'r')

    number_of_words = 0

    for line in file:
        words = line.split()
        number_of_words = number_of_words + len(words)
    
    print(number_of_words)

count_words()
