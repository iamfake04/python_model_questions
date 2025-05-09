def list_of_frequency(s):
    # Create a dictionary to store the frequency of each character
    frequency = {}
    
    # Count the frequency of each character in the string
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Sort the dictionary by frequency in non-increasing order
    sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    
    # Print the characters in non-increasing order of frequency
    for char, freq in sorted_frequency:
        print(f"'{char}': {freq}")

# Example usage
input_string = input("Enter a string: ")
list_of_frequency(input_string)