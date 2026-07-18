# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Start small. Ship something.")#ئمة الكتب
bookList = [
    {
        "title": "Intro To C++",
        "author": "Kamal",
        "available": True
    },
    {
        "title": "Intro To Python",
        "author": "Ahmed",
        "available": True
    },
    {
        "title": "Intro To Java",
        "author": "Marco",
        "available": True
    }
]


# عرض الكتب
def show_books():
    for book in bookList:
        print(book)


# إضافة كتاب
def add_book():
    print ("welcome to fun add_book")
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    new_book = {
        "title": title,
        "author": author,
        "available": True
    }

    bookList.append(new_book)
    print("Book added successfully.")


# حذف كتاب
def remove_book():
    print ("welcome to fun remove_book")
    title = input("Enter book title to remove: ")

    for book in bookList:
        if book["title"].lower() == title.lower():
            bookList.remove(book)
            print("Book removed successfully.")
            return

    print("Book not found.")


# البرنامج
show_books()

add_book()

show_books()

remove_book()

show_books(
