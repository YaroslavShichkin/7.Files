file_names = ['1', '2', '3', 'Что-то', 'И что-то еще']
all_text = []
text_lenght = []
finish_text = []

for name in file_names:
    all_name = 'Files_2/' + name + '.txt'
    with open(all_name, 'r', encoding='utf8') as file:
        content = file.readlines()
        all_text.append({'name' : name+'.txt', 'lenght' : len(content), 'text' : content})
        text_lenght.append(len(content))

for lenght in sorted(text_lenght):
    for text in all_text:
        if lenght == text['lenght']:
            finish_text.append(text)
            all_text.remove(text)

with open('Files_2/all.txt', 'w', encoding='utf8') as file:
    for text in finish_text:
        text['lenght'] = str(text['lenght'])
        file.writelines([text['name']+'\n', text['lenght']+'\n'])
        for line in text['text']:
            file.write(line)
        file.write('\n')
