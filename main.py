from sys import argv
import iter
import codecs


def str_file(direct: str):
    data = ""
    try:
        file = codecs.open(direct, encoding='utf-8')
        data = file.read()
    except FileNotFoundError:
        print("not found file")
    return data


# методы, на чарах
def main():
    dir_input = argv[1]
    old_data = str_file(dir_input)
    new_data = iter.DataIteration(old_data).couples_word_other()

    print("Исходный текст:")
    print(old_data)
    print("Новый текст:")
    print(new_data)


# 23
if __name__ == '__main__':
    main()
