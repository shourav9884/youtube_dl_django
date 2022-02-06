# Youtube video and audio downloader

This is a kind of a clone of keepvid without any ad or something yet.

This is built using
- `Django` 
- [`youtube-dl`](https://github.com/ytdl-org/youtube-dl/)

## Installation

- Firstly create a virtualenv and activate it 
```
virtualenv venv -p python3
source venv/bin/activate
```
- Then install requirements
```
pip install -r requirements.txt
```
- Run it 
```
python manage.py runserver
```

Now you can get a website running on `8000` port in your localhost. Please visit `http://localhost:8000` from your browser

I have a demo deployed in Heroku

[Heroku deploy](http://youtube-dl-shourav9884.herokuapp.com/)

**Please let me if there is any feature we can build on this**