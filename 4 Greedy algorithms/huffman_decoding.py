def decode(
    encoding: dict,
    code: str,
):
    result = []
    encoding = {v: k for k, v in encoding.items()}
    
    key = ''
    for num in code:
        key+=num
        if key in encoding:           
            result.append(encoding[key])
            key = ''
  
    return ''.join(result)


assert decode(
    encoding={'a': '0'},
    code = '0'
) == 'a'
assert decode(
    encoding={
        'a': '0',
        'b': '10',
        'c': '110',
        'd': '111',
    },
    code = '01001100100111',
) == 'abacabad'
