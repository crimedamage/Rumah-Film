from django.contrib import admin

from .models import Film,Links_Film,Xerror_Film
from django.urls import path
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf.urls import url
from . import views

#Register your models here.

# class adminFilm(admin.AdminSite):
# 	site_header = "Database Film"


# RmFilm = adminFilm(name="rmFilm")
# RmFilm.register(Film)
# RmFilm.register(Links_Film)
# RmFilm.register(Xerror_Film)
# admin.register(Film)
class Filmadmin(admin.ModelAdmin):
	search_fields = ('namafilm',)
	# actions = ['get_oke']
	list_display = ('namafilm','ID_FILM')
	change_list_template="admin/film/base_site.html"

	def get_urls(self):
		# print(request)
		urls = super().get_urls()
		custom_urls = [
		 	#url(r'/lod_data/^(?P<jumlah>[0-9]+)/$', views.data),
			path('admin3/data/<int:size>/',self.load_data)
		]
		
		return urls+custom_urls

	def load_data(self,request,size):
		# list_display = ('namafilm','bt_'+str(size))
		pass
	def ID_FILM(self,obj):
		return obj.idfilm
	# def get_oke(self,request):
	# 	print("oke")
	# def view_check():
	# 	pass


class FilmadminLink(admin.ModelAdmin):
	# search_fields = ('namafilm',)
	# actions = ['get_oke']
	list_display = ('Film','VERIFIED')
	change_list_template="admin/film/base_site_link.html"

	def get_urls(self):
		# print(request)
		urls = super().get_urls()
		custom_urls = [
		 	#url(r'/lod_data/^(?P<jumlah>[0-9]+)/$', views.data),
			path('admin3/data/link/',self.load_data)
		]
		return urls+custom_urls

	def load_data(self,request,size):
		# list_display = ('namafilm','bt_'+str(size))
		pass
	def VERIFIED(self,obj):
		return obj.verified
	def get_oke(self,request):
		print("oke")
	def view_check():
		pass



def change_button(self, obj):
    return format_html('<a class="btn" href="/admin/film/models/{}/change/">oke</a>', obj.id)

# admin.site.site_title="oke"
admin.site.register(Film,Filmadmin)
admin.site.register(Links_Film,FilmadminLink)
admin.site.register(Xerror_Film)
admin.site.site_header = "Rumah Film"
admin.site.site_title = "DB"
admin.site.index_title = "Rumah Film"
list_display = ('__str__', 'change_button')
