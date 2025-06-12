def one_to_nineteen(n):
    words = [
        '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
        'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
        'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ]
    return words[n]

def tens(n):
    words = [
        '', '', 'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety'
    ]
    return words[n]

def two_digits(n):
    if n < 20:
        return one_to_nineteen(n)
    else:
        return tens(n // 10) + ('-' + one_to_nineteen(n % 10) if n % 10 != 0 else '')

def three_digits(n):
    if n < 100:
        return two_digits(n)
    else:
        return one_to_nineteen(n // 100) + ' hundred' + (' and ' + two_digits(n % 100) if n % 100 != 0 else '')

def number_to_words(n):
    if n == 0:
        return 'zero'

    parts = []
    if n >= 1_000_000:
        parts.append(three_digits(n // 1_000_000) + ' million')
        n %= 1_000_000
    if n >= 1_000:
        parts.append(three_digits(n // 1_000) + ' thousand')
        n %= 1_000
    if n > 0:
        parts.append(three_digits(n))

    return ' '.join(parts)

if __name__ == "__main__":
    number = int(input("Enter a number (0 - 999999999): "))
    print("In words:", number_to_words(number))
