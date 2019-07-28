from django.shortcuts import render
from .models import Input
from .forms import InputForm

from .cal_longlat import calLocation

# Create your views here.
def main(request):
    if request.method == 'POST':

        form = InputForm(request.POST)
        if form.is_valid():
            post = Input()
            post.age = form.cleaned_data['age']
            post.gender = form.cleaned_data['gender']
            post.category = form.cleaned_data['category']
            print(post.age, post.gender, post.category)
            post.save()

            # 선택한 것들을 가지고 위치와 주변지역 검색
            location_list = []
            location_list = calLocation(post.pk)
            print(location_list[0])
            return render(request, 'map/mapbox.html', {
                'location_list': location_list,
            })

    return render(request, 'map/main.html')


def mapbox(request):
    return render(request, 'map/mapbox.html')

def local_search(request):
    return render(request, 'map/local_search.html')
    