# deephops: Getting Started


![dh logo](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/98f67462-10a7-46f8-8430-0c99d8bb5bde/github.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220124T110800Z&X-Amz-Expires=86400&X-Amz-Signature=6a1702239098fb8ade82dd54a69fd41c7745d9a5ed2161de47561dbff87804cd&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22github.png%22&x-id=GetObject)





## Running Locally

Make sure you have Python 3.9.7 [installed locally](https://docs.python-guide.org/starting/installation/).

```sh
$ git clone https://github.com/sth-v/deephops.git
$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python .\app.py
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create


$ git push heroku main


$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

