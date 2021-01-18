from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


def cars(request):

	# 
	cars = Car.objects.order_by('created_date')

	paginator = Paginator(cars, 3)

	page = request.GET.get('page')
	paged_cars = paginator.get_page(page)

	data ={
		'cars':paged_cars,


	}
	return render(request,'cars/cars.html', data)


def car_detail(request, id):

	single_car = get_object_or_404(Car, pk=id)

	data = {
		'single_car': single_car,

	}
	return render(request,'cars/car_detail.html', data)


def search(request):

	cars = Car.objects.order_by('created_date')

	if 'keyword' in request.GET:
		keyword = request.GET['keyword']
		if keyword:
			cars = cars.filter(description__icontains=keyword)

	if 'select_model' in request.GET:
		select_model = request.GET['select_model']
		if select_model:
			cars = cars.filter(model__iexact=select_model)

	if 'select_city' in request.GET:
		select_city = request.GET['select_city']
		if select_city:
			cars = cars.filter(city__iexact=select_city)

	if 'select_year' in request.GET:
		select_year = request.GET['select_year']
		if select_year:
			cars = cars.filter(year__iexact=select_year)			

	if 'select_body_style' in request.GET:
		select_body_style= request.GET['select_body_style']
		if select_body_style:
			cars = cars.filter(body_style__iexact=select_body_style)			

	data = {
		'cars': cars,
	}

	return render(request, 'cars/search.html',data)
