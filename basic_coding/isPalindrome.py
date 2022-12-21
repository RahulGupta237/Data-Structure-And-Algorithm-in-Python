#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# isPalindrome Solution

s="r"
x=list(s[1:-1])
print(x)
def isPalindrome(strng):
    print(strng)
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng)-1]:
        return False
    return isPalindrome(strng[1:-1])

print(isPalindrome('awesome')) # false
print(isPalindrome('foobar')) # false
print(isPalindrome('tacocat')) # true
print(isPalindrome('amanaplanacanalpanama')) # true
print(isPalindrome('amanaplanacanalpandemonium')) # false