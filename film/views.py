from django.shortcuts import render
from django.http import HttpResponse
import threading
from .models import Film,Links_Film
import requests,json
from django.shortcuts import redirect
import time
import os

# Create your views here.
from dotenv import load_dotenv

load_dotenv()
A_K = os.getenv('API_KEY_FILM')
class get_load_data:
	def page_ad(request,jumlah):
		global reques
		global t_1
		reque = request
		reques = request
		print(jumlah)
		context = {
			'jumlah_data' : int(jumlah)
		}
		# print("DISINI ",context["jumlah_data"])
		# print(type(context["jumlah_data"]))
		if jumlah != 0:
			# t1 = threading.Thread(target=get_load_data.change_page,args=(request,int(jumlah),))
			# t1.start()
			# time.sleep(1)
			# t1.join()
			return get_load_data.print_square(request,jumlah)
	# def change_page(request,jumlah):
	# 	context = {
	# 		'jumlah_data' : int(jumlah)
	# 	}
	# 	return render(request,"admin/film/load.html",context)
	def print_square(request,nilai):
		# for x in range(3):
		# 	time.sleep(3)
		# 	print("hitungan ke : ",x)
		# context = {
		# 	'jumlah_data' : int(0)
		# }

		ad_data = Film
		for x in range(nilai):
			query = 'https://api.themoviedb.org/3/movie/'+str(x)+'?api_key='+A_K+'&language=en-US'
			response = requests.get(query)
			if response.status_code == 200:
				array = response.json()
				text = json.dumps(array)
				if text != "error":
					resp_dict = json.loads(text)
					if ad_data.objects.filter(idfilm=resp_dict['id']).exists():
						print("data sudah Ada")
					else:
						ad_data.objects.create(idfilm=resp_dict['id'],namafilm=resp_dict['title'])
					# ad_data1.Film = ad_data.objects.get(idfilm=resp_dict['id'],namafilm=resp_dict['title'])
					# ad_data1.objects.create(Film=resp_dict['title'])
					print(resp_dict['id'])
					print(resp_dict['title'])
		
		return redirect('/admin/film/film/')

class get_link_data:
	def check_link(request):
		ad_data1 = Links_Film
		for flm in Film.objects.all():
			#ad_data1 = Film.objects.get(namafilm=flm['namafilm'])
			if ad_data1.objects.filter(Film=flm).exists():
				print("Data Sudah Ada")
				print(flm)
			else:
				ad_data1.objects.create(Film=flm)
		return redirect('/admin/film/links_film/')

	# 	context = {
	# 			'jumlah_data' : int(jumlah)
	# 		}
	# 	print("oke DISINI C_G")
	# 	print(jumlah)
	# 	#print(t1.deamon())
	# 	return render(request,"admin/film/load.html",context)

class RumahFilm:
	def home_page(request):
		response_data = {}
		# query = "https://api.themoviedb.org/3/movie/popular?api_key="+API_key+"&language=en-US&page=500"
		
		response_data["popular"] = get_film_dat("p")['results'] 
		response_data["trend"] = get_film_dat("t")['results']
		return HttpResponse(json.dumps(response_data),content_type="application/json")


def get_film_dat(tipe):
	if tipe == "p":
		response =  requests.get("https://api.themoviedb.org/3/movie/popular?api_key="+A_K+"&language=en-US&page=500")
		array = response.json()
		text = json.dumps(array)
		resp_dict = json.loads(text)
	elif tipe == "t":
		response =  requests.get("https://api.themoviedb.org/3/trending/all/day?api_key="+A_K)
		array = response.json()
		text = json.dumps(array)
		resp_dict = json.loads(text)

	elif tipe == "g":
		pass
	elif tipe == "d_f":
		pass

	return resp_dict

	
			
		
		


		
		


