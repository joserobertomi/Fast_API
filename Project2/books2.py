from fastapi import FastAPI

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int 

    def __init__(self, id: int, title: str, author: str, description: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

# Creating instances of the Book class and storing the instances in the BOOKS list
BOOKS = [
    Book(id=1, title="1984", author="George Orwell", description="A dystopian novel.", rating=5),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", description="A novel about racial injustice.", rating=4),
    Book(id=3, title="The Great Gatsby", author="F. Scott Fitzgerald", description="A story about the American dream.", rating=5),
    Book(id=4, title="Pride and Prejudice", author="Jane Austen", description="A classic romance novel.", rating=5),
    Book(id=5, title="Moby-Dick", author="Herman Melville", description="A novel about a giant whale.", rating=4),
    Book(id=6, title="War and Peace", author="Leo Tolstoy", description="A novel set during the Napoleonic Wars.", rating=5),
    Book(id=7, title="The Catcher in the Rye", author="J.D. Salinger", description="A story about teenage rebellion.", rating=4),
    Book(id=8, title="The Hobbit", author="J.R.R. Tolkien", description="A fantasy adventure.", rating=5),
    Book(id=9, title="Fahrenheit 451", author="Ray Bradbury", description="A novel about a dystopian future.", rating=5),
    Book(id=10, title="Jane Eyre", author="Charlotte Brontë", description="A novel about the experiences of an orphan girl.", rating=5)
]

@app.get("/books")
async def return_all_books():
    return BOOKS