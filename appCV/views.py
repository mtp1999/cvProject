from django.shortcuts import render


def home(request):
    context = {
        'name': 'Mohamad TP',
    }
    return render(request, 'appCV/home.html', context)


def about(request):
    context = {
        'name': 'Mohamad TP',
        'phone': '+98 911 *** 10 15',
        'email': 'mohamad.tavakolpoorsaleh@gmail.com',
        'city': 'Tehran, Iran',
        'website': 'www.example.com',
        'age': '24',
        'degree': 'Bachelor',
        'freelance': 'available',
        'birthdate': '21 March 1999',

    }
    return render(request, 'appCV/about.html', context=context)


def languages(request):
    return render(request, 'appCV/languages.html')


def skills(request):
    context = {
        'skills': [
            ['HTML', 100],
            ['CSS', 90],
            ['Bootstrap', 90],
            ['Javascript', 60],
            ['LPIC1', 80],
            ['Python', 90],
            ['PySide6', 80],
            ['Django', 70],
            ['Git', 90],
            ['Docker', 70],
        ]
    }
    return render(request, 'appCV/skills.html', context=context)


def resume(request):

    return render(request, 'appCV/resume.html')


def contact(request):
    context = {
        'location': 'Tehran, Sattari avu, blv Khalil abadi, Mehr-B3',
        'email': 'mohamad.tavakolpoorsaleh@gmail.com',
        'phone': '+98 4447 ** *5'

    }
    return render(request, 'appCV/contact.html', context=context)


def services(request):
    return render(request, 'appCV/services.html')



