from django.contrib import admin

from .models import Items, products_discounts, Products_shoes


# with this line of code we are managing the items from the admin area
class ProductShoes(admin.ModelAdmin):
    list_display = ('shoe_type', 'shoe_color', 'shoe_brand')


class DiscountOffers(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


# the values from the models should match from the classes and the methods which were defined from that
admin.site.register(Products_shoes, ProductShoes)
admin.site.register(products_discounts, DiscountOffers)
admin.site.register(Items, ProductAdmin)
