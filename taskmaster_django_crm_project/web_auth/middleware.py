from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path in [reverse_lazy('login'), reverse_lazy('register')]:
            return redirect('index')
        elif not request.user.is_authenticated and request.path in [reverse_lazy('my_tasks'),
                                                                    reverse_lazy('my_dashboard'),
                                                                    reverse_lazy('my_customers')]:
            return redirect('index')

        response = self.get_response(request)
        return response
