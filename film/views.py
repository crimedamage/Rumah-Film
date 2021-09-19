from django.shortcuts import render
from django.http import HttpResponse
import threading
from .models import Film,Links_Film
import requests,json
from django.shortcuts import redirect
import time
import os
from django.core import serializers
from datetime import datetime
from django.conf import settings
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
# Create your views here.
from dotenv import load_dotenv
from django.core.files.storage import default_storage

load_dotenv()
A_K = os.getenv('API_KEY_FILM')

#for databases
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
			return get_load_data.get_data(request,jumlah)
		else:
			return redirect('/admin/film/film/')

	# def change_page(request,jumlah):
	# 	context = {
	# 		'jumlah_data' : int(jumlah)
	# 	}
	# 	return render(request,"admin/film/load.html",context)
	def get_data(request,nilai):
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
						#print(resp_dict['genres'])
						genr = ""
						genrNum=0
						for X_ in resp_dict['genres']:
							genrNum +=1
							genr += X_['name']
							if genrNum < len(resp_dict['genres']):
								genr +="," 
							# print(X_)
							# print(X_['name'])
							# print(len(X_))
							# print(len(resp_dict['genres']))
						release_date = datetime.strptime(resp_dict['release_date'], "%Y-%m-%d").date()
						namePoster = str(resp_dict['poster_path'])

						print(type(namePoster))
						localPath = ""
						media_url = settings.MEDIA_URL
						if namePoster != "None":
							url = 'https://image.tmdb.org/t/p/original' + str(resp_dict['poster_path'])
							r = requests.get(url, allow_redirects=True)
							local = str(os.getcwd())
							
							local = local.replace(r'\"',"/")
							localPath = local+'/media/Films/poster' + resp_dict['poster_path']
							localPath1 = 'Films/poster' + resp_dict['poster_path']
							# localpath = os.path.join(media_url,'Films/poster' + resp_dict['poster_path'])
							# print(media_url)
							# print(localPath)
							# print(r.content)

							open(localPath, 'wb').write(r.content)
							# f = default_storage.open(os.path.join(localPath, r.content)).write(r.content)
							# data = f.read()
							# f.close()
							# print(data)

							# img_temp = NamedTemporaryFile(delete=True)
							# img_temp.write(urlopen(url).read())
							# img_temp.flush()
							# print(img_temp)
						else:
							localPath = "Films/poster/cs.jpg"
						rate = format(float(resp_dict['vote_average']),".1f")
						if "." in rate:
							rate = rate.replace(".","")

						ad_data.objects.create(idfilm=resp_dict['id'],namafilm=resp_dict['title']
							,desc=resp_dict['overview'],date=release_date,poster=localPath1
							,genrefilm=genr.lower(),rate=int(rate),popular=resp_dict['popularity']
							,vote_count=resp_dict['vote_count'])
					# ad_data1.Film = ad_data.objects.get(idfilm=resp_dict['id'],namafilm=resp_dict['title'])
					# ad_data1.objects.create(Film=resp_dict['title'])
					# print(resp_dict['id'])
					# print(resp_dict['title'])
		
		return redirect('/admin/film/film/')
#for databases
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

# for views html json
genre = ['action','adventure','animation','anime'
		,'biografi','comedy','crime','documentary'
		,'drama','fantasy','horor','musical','mystery'
		,'romance','sci-fi','sport','thriller','war']
class RumahFilm:
	def Film_API(request,link,data,key):
		response_data = {}
		try:
			if key == "ucok":
				if link == "genre":
					if data.lower() in genre:
						return RumahFilm_get.j_genre(request,data)
					else:
						response_data["404"] = ["ERROR"+link]
				elif link == "detail":
					print(data)
					return RumahFilm_get.get_details(request,data)
				elif link == "search":
					return RumahFilm_get.j_search(request,data)
				elif link == "film":
					if data.lower() == "popular":
						return RumahFilm_get.j_popular(request)
					elif data.lower() == "trend":
						return RumahFilm_get.j_tren(request)
					elif data.lower() == "top":
						return RumahFilm_get.j_top(request)
					# elif data.lower() == "recomended":
					# 	return RumahFilm_get.j_recomended(request)
					elif data.lower() == "latest":
						return RumahFilm_get.j_latest(request)
			# if data == "genre":
			# 	return RumahFilm_get.j_genre(request)
			# else:
			# 	response_data = {}
			# 	response_data["404"] = ["A NAN ANG CARI!!! \nden lapak kapalo ang ko a, MATI ANG!!!"]

			# 	return HttpResponse(json.dumps(response_data),content_type="application/json")

			else:
			
				response_data["4041"] = ["ERROR"]

				return HttpResponse(json.dumps(response_data),content_type="application/json")
		except:
			response_data["4043"] = ["ERROR"]
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		return HttpResponse(json.dumps(response_data),content_type="application/json")

