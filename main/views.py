from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView
from django.db.models import Q
from .models import Category, Salesman, Shop_name, Product, product_Shorts, Rating_star, Rating, Reviews
from .forms import ReviewForm, PurchaseForm, RatingForm


class CategoryYear:
    def get_categores(self):
        return Category.objects.all()

    def get_day(self):
        return Product.objects.filter(draft=False).values_list("data")

class ProductView(CategoryYear, ListView):
    paginate_by = 3
    model = Product
    queryset = Product.objects.filter(draft=False)


class ProductDetailView(DetailView):

    model = Product
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        context['form'] = ReviewForm()
        return context

class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())

class AddPurchase(View):
    """покупка"""
    def post(self, request, pk):
        form = PurchaseForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())
# Create your views here.
class SalesmanView(DetailView):
    model = Salesman
    template_name = 'main/salesman.html'
    slug_field = "name"


class FilterProductView(CategoryYear, ListView):

    def get_queryset(self):
        queryset = Product.objects.filter(
            category__in=self.request.GET.getlist('category')
        )
        return queryset


class FilterJsonProductView(CategoryYear, ListView):
    def get_queryset(self):
        queryset = Product.objects.filter(
            Q(category__in=self.request.GET.getlist('category'))
        ).distinct().values('title', 'price', 'url', 'poster')
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({'models' : queryset}, safe=False)


class AddStarRating(View):
    """Добавление рейтинга фильму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                product_id=int(request.POST.get("product")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)

class Search(ListView):
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = f'q={self.request.GET.get("q")}&'
        return context