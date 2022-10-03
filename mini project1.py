# The list of books in my library
l=['To Kill a Mockingbird by Harper Lee'
,'The Great Gatsby by F Scott Fitzgerald'
,'Things Fall Apart by Chinua Achebe'
,'Moby-Dick by Herman Melville'
,'The Color Purple by Alice Walker'
,'Catch-22 by Joseph Heller'
,'Atlas Shrugged by Ayn Rand'
,'The Lord of the Rings by J.R.R. Tolkien'
,'Harry Potter and the Philosopher Stone by J.K. Rowling'
,'Diary of a Wimpy Kid: Old School by Jeff Kinney'
,'The BFG by Roald Dahl'
,'Harry Potter and the Chamber of Secrets by J.K. Rowling'
,'Harry Potter and the prisoner of Azkaban by J.K. Rowling'
,'Diary of a Wimpy Kid: Double Down by Jeff Kinney'
,'Awful Auntie by David Walliams'
,'Diary of a Wimpy Kid: by Hard Luck Jeff Kinney'
,'Wonder by R.J. Palacio'
,'James and the Giant Peach by Roald Dahl'
,'Ratburger by David Walliams'
,'Matilda by Roald Dahl' ]



class nikhil_library:
    lst_of_books=l.copy()
    lst_of_books1=l.copy()
    lst_of_books2=l.copy()
    issued_books=[]
    def __init__(self,list_of_books,library_name):
        self.list_of_books=list_of_books
        self.library_name=library_name
    print('\n')
    @classmethod
    def display(cls):
        print('\n')
        print('The list of books in the library : ','\n')
        for i,j in enumerate(cls.lst_of_books2):
            print(i+1, '-' ,j)
        print('\n')
        print('The availabe books in the library : ','\n')
        for i,j in enumerate(nikhil_library.lst_of_books):
            print(i+1, '-' ,j)
        print('\n')
        return ' '
    @classmethod
    def issued_books1(cls):
        print('Issued books : ','\n')
        if len(cls.issued_books)!=0:
            for i,j in enumerate(cls.issued_books):
                print(i+1, '-' ,j)
        else:
            print('No books are issued')
        return ' '
    @classmethod
    def lend(cls):
        nme=input('Enter your Name : ')
        lst = int(input('Select a book you want to lend with number : '))
        string = f'{cls.lst_of_books[lst - 1]} - This book is issued to MR/MRS.{nme}'
        cls.issued_books.append(string)
        cls.lst_of_books.remove(cls.lst_of_books[lst-1])
        return ' '
    @classmethod
    def return_(cls):
        nme=input('Enter your Name :')
        lst=int(input('Select a book you want to return with number : '))
        cls.lst_of_books.insert(lst-1,cls.lst_of_books1[lst-1])
        string=f'{cls.lst_of_books1[lst-1]} - This book is issued to MR/MRS.{nme}'
        cls.issued_books.remove(string)
        return ' '
    @classmethod
    def donate(cls):
        na=input('enter the name of the book : ')
        cls.lst_of_books.append(na)
        cls.lst_of_books2.append(na)
        cls.lst_of_books1.append((na))
        return ' '

emp=nikhil_library(l,'nikhil''s''library')

while True:
    print(r"Welcome to Nikhil's Library",'\n')
    print('1 - To Display books in the library')
    print('2 - To Lend books from the library')
    print('3 - To Return books to the library')
    print('4 - To Donate books to the library')
    print('5 - To view lend details (For Authorised Personal Only)')
    print('q - To Quit the program','\n')
    n=input('select an option from the above : ')

    if n=='1':
        print(emp.display())
    elif n=='2':
        print(emp.lend())
    elif n=='3':
        print(emp.return_())
    elif n=='4':
        print(emp.donate())
    elif n=='5':
        a=input("Enter User ID : ")
        b=input("Enter the Password : ")
        if a=='336677' and b=='nikhil@123':
            print(emp.issued_books1())
        else:
            print('Invalid ID or Password')
            print('\n')
    elif n=='q':
        break
    else:
        print('Wrong input')