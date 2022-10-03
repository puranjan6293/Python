#COROUTINES IN PYTHON
"""
def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("harry")

search.close()
search.send("harry")
# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")

"""
# TASK
def searcher():
    import time
    # Some 4 seconds time consuming task
    book = ["harry" , "rama" , "sita" , "puranjan"]
    time.sleep(3)

    while True:
        text = (yield)
        if text in book:
            print("Congratulations sir your name is in the book")

        else:
            print("Sorry sir your name is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send(input("enter your name\n"))


