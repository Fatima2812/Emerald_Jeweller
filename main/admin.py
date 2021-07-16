from django.contrib import admin
from .models import Item, CartItems, Reviews
from django.db import models
from .models import *

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Created By", {'fields': ["created_by"]}),
        ("Title", {'fields': ["title"]}),
        ("Image", {'fields': ["image"]}),
        ("Discount", {'fields': ["Discount"]}),
        ("Price", {'fields': ["price"]}),
        ("Labels", {'fields': ["labels"]}),
        ("Slug", {'fields': ["slug"]}),
    ]
    list_display = ('id','created_by','title','Discount','price','labels')

class CartItemsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Order Status", {'fields' : ["status"]}),
        ("Delivery Date", {'fields' : ["delivery_date"]})

    ]
    list_display = ('id','user','item','quantity','ordered','ordered_date','delivery_date','status')
    list_filter = ('ordered','ordered_date','status')

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('user','item','review','posted_on')

admin.site.register(Item,ItemAdmin)
admin.site.register(CartItems,CartItemsAdmin)
admin.site.register(Reviews,ReviewsAdmin)
admin.site.register(Employee)
admin.site.register(C_Payment)
admin.site.register(Personal_Data)
admin.site.register(Qualification)
admin.site.register(Previous_Experience)
admin.site.register(Skills)
admin.site.register(Contact_Detail)
admin.site.register(Product_Category)
admin.site.register(Supplier)
admin.site.register(Product_Type)
admin.site.register(Product)
admin.site.register(S_Order_Booking)
admin.site.register(S_Order_Detail)
admin.site.register(S_Payment)
admin.site.register(S_Contact_Detail)
admin.site.register(S_Contact_Person)
admin.site.register(Customer)
admin.site.register(Corderbooking)
admin.site.register(corderdetail)
admin.site.register(Daily_Expense)
admin.site.register(Current_Stock)
admin.site.register(productimg)
admin.site.register(serviceimg)
admin.site.register(indeximg)
admin.site.register(Contact)
admin.site.register(ourdesigns)
admin.site.register(COD)