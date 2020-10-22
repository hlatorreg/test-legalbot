from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from urllib.parse import urljoin
from utils import requests_retry_session, requests
import os
import threading

BASE_URL = 'https://www.diariooficial.interior.gob.cl/edicionelectronica/'

def _get_links(date:datetime = None):
   index_url =  f"{BASE_URL}index.php"
   if date:
      index_url = f"{BASE_URL}index.php?date={date.strftime('%d-%m-%Y')}"
   initial_soup = BeautifulSoup(requests_retry_session().get(index_url).text, 'html.parser')
   main_link = initial_soup.select_one("a[href*='empresas_cooperativas.php']")
   day_soup = BeautifulSoup(requests_retry_session().get(f"{BASE_URL}{main_link['href']}").text, 'html.parser')
   con_links = day_soup.select("td > a")
   return con_links

def _setup_folder(path:str):
   if not os.path.exists(path):
      os.makedirs(path)

def _download_file(path:str, link):
   filename = os.path.join(path, link['href'].split('/')[-1])
   print(f"downloading file {filename}...")
   try:
      file_dl = requests_retry_session().get(link['href'], stream=True)
   except ConnectionError:
      nsession = requests.Session()
      file_dl = requests_retry_session(session=nsession).get(link['href'], stream=True)
   with open(filename, 'wb') as file:
      for chunk in file_dl.iter_content(1024):
         if chunk:
            file.write(chunk)

def _download_thread(path:str, link):
   dl_thread = threading.Thread(target=_download_file, args=(path, link))
   dl_thread.start()

def _download_constituciones(path:str, links):
   for l in links:
      _download_thread(path, l)

def download_todays_constituciones(path:str):
   today = datetime.now()
   _setup_folder(path)
   _download_constituciones(path, _get_links(today))

def download_constituciones_from_year(year:int, path:str):
   start = datetime(year=year, month=1, day=1)
   end = datetime(year=year, month=12, day=31)
   current_date = start
   while start <= end:
      formatted_date = current_date.strftime('%d-%m-%Y')
      print(formatted_date)
      datepath = f"{path}/{formatted_date}"
      _setup_folder(datepath)
      _download_constituciones(datepath, _get_links(current_date))
      current_date = current_date + timedelta(days=1)



download_todays_constituciones('./constituciones')
# download_constituciones_from_year(2019, './constituciones')