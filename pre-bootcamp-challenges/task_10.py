def common(string1, string2):
    common = ''
    for item in string1:
        for items in string2:
            if item == items:
                common += f'{items} '
    print(f'Common letters: {common}')
common('house', 'computers')
