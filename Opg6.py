# Et forsøg på at lave opgave 6 : - )

with open('originaltext.txt', 'r') as file:
    content = file.read()

content = content.strip()

content = ' '.join(content.split())

content = content.replace(' ,', ',').replace(' .', '.').replace(' ?', '?').replace(' !', '!').replace(' ;', ';').replace(' :', ':')

newText = ''
for i, c in enumerate(content):
    if c == '.' and i < len(content) - 1:
        newText += c + ' ' + content[i+1].capitalize()

    newText += c

with open('formattedtext.txt', 'w') as file:
    file.write(newText)

