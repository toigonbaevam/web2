from django.shortcuts import render
def home_screen_view(request):
    print(request.headers)
    return render(request,"base.html",{})
def home(request):
    # Logic to create data
    return render(request, 'app_name/home.html', {'data': data})

def blog(request):
    # Logic to create data
    return render(request, 'app_name/blog.html', {'blog_posts': blog_posts})

def products(request):
    # Logic to create data
    return render(request, 'app_name/products.html', {'products': products})


def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})
