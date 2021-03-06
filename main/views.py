from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, CartItems, Reviews
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .decorators import *
from django.db.models import Sum
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import edituserprofile
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SubscribeForm

class MenuListView(ListView):
    model = Item
    template_name = 'main/home.html'
    context_object_name = 'menu_items'

def menuDetail(request, slug):
    item = Item.objects.filter(slug=slug).first()
    reviews = Reviews.objects.filter(rslug=slug).order_by('-id')[:7] 
    context = {
        'item' : item,
        'reviews' : reviews,
    }
    return render(request, 'main/design.html', context)

@login_required
def add_reviews(request):
    if request.method == "POST":
        user = request.user
        rslug = request.POST.get("rslug")
        item = Item.objects.get(slug=rslug)
        review = request.POST.get("review")

        reviews = Reviews(user=user, item=item, review=review, rslug=rslug)
        reviews.save()
        messages.success(request, "Thankyou for reviewing this product!!")
    return redirect(f"/design/{item.slug}")

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['title', 'image', 'Discount', 'price', 'labels', 'slug']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    fields = ['title', 'image', 'Discount', 'price', 'labels', 'slug']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.created_by:
            return True
        return False

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    success_url = '/item_list'

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.created_by:
            return True
        return False

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    cart_item = CartItems.objects.create(
        item=item,
        user=request.user,
        ordered=False,
    )
    messages.info(request, "Added to Cart!!Continue Shopping!!")
    return redirect("main:cart")

@login_required
def get_cart_items(request):
    cart_items = CartItems.objects.filter(user=request.user,ordered=False)
    bill = cart_items.aggregate(Sum('item__price'))
    number = cart_items.aggregate(Sum('quantity'))
    total = bill.get("item__price__sum")
    count = number.get("quantity__sum")
    context = {
        'cart_items':cart_items,
        'total': total,
        'count': count,
    }
    return render(request, 'main/cart.html', context)

class CartDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CartItems
    success_url = '/cart'

    def test_func(self):
        cart = self.get_object()
        if self.request.user == cart.user:
            return True
        return False

@login_required
def order_item(request):
    cart_items = CartItems.objects.filter(user=request.user,ordered=False)
    ordered_date=timezone.now()
    cart_items.update(ordered=True,ordered_date=ordered_date)
    messages.info(request, "Item Ordered")
    return redirect("main:order_details")

@login_required
def order_details(request):
    items = CartItems.objects.filter(user=request.user, ordered=True,status="Active").order_by('-ordered_date')
    cart_items = CartItems.objects.filter(user=request.user, ordered=True,status="Delivered").order_by('-ordered_date')
    bill = items.aggregate(Sum('item__price'))
    number = items.aggregate(Sum('quantity'))
    total = bill.get("item__price__sum")
    count = number.get("quantity__sum")
    context = {
        'items':items,
        'cart_items':cart_items,
        'total': total,
        'count': count,
    }
    return render(request, 'main/order_details.html', context)

@login_required(login_url='/accounts/login/')
@admin_required
def admin_view(request):
    cart_items = CartItems.objects.filter(item__created_by=request.user, ordered=True,status="Delivered").order_by('-ordered_date')
    context = {
        'cart_items':cart_items,
    }
    return render(request, 'main/admin_view.html', context)

@login_required(login_url='/accounts/login/')
@admin_required
def item_list(request):
    items = Item.objects.filter(created_by=request.user)
    context = {
        'items':items
    }
    return render(request, 'main/item_list.html', context)

@login_required(login_url='/accounts/login/')
@admin_required
def customer_details(request):
    items = COD.objects.filter()
    context = {
        'items':items
    }
    return render(request, 'main/customer_details.html', context)

@login_required(login_url='/accounts/login/')
@admin_required
def message(request):
    items = Contact.objects.filter()
    context = {
        'items':items
    }
    return render(request, 'main/message.html', context)

@login_required
@admin_required
def update_status(request,pk):
    if request.method == 'POST':
        status = request.POST['status']
    cart_items = CartItems.objects.filter(item__created_by=request.user, ordered=True,status="Active",pk=pk)
    delivery_date=timezone.now()
    if status == 'Delivered':
        cart_items.update(status=status, delivery_date=delivery_date)
    return render(request, 'main/pending_orders.html')

@login_required(login_url='/accounts/login/')
@admin_required
def pending_orders(request):
    items = CartItems.objects.filter(item__created_by=request.user, ordered=True,status="Active").order_by('-ordered_date')
    context = {
        'items':items,
    }
    return render(request, 'main/pending_orders.html', context)


@login_required(login_url='/accounts/login/')
@admin_required
def admin_dashboard(request):
    cart_items = CartItems.objects.filter(item__created_by=request.user, ordered=True)
    pending_total = CartItems.objects.filter(item__created_by=request.user, ordered=True,status="Active").count()
    completed_total = CartItems.objects.filter(item__created_by=request.user, ordered=True,status="Delivered").count()
    count1 = CartItems.objects.filter(item__created_by=request.user, ordered=True,item="3").count()
    count2 = CartItems.objects.filter(item__created_by=request.user, ordered=True,item="4").count()
    count3 = CartItems.objects.filter(item__created_by=request.user, ordered=True,item="5").count()
    total = CartItems.objects.filter(item__created_by=request.user, ordered=True).aggregate(Sum('item__price'))
    income = total.get("item__price__sum")
    context = {
        'pending_total' : pending_total,
        'completed_total' : completed_total,
        'income' : income,
        'count1' : count1,
        'count2' : count2,
        'count3' : count3,   
    }
    return render(request, 'main/admin_dashboard.html', context)

def contact(request):
    
    if request.method== "POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        print(name, email, phone, message)
        ins= Contact(name=name, email=email, phone=phone, message=message)
        ins.save()
    return render (request, 'main/contact.html')




def changepassword(request):
    if request.user.is_authenticated:
       if request.method == "POST":
          fm = PasswordChangeForm(user=request.user, data=request.POST)
          if fm.is_valid():
            fm.save()
          update_session_auth_hash(request, fm.user)
          return HttpResponseRedirect('/')
       else:
        fm = PasswordChangeForm(user=request.user)
        return render(request, 'main/changepassword.html', {'form':fm})
    else:
         return HttpResponseRedirect('accounts/login')

def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm= edituserprofile(request.POST, instance=request.user)
            if fm.is_valid():
              messages.success(request, 'Profile Updated')
              fm.save()
             
            return HttpResponseRedirect('/')
        else:
          fm= edituserprofile(instance=request.user)
        return render(request, 'main/edit_profile.html', {'name':request.user, 'form':fm})
    else:
        return HttpResponseRedirect('accounts/login')

def cod(request):
    
    if request.method== "POST":
        name=request.POST['name']
        phone=request.POST['phone']
        Address=request.POST['Address']
        print(name, phone, Address)
        ins= COD(Name=name , PhoneNo3=phone, Address = Address)
        ins.save()
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Your order is placed confermation from Emerald Jeweller!'
            message = 'Dear Customer, Thank you for ordering from Emerald Jeweller! We are excited for you to receive your order and notifying you that its on its way. If you have ordered from multiple sellers, your items will be delivered in separate packages. We hope you had a great shopping experience! You can check your order status here. Please note, we are unable to change your delivery address once your order is placed.???'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            #return redirect('/')

    return render(request, 'main/cash_on_delivery.html', {'form': form})
        

def OP(request):       
    return render (request, 'main/online_payment.html')
