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
        0: "Tintin in the Land of the Soviets",
        1: "Tintin in the Congo",
        2: "Tintin in America",
        3: "Cigars of the Pharaoh",
        4: "The Blue Lotus",
        5: "The Broken Ear",
        6: "The Black Island",
        7: "King Ottokar's Sceptre",
        8: "The Crab with the Golden Claws",
        9: "The Shooting Star",
        10: "The Secret of the Unicorn",
        11: "Red Rackham's Treasure",
        12: "The Seven Crystal Balls",
        13: "Prisoners of the Sun",
        14: "Land of Black Gold",
        15: "Destination Moon",
        16: "Explorers on the Moon",
        17: "The Calculus Affair",
        18: "The Red Sea Sharks",
        19: "Tintin in Tibet",
        20: "The Castafiore Emerald",
        21: "The Flight 714 to Sydney",
        22: "Tintin and the Picaros",
        23: "Tintin and Alph-Art"
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
        c=int(bontent)

    # Pass the corresponding book to the template
    return render(request, 'bookoftheday.html', {'book': books[bontent], 'no': c})

def author(request):
    return render(request, 'author.html')