# get img
# https://image.tmdb.org/t/p/original
		
class RumahFilm_get:
	def j_genre(request,genre):
		response_data = {}
		try:
			query = Film.objects.filter(genrefilm__icontains=genre.lower())
			data = []

			for x in query:
				if "," in x.genrefilm:
					genre = x.genrefilm.split(',')
				else:
					genre = genrefilm
				data_x = {"id":x.idfilm,"title":x.namafilm,"genre":genre,"rate":x.rate}
				data.append(data_x)

			response_data["film"] ={"List":data}
		except: 
			response_data = ["Data Tidak Valid"]
		
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	def j_latest(request):
		response_data = {}
		print("lancar 2")
		query = Film.objects.order_by("-date")
		data= []
		print("ini query :")
		print(query)
		for x in query:
			if "," in x.genrefilm:
				genre = x.genrefilm.split(',')
			else:
				genre = genrefilm
			data_x = {"id":x.idfilm,"title":x.namafilm,"genre":genre,"date":str(x.date),"rate":x.rate}
			data.append(data_x)

		response_data["lates"] = {"list":data}
		print(response_data)
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	def j_popular(request):
		response_data = {}
		print("popular")
		#query = Film.objects.order_by("-date")
		query = Film.objects.filter(popular__range=(1000.0,10000.0)).order_by("-date")
		data=[]
		print(query)
		for x in query:
			if "," in x.genrefilm:
				genre = x.genrefilm.split(',')
			else:
				genre = genrefilm
			data_x = {"id":x.idfilm,"title":x.namafilm,"genre":genre,"date":str(x.date),"rate":x.rate,"popularity":x.popular}
			data.append(data_x)

		response_data["lates"] = {"list":data}
		# response_data =["null"]
		
		# query = "https://api.themoviedb.org/3/movie/popular?api_key="+API_key+"&language=en-US&page=500"
		# response_data["popular"] = RumahFilm_get.get_film_dat("populer",0)
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	# def j_recomended(request):
	# 	response_data = {}
	# 	response_data["trend"] = RumahFilm_get.get_film_dat("recomended",0)['results']
		# return HttpResponse(json.dumps(response_data),content_type="application/json")
	def j_search(request,data):
		response_data = {}
		print("popular")
		#query = Film.objects.order_by("-date")
		try:
			query = Film.objects.filter(namafilm__icontains=data.lower())
			data=[]
			print(query)
			for x in query:
				if "," in x.genrefilm:
					genre = x.genrefilm.split(',')
				else:
					genre = genrefilm
				data_x = {"id":x.idfilm,"title":x.namafilm,"genre":genre,"date":str(x.date),"rate":x.rate,"popularity":x.popular}
				data.append(data_x)

			response_data["lates"] = {"list":data}
		except:
			response_data["lates"] = {"list":"404"}

		
		# response_data =["null"]
		
		# query = "https://api.themoviedb.org/3/movie/popular?api_key="+API_key+"&language=en-US&page=500"
		# response_data["popular"] = RumahFilm_get.get_film_dat("populer",0)
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	def j_top(request):
		response_data = {}
		print("popular")
		#query = Film.objects.order_by("-date")
		query = Film.objects.filter(rate__range=(85,100)).order_by("-date")
		data=[]
		print(query)
		for x in query:
			if "," in x.genrefilm:
				genre = x.genrefilm.split(',')
			else:
				genre = genrefilm
				data_x = {"id":x.idfilm,"title":x.namafilm,"genre":genre,"date":str(x.date),"rate":x.rate}
				data.append(data_x)

		response_data["lates"] = {"list":data}
		# response_data =["null"]
		
		# query = "https://api.themoviedb.org/3/movie/popular?api_key="+API_key+"&language=en-US&page=500"
		# response_data["popular"] = RumahFilm_get.get_film_dat("populer",0)
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	def j_tren(request):
		response_data = {}
		print("popular")
		#query = Film.objects.order_by("-date")
		query = Film.objects.filter(popular__range=(1000.0,10000.0)).order_by("-date")
		data=[]
		print(query)
		for x in query:
			if "," in x.genrefilm:
				genre = x.genrefilm.split(',')
			else:
				genre = genrefilm
			data_x = {"id":x.idfilm,"title":x.namafilm,"genre":genre,"date":str(x.date),"rate":x.rate}
			data.append(data_x)

		response_data["lates"] = {"list":data}
		# response_data =["null"]
		
		# query = "https://api.themoviedb.org/3/movie/popular?api_key="+API_key+"&language=en-US&page=500"
		# response_data["popular"] = RumahFilm_get.get_film_dat("populer",0)
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	def get_details(request,id):
		response_data = {}
		# query = "https://api.themoviedb.org/3/movie/popular?api_key="+API_key+"&language=en-US&page=500"
		#response_data["detail"] = RumahFilm_get.get_film_dat("detail_film",id)['title']
		da = Film.objects.filter(idfilm=id)
		# print(id)
		# print(da[0])
		# print(response_data)
		response_data["detail_film"] = {
		"title" :list(to_json("film",da[0],"namafilm")),
		"desc"	:list(to_json("film",da[0],"desc")),
		"date"	:list(to_json("film",da[0],"date")),
		"poster"	:list(to_json("film",da[0],"poster")),
		"genrefilm"	:list(to_json("film",da[0],"genrefilm")),
		"rate"	:list(to_json("film",da[0],"rate"))

		}  
		response_data["detail_link_download"] = {
		"link_144":list(to_json("film_link",da[0],"link_144")),
		"link_240":list(to_json("film_link",da[0],"link_240")),
		"link_360":list(to_json("film_link",da[0],"link_360")),
		"link_480":list(to_json("film_link",da[0],"link_480")),
		"link_720":list(to_json("film_link",da[0],"link_720")),
		"link_1080":list(to_json("film_link",da[0],"link_1080"))
		}
		# print(response_data)
		return HttpResponse(json.dumps(response_data),content_type="application/json")

		# https://api.themoviedb.org/3/keyword/{keyword_id}?api_key=<<api_key>>

	def get_film_dat(tipe,id):
		data_film = Film
		if tipe == "populer":
			query = data_film.objects.filter()
			query = "https://api.themoviedb.org/3/movie/popular?api_key="+A_K+"&language=en-US&page=500"
			response =  requests.get(query)
			array = response.json()
			text = json.dumps(array)
			resp_dict = json.loads(text)
		elif tipe == "trend":
			query = "https://api.themoviedb.org/3/trending/all/day?api_key="+A_K
			response =  requests.get(query)
			array = response.json()
			text = json.dumps(array)
			resp_dict = json.loads(text)
		elif tipe == "latest":
			query = "https://api.themoviedb.org/3/movie/latest?api_key="+A_K+"&language=en-US"
			response =  requests.get(query)
			array = response.json()
			text = json.dumps(array)
			resp_dict = json.loads(text)
		elif tipe == "detail_film":
			query = 'https://api.themoviedb.org/3/movie/'+str(id)+'?api_key='+A_K+'&language=en-US'
			response =  requests.get(query)
			array = response.json()
			text = json.dumps(array)
			resp_dict = json.loads(text)
		# elif tipe == "recomended":
		# 	query = 'https://api.themoviedb.org/3/movie/'+str(id)+'?api_key='+A_K+'&language=en-US'
		# 	response =  requests.get(query)
		# 	array = response.json()
		# 	text = json.dumps(array)
		# 	resp_dict = json.loads(text)
		elif tipe == "search":
			query = 'https://api.themoviedb.org/3/movie/'+str(id)+'?api_key='+A_K+'&language=en-US'
			response =  requests.get(query)
			array = response.json()
			text = json.dumps(array)
			resp_dict = json.loads(text)

		else:
			resp_dict = {}
			resp_dict["404"] = ["ERROR"]

		return resp_dict
	
