import requests
from bs4 import BeautifulSoup
import json

# Tentukan URL situs web yang ingin discrape
url_detik = "https://www.detik.com/terpopuler/inet"  # Ganti dengan URL yang ingin Anda scrape
url_kompas = "https://tekno.kompas.com/"  # Ganti dengan URL yang ingin Anda scrape


# Parse konten HTML dengan BeautifulSoup
detik = BeautifulSoup(requests.get(url_detik).content, "html.parser")
kompas = BeautifulSoup(requests.get(url_kompas).content, "html.parser")

# Temukan elemen yang ingin Anda ekstrak datanya
# Misalnya, untuk mengekstrak semua heading level 1 (h1)
headings_detik = detik.find_all("h3", class_="media__title") #detik.com
headings_kompas = kompas.find_all("h4", class_="most__title") #kompas.com

# Cetak teks dari setiap heading

data_detik = []
for heading in headings_detik:
  data_detik.append({
    "judul": heading.text.replace("\n", ""),
  })

# Konversi data ke format JSON
json_data = json.dumps(data_detik, indent=4)

# Cetak data JSON
print(json_data)

data_kompas = []
for heading in headings_kompas:
  data_kompas.append({
    "judul": heading.text,
  })

# Konversi data ke format JSON
json_data = json.dumps(data_kompas, indent=4)

# Cetak data JSON
print(json_data)
