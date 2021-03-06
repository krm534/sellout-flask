# sellout-flask

If you're here, you're probably in my group.
To run this project, you'll need a few things installed:
- Python 3.6 or greater
- Flask (called "flask" in pip3)
  * The basic Flask application
- Flask-Login ("flask-login")
  * The module that greatly simplifies and secures user logins/sessions for us
- Flask-WTF ("flask-wtf")
  * The module that handles form generation and posting
- Flask-SQLAlchemy
  * The module that handles database access for us
- Flask-Migrate
  * The module that greatly simplifies updates to our database for us (adding/removing/modifying columns etc)
- Flask-Uploads
  * The module that handles image uploading for us
- phonenumbers
  * The module that handles phone number parsing for us.
- Elasticsearch
  * [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html#install-elasticsearch "Elasticsearch install page") is a full-text search engine that we use for querying the item database. Getting it running locally is a little involved; the site will still work (minus the search feature) if you don't have an Elasticsearch cluster running locally.

You may choose to install these things on a virtual environment rather than your root Python install. To create a virtual environment for these things, run the following command in your terminal in the sellout-flask folder: 
```bash
python3 -m venv venv
```
This will create a virtual environment named *venv* in your application folder. To enter the virtual environment, then run:
```bash
source venv/bin/activate
```
Now everything you install with pip3 will be nice and cleanly installed to the virtual environment instead of your root machine. To install our flask modules, run the following:
```bash
pip3 install flask
pip3 install flask-login
pip3 install flask-wtf
pip3 install flask-sqlalchemy
pip3 install flask-migrate
pip3 install flask-uploads
pip3 install phonenumbers
```

To try running the web server, run
```bash
export FLASK_APP=sellout.py
export FLASK_DEBUG=1
flask run
```

To leave the virtual environment, run
```bash
deactivate
```

To make sure image links render correctly, you'll need to change the IPs used in config.py to match the IP of your server. If you're hosting it locally, this doesn't need to be changed.
