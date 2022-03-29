from django.http import HttpResponse
from django.shortcuts import redirect 

def unAllowed_user(view_func):
    def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect("all-posts")
            else:
                return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_actions=[]):
    def decoratoer(view_func):
        def wraper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_actions:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse(" You are not authoerized to view this page")
            
            
        return wraper_func
    return decoratoer




# resource : https://www.youtube.com/watch?v=eBsc65jTKvw&list=RDCMUCTZRcDjjkVajGL6wd76UnGg&index=4