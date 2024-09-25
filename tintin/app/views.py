from django.shortcuts import render

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
    # Assuming you have a list of image paths
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
        # Add more image paths as needed
    ]
    return render(request, 'thumbnails.html', {'image_paths': image_paths})

#def book_of_the_day(request):
    
def author(request):
    return render(request, 'author.html')
