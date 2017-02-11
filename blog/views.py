from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})    #drugi argument je template, trazice ga automatski u templates subfolderu koji treba da napravis, a onda blog subfolder i fajl post_list.html
