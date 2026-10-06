import csv
import json


with open("users.json", "r", encoding="utf-8") as file:
    users = json.load(file)


with open("books.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    books = list(reader)


result_books = []

for row in books:
    book = {
        "title": row["Title"],
        "author": row["Author"],
        "pages": int(row["Pages"]),
        "genre": row["Genre"]
    }

    result_books.append(book)


result_users = []

for user in users:
    result_user = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": []
    }

    result_users.append(result_user)


books_per_user, extra_books = divmod(
    len(result_books),
    len(result_users)
)


book_index = 0

for index, user in enumerate(result_users):
    books_count = books_per_user

    if index < extra_books:
        books_count += 1

    user["books"] = result_books[
        book_index:book_index + books_count
    ]

    book_index += books_count


with open("result.json", "w", encoding="utf-8") as file:
    json.dump(
        result_users,
        file,
        ensure_ascii=False,
        indent=4
    )


with open("result.json", "r", encoding="utf-8") as file:
    json.load(file)