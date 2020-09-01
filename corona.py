# Coronavirus api kullanarak bildirim panelinde Türkiye için günlük açıklanan vaka bilgilerini bulabilirsiniz.
# r = requests.get('https://coronavirus-19-api.herokuapp.com/all') olarak kullanırsanız dünya geneli verileri verir.



import requests
import json
from win10toast import ToastNotifier
from time import sleep


r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/turkey')
data = r.json()
text = f'Yeni Vaka : {data["todayCases"]} \nBugün Ölen : {data["todayDeaths"]} \nToplam İyileşen : {data["recovered"]}\nAktif Hasta : {data["active"]}'
while True:
	toast = ToastNotifier()
	toast.show_toast("Türkiye Covid-19 Rakamlar",text, duration=40)
	sleep(60)