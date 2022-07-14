from collections import defaultdict


def encode(text: str):
    encoding = defaultdict(str)
    if len(set(text)) == 1:
        encoding[text[0]] = '0'

    chars_dict = defaultdict(int)
    for char in text:
        chars_dict[char] += 1

    chars = list(chars_dict.items())

    while len(chars) > 1:
        chars = sorted(chars, key=lambda x: x[1])
        first, first_cnt = chars.pop(0)
        second, second_cnt = chars.pop(0)

        chars.append((first+second, first_cnt+second_cnt))

        for char in first:
            encoding[char] = '0' + str(encoding[char])
        for char in second:
            encoding[char] = '1'+ str(encoding[char])

    return ''.join([encoding[char] for char in text])

assert encode('a') == '0'
assert encode('fff') == '000'
assert encode('abacabad') == '01001100100111'
