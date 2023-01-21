def process_file(string):
    for word in string.split(" "):
        if word[-1] == ',' or word[-1] == '!' or word[-1] == '.' or word[-1] == '?':
            marks_list.append(word[-1])
            if word[:-1] not in word_list:
                word_list.append(word[:-1])
        elif word not in word_list:
            word_list.append(word)
    print(word_list)
    print(list(set(marks_list)))


word_list = []
marks_list = []
string = 'Мне не грозит опасность, Скайлер, я сам опасность! Кто-то откроет дверь и ' \
         'схватит пулю. Думаешь, им буду я? Нет. Это я постучу в дверь.'
process_file(string)
