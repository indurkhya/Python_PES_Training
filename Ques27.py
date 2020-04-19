# Write a program to check given string is Palindrome or not.That is reverse the given string
# and check whether it is same as original string, if so then it is palindrome.
# Example: String = "malayalam"  reverse string = "malayalam" hence given string
# is palindrome. Use built functions to check given string is palindrome or not.

def reverse_str(n):
    return n[::-1]


def palindrome(s):
    rev = reverse_str(s)

    if rev == s:
        print("Given string is palindrome: ", s)

    else:
        print("Given string is not palindrome: ", s)


palindrome("malayalfram")

