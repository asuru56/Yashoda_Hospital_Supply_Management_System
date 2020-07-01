from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm


# Create your views here.

def home(request):
	orders = Order.objects.all()
	Customers = Customer.objects.all()

	total_Customers = Customers.count()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status = 'Pending').count()

	context = {'orders': orders , 'Customers':Customers,
	'total_orders':total_orders, 'delivered':delivered,
	'pending':pending}

	return render(request, 'accounts/dashboard.html', context)

def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.html' , {'products':products})

def Customer(request , pk_test):
	Customer = Customer.objects.get(id=pk)
	orders = Customer.order_set.all()
	orders_count = orders.count()
	context = {'Customer':Customer,'orders':orders , 'orders_count':orders_count}
	return render(request, 'accounts/Customer.html', context)

def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		print("Printing POST: " , request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')


	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
	order = Order.objects.get(id=pk)
	form = OrderForm(request.POST , instance=order)
	if form.is_valid():
		form.save()
		return redirect('/')
	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')
	context = {'item':order}
	return render(request, 'accounts/delete.html', context)
