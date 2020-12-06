### Cara Install :
Clone repo ini:  
> git clone https://github.com/shabri-arrahim/news_scraper.git

Masuk kedalam folder project
> cd news_scraper

## Kalau mau pakai Virtual ENV:
Instalasi env package
> pip install virtualenv

Buat vitual ENV
> virtualenv "nama_env"

Aktivasi virtual env
Kalau pakai MacOS atau linux 'bash'
> source "nama_env"/bin/activate

Kalau pakai windows 'cmd'
> "nama_env"\Scripts\activate.bat

Kalau pakai windows 'PowerShell'
> "nama_env"\Scripts\activate.ps1

Kalau pakai windows 'git bash'
> source "nama_env"\Scripts\activate

Install requirements
> pip install -r requirements.txt

### Cara Penggunaan
Masuk kedalam direktori kompas
> cd kompas

Sesuaikan pengaturan seperti yang tertulis pada masing-masing kelas spider

Run crawl command berikut untuk mengumpulkan index berita:
> scrapy crawl kompas -o kompasindex.json -t json

Run crawl command berikut untuk mengumpulkan content berita sebagai json file:
> scrapy crawl kompastrd -o kompascontent.json -t json

Run crawl command berikut untuk mengumpulkan content berita sebagai csv file [Sebaiknya gunakan yang ini]:
> scrapy crawl kompastrd -o kompascontent.csv -t csv 
