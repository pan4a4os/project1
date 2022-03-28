from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главаня страница',
        'values': ['Some', 'hello', '12345'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
