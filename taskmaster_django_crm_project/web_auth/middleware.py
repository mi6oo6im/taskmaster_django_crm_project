from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path in [reverse('login'), reverse('register')]:
            return redirect('index')
        elif not request.user.is_authenticated and request.path in [reverse('my_tasks'),
                                                                    reverse('my_dashboard'),
                                                                    reverse('my_customers')]:
            return redirect('index')

        response = self.get_response(request)
        return response
