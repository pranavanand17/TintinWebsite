from django.shortcuts import render
import random
from datetime import datetime
import os

def homepage(request):
    image_paths= [
        "/static/images/slideshow/0.png",
        "/static/images/slideshow/1.png",
        "/static/images/slideshow/2.png",
        "/static/images/slideshow/3.png",
        "/static/images/slideshow/4.png",
        "/static/images/slideshow/5.png",
        "/static/images/slideshow/6.png",
        "/static/images/slideshow/6.5.png",
        "/static/images/slideshow/7.png",
        "/static/images/slideshow/9.png",
        "/static/images/slideshow/10.jpg",
        "/static/images/slideshow/11.png",
        "/static/images/slideshow/12.png",
        "/static/images/slideshow/13.png",
        "/static/images/slideshow/14.jpg",
        "/static/images/slideshow/15.png",
        "/static/images/slideshow/16.jpg",
        "/static/images/slideshow/17.png",
        "/static/images/slideshow/18.jpg",
        "/static/images/slideshow/19.jpg",
        ]
    return render(request, 'homepage.html', {'image_paths': image_paths})

def display_thumbnails(request):
    image_paths = [
        "/static/media/thumbnails/0.jpeg",
        "/static/media/thumbnails/1.jpg",
        "/static/media/thumbnails/2.jpg",
        "/static/media/thumbnails/3.jpg",
        "/static/media/thumbnails/4.jpg",
        "/static/media/thumbnails/5.jpg",
        "/static/media/thumbnails/6.jpg",
        "/static/media/thumbnails/7.jpg",
        "/static/media/thumbnails/8.jpg",
        "/static/media/thumbnails/9.jpg",
        "/static/media/thumbnails/10.jpg",
        "/static/media/thumbnails/11.jpg",
        "/static/media/thumbnails/12.jpg",
        "/static/media/thumbnails/13.jpg",
        "/static/media/thumbnails/14.jpg",
        "/static/media/thumbnails/15.jpg",
        "/static/media/thumbnails/16.jpg",
        "/static/media/thumbnails/17.jpg",
        "/static/media/thumbnails/18.jpg",
        "/static/media/thumbnails/19.jpg",
        "/static/media/thumbnails/20.jpg",
        "/static/media/thumbnails/21.jpg",
        "/static/media/thumbnails/22.jpg",
        "/static/media/thumbnails/23.jpg",
    ]
    return render(request, 'thumbnails.html', {'image_paths': image_paths})

def book_of_the_day(request):
    # Get the directory where views.py is located
    app_dir = os.path.dirname(os.path.abspath(__file__))

    # Build file paths relative to the app directory
    date_file_path = os.path.join(app_dir, "date.txt")
    book_file_path = os.path.join(app_dir, "book.txt")

    books = {
        1: "Tintin in the Land of the Soviets",
        2: "Tintin in the Congo",
        3: "Tintin in America",
        4: "Cigars of the Pharaoh",
        5: "The Blue Lotus",
        6: "The Broken Ear",
        7: "The Black Island",
        8: "King Ottokar's Sceptre",
        9: "The Crab with the Golden Claws",
        10: "The Shooting Star",
        11: "The Secret of the Unicorn",
        12: "Red Rackham's Treasure",
        13: "The Seven Crystal Balls",
        14: "Prisoners of the Sun",
        15: "Land of Black Gold",
        16: "Destination Moon",
        17: "Explorers on the Moon",
        18: "The Calculus Affair",
        19: "The Red Sea Sharks",
        20: "Tintin in Tibet",
        21: "The Castafiore Emerald",
        22: "The Flight 714 to Sydney",
        23: "Tintin and the Picaros",
        24: "Tintin and Alph-Art"
    }

    # Get current date
    current = datetime.now().date()

    # Open 'date.txt' to check last updated date
    with open(date_file_path, "r+") as file:
        content = file.read().strip()
        # If the date is different from today
        if content != str(current):
            file.seek(0)
            file.truncate()  # Clear the file
            file.write(str(current))  # Write the current date

            # Generate a random number for book selection
            random_number = random.randint(1, 24)

            # Open 'book.txt' to store the book number
            with open(book_file_path, "w") as bile:  # Use 'w' to overwrite directly
                bile.write(str(random_number))

    # Read the book number from 'book.txt'
    with open(book_file_path, "r") as cile:
        bontent = int(cile.read().strip())  # Convert back to integer

    # Pass the corresponding book to the template
    return render(request, 'bookoftheday.html', {'book': books[bontent]})
def author(request):
    return render(request, 'author.html')
