from django.shortcuts import render


def show_billboards(request):
    return render(request, 'index.html')
