def most_frequent(input_string):
    char_frequency = {}

    for char in input_string:
        if char.isalpha():
            char = char.lower()
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

    sorted_chars = sorted(char_frequency.items(), key=lambda x: x[1], reverse=True)

    for char, frequency in sorted_chars:
        print(f"{char} = {frequency:02}")

input_string = input("Please enter a string: ")
most_frequent(input_string)