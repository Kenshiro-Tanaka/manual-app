from django.shortcuts import render, redirect
from .models import Manual
from django.db.models import Q

# Create your views here.

def manual_list(request):
    query = request.GET.get('q', '')
    manuals = Manual.objects.all().order_by('-uploaded_at')
    if query:
        manuals = manuals.filter(Q(title__icontains=query))
    return render(request, 'manuals/manual_list.html', {'manuals': manuals, 'query': query})

def manual_upload(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        file = request.FILES['file']
        Manual.objects.create(title=title, description=description, file=file)
        return redirect('manual_list')
    return render(request, 'manuals/manual_upload.html')
