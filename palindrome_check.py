s = input("Enter a string: ")

# Remove spaces and convert to lowercase
cleaned_s = s.replace(" ", "").lower()

# Check if the cleaned string is a palindrome using slicing
if cleaned_s == cleaned_s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")