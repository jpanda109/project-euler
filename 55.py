def reverseInt(x):
    si = str(x)
    si = si[::-1]
    x = int(si)
    return x

def isPalindrome(x):
    return str(x) == str(x)[::-1]

def isLychrel(x):
    for i in xrange(50):
        x+=reverseInt(x)
        if isPalindrome(x):
            return False
    return True

x = 1
count = 0
while x < 10000:
    if isLychrel(x):
        count+=1
    x+=1

print count
