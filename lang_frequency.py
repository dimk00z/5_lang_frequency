import os
import argparse
from re import findall
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    words = findall(r'\w+', text)
    return Counter(words).most_common(10)


def read_txt_filenames_from_args():
    args_parser = argparse.ArgumentParser(add_help=False)
    args_parser.add_argument("txt_file_name", type=str, nargs='+',
                             help="TXT file for get most frequent words")
    return args_parser.parse_args().txt_file_name

if __name__ == '__main__':
    txt_file_names = read_txt_filenames_from_args()
    for txt_file_name in txt_file_names:
        text_file = load_data(txt_file_name)
        if not text_file:
            print("Файла " + txt_file_name + " не найдено!")
        else:
            print("-----------------------------------------")
            print("Загружен файл " + txt_file_name)
            print("-----------------------------------------")
            frequent_words = get_most_frequent_words(text_file)
            print("Десять самых часто встречающихся слов в тексте:")
            for word in frequent_words:
                print("Слово: '" + word[0] +
                      "' встречается " + str(word[1]) + " раз")
    print("Программа завершена.")
