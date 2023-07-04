def is_palindrome(input_string):
    left = 0
    right = len(input_string) - 1

    while left < right:
        # Skip non-alphabetic characters on the left.
        while left < right and not input_string[left].isalpha():
            left += 1

        # Skip non-alphabetic characters on the right.
        while left < right and not input_string[right].isalpha():
            right -= 1

        # If the characters don't match, it's not a palindrome.
        if input_string[left].lower() != input_string[right].lower():
            return False

        # Move the pointers towards the center.
        left += 1
        right -= 1

    return True

print("***** Palindrome Checker *****")
input_string = input("\nEnter a word or sentence: ")
if is_palindrome(input_string):
    print(f"\n'{input_string.capitalize()}' is a palindrome.")
else:
    print(f"\n'{input_string.capitalize()}' is not a palindrome.")