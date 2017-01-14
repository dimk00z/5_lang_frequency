import sys
import os
from re import findall
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        print("Файла " + filepath + " не найдено!")
        return None
    print("-----------------------------------------")
    print("Загружен файл " + filepath)
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    words = findall(r'\w+', text)
    print("Десять самых часто встречающихся слов в тексте:")
    for i in Counter(words).most_common(10):
        print("Слово: '" + i[0] + "' встречается " + str(i[1]) + " раз")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for param in sys.argv[1:]:
            text_file = load_data(param)
            if text_file:
                get_most_frequent_words(text_file)
    else:
        print("Не введены параметры командной строки " +
              "вида: python lang_frequency.py <path to file>")
    print("Программа завершена.")
