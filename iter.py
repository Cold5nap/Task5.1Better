def is_letter(c):
    if 'Z' >= c >= 'A' or 'z' >= c >= 'a' or 'я' >= c >= 'А':
        return True
    else:
        return False


def add_rev_word_to_data(data: str, word: str):
    it_word = iter(DataIteration(word[::-1]))
    while True:
        try:
            data += next(it_word)
        except StopIteration:
            break
    return data


def index_first_others(data):
    for i in range(len(data)):
        if is_letter(data[i]):
            return i


def index_last_other(data):
    for i in range(len(data[::-1])):
        if not is_letter(data[i]):
            return len(data) - i


class DataIteration:
    class IterImpl:
        def __init__(self, data: str):
            self.data = data
            self.n = 0

        def __next__(self):
            if self.n < len(self.data):
                word_and_other_str = self.data[self.n]
                self.n += 1
                return word_and_other_str
            else:
                raise StopIteration

    def __init__(self, data: str):
        self.container = data

    def __iter__(self):
        return DataIteration.IterImpl(self.container)

    def couples_word_other(self):
        data = self.container
        couples = {}
        sub_word = sub_other = ""
        is_coup_begun = is_word_begun = is_other_begun = False
        sub_data = data[index_first_others(data):index_last_other(data)]
        if not index_first_others(data) == 0:
            couples[""] = data[:index_first_others(data)]
        for c in sub_data:
            if is_word_begun and is_other_begun:
                is_coup_begun = True
                is_word_begun = False
                is_other_begun = False

            if is_letter(c):
                is_word_begun = True
            else:
                is_other_begun = True

            if is_coup_begun and is_word_begun:
                couples[sub_word] = sub_other
                is_coup_begun = False
                sub_other = sub_word = ""

            if is_letter(c):
                sub_word += c
            else:
                sub_other += c

        couples[sub_word] = sub_other
        return couples

    # пара значений не слово и слово
    def rev_words(self):
        new_data = ""
        sub_str = ""
        is_word = False
        is_other = False
        while True:
            try:
                for c in self.couples_word_other():


            except StopIteration:
                break

        new_data = ""
        word = ""
        iterator = iter(DataIteration(self.container))
        while True:
            try:
                c = next(iterator)
                if is_letter(c):
                    word += c
                else:
                    if len(word) > 0:
                        new_data = add_rev_word_to_data(new_data, word)
                        word = ""
                    new_data += c
            except StopIteration:
                break

        if len(word) > 0:
            new_data = add_rev_word_to_data(self.container, word)
        return new_data
