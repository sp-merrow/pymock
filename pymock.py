mockText = input('Enter uninformed internet comment to make fun of: ')
mocked = ''

for count, letter in enumerate(mockText):
    if (count+1) % 2 == 0:
        mocked += letter.upper()
    else:
        mocked += letter.lower()

print(f'\n{mocked}')