import json
import random
from faker import Faker
from random import randint, uniform
from conf import MODEL

fake = Faker('ru_RU')


def main() -> None:
    '''
    Возвращает список из 100 случайно сгенерированных книг и записывает их в файл books_list.json.
    :return: Файл books_list.json, содержащий 100 книг.
    '''
    with open('books_list.json', 'w', encoding='utf-8') as file:
        json.dump(generate_book(100), file, ensure_ascii=False, indent=2)


def title() -> str:
    """
    Выбирает случайное название книги из файла books.txt
    :return: возврашает случайно выбранное название книги в формате str.
    """

    with open('books.txt', mode='r', encoding='utf-8') as f:
        for i in range(1):
            book = f.read().splitlines()
    return random.choice(book)


def year() -> int:
    """
    Возвращает случайный год в промежутке от 1700 до 2020 года.
    :return: случайный год в формате int.
    """
    return randint(1700, 2020)


def pages() -> int:
    """
    Возвращает случайное количество страниц в промежутке от 50 до 499.
    :return: случайное количество страниц в формате int.
    """
    return randint(50, 499)


def isbn13() -> str:
    """
    Возвращает случайный код ISBN13
    :return: случайный код ISBN13 в формате str.
    """
    return fake.isbn13()


def rating() -> float:
    """
    Возвращает случайное значение рейтинга книги в промежутке от 1 до 5, с округлением до 2-х знаков после запятой.
    :return: Случайный рейтинг книги в формате float.
    """
    return round(uniform(0, 5), 2)


def price() -> float:
    """
    Возвращает случайное значение цены книги в промежутке от 300 до 2000, с округлением до 2-х знаков после запятой.
    :return: Случайную стоимость книги в формате float.
    """
    return round(uniform(300, 2000), 2)


def author() -> list:
    """
    Возвращает случайное ФИО автора в помощью функции Faker.
    :return: Возвращает список, содержащий от 1 до 3 случайных ФИО в формате list.
    """
    author_name = []
    for i in range(randint(1, 3)):
        author_name.append(fake.name())
    return author_name


def get_book_info() -> dict:
    """
    Возвращает словарь, содрежащий ключевую информацию про книгу. Объединяет в себе почти все предыдущие функции.
    :return: словарь информации про книгу в формате dict.
    """
    book_info = {'title': title(),
     'year': year(),
     'pages': pages(),
     'isbn13': isbn13(),
     'rating': rating(),
     'price': price(),
     'author': author()}
    return book_info


def final_dict(counter: int = 1) -> dict:
    """
    Возвращает конечную версию словаря с номером книги и информацией о ней.
    :param counter: Стартовое значение для индекса книги, по-умолчанию 1.
    :return: словарь, который можно передавать в books_list.json
    """
    while True:
        yield {
            'model': MODEL,
            'pk': counter,
            'fields': get_book_info()
        }
        counter += 1


def generate_book(number_of_books: int, pk: int = 1) -> list:
    """
    Возвращает список книг.
    :param number_of_books: количество книг
    :param pk: номер книги
    :return: список книг
    """
    book = []
    gen_book = final_dict(pk)
    for i in range(number_of_books):
        book.append(next(gen_book))
    return book


if __name__ == '__main__':
    main()
