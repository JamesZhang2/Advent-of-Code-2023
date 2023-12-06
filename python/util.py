def get_numbers(s):
    """
    Returns a list of (number, startIdx, endIdx) tuple, ordered increasingly by startIdx.
    endIdx is the idx right after the last digit of the number,
    so s[startIdx, endIdx] is the number.
    """
    numbers = []
    start = -1
    for i in range(len(s)):
        if s[i].isdigit():
            if start == -1:
                start = i
        else:
            if start != -1:
                numbers.append((int(s[start:i]), start, i))
            start = -1
    if start != -1:
        numbers.append((int(s[start:len(s)]), start, len(s)))
    return numbers

def get_digits(s):
    """
     Returns a list of (digit, idx) tuple, ordered increasingly by idx.
    """
    digits = []
    for i, ch in enumerate(s):
        if ch.isdigit():
            digits.append((int(ch), i))
    return digits

print(get_numbers("123abc345bcd8"))
print(get_numbers("9"))
print(get_numbers("0abcd9523235d8d8p12"))
print(get_numbers("abc456abc"))
print(get_numbers("The quick brown fox jumps over the lazy dog!"))

print(get_digits("123abc345bcd8"))
print(get_digits("9"))
print(get_digits("0abcd9523235d8d8p12"))
print(get_digits("abc456abc"))
print(get_digits("The quick brown fox jumps over the lazy dog!"))
