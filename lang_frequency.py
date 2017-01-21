import os
import argparse
from re import findall
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text, count):
    words = findall(r'\w+', text.lower())
    return Counter(words).most_common(count)


def read_txt_filenames_from_args():
    args_parser = argparse.ArgumentParser(add_help=False)
    args_parser.add_argument("txt_file_name", type=str, nargs='+',
                             help="TXT file for get most frequent words")
    return args_parser.parse_args().txt_file_name


def print_frequent_words(words):
    print("Десять самых часто встречающихся слов в тексте:")
    for word in words:
        print("Слово: '{}' встречается {} раз".format(word[0],
                                                      str(word[1])))


if __name__ == '__main__':
    txt_file_names = read_txt_filenames_from_args()
    for txt_file_name in txt_file_names:
        text_file = load_data(txt_file_name)
        if not text_file:
            print("\nФайла {} не найдено!".format(txt_file_name))
            continue
        print("\nЗагружен файл {}".format(txt_file_name))
        print_frequent_words(get_most_frequent_words(text_file, 10))
    print("\nПрограмма завершена.")
