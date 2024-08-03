def isPalindrome(self, x: int) -> bool:
    convert_to_string = str(x)
    return convert_to_string == convert_to_string[::-1]
