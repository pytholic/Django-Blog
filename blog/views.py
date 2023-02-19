from django.shortcuts import render

posts = [
    {
        "author": "Pytholic",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "February 18, 2023",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "February 19, 2023",
    },
]

# How we handle our blog's home page
def home(request):
    context = {"posts": posts}
    # we can access this context data in out template
    return render(request, template_name="blog/home.html", context=context)


def about(request):
    return render(request, template_name="blog/about.html", context={"title": "About"})