def to_json(dbf,dat,value):
	# array = dat.json()
	# text = json.dumps(array)
	# resp_dict = json.loads(dat)
	if dbf == "film":
		print(value)
		da1 = Film.objects.filter(namafilm=dat).values(value)
		data = []
		if value == "genrefilm":
			for x in da1:
				data.append(x.get(value))
				if "," in x.get(value):
					StringNya = ','.join(map(str, data))
					StringNya = StringNya.split(',')
				else:
					StringNya = data
		else:
			for x in da1:
				data.append(str(x.get(value)))
				print(x)
			StringNya = data

	elif dbf == "film_link":
		da1 = Links_Film.objects.filter(Film=dat).values(value)
		data = []

		for x in da1:
			data.append(x.get(value))
			if " " in x.get(value):
				StringNya = ' '.join(map(str, data))
				StringNya = StringNya.split(' ')
			else:
				StringNya = data
	
	
	return StringNya

def list_link(request):
	response_data={}
	response_data['link']={
			"Genre": "api/Film_API/genre/(nama genre)/ucok",
			"latest": "api/Film_API/film/latest/ucok",
			"populer": "api/Film_API/film/popular/ucok",
			"search": "api/Film_API/search/(nama film)/ucok",
			"top": "api/Film_API/film/top/ucok",
			"tren":"api/Film_API/film/trend/ucok",
			"detail":"api/Film_API/detail/(id film)/ucok"
		}
	return HttpResponse(json.dumps(response_data),content_type="application/json")




	
			
		
		


		
		


