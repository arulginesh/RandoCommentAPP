# RandoCommentAPP
This App is Developed using the Language Python 
And the Framework used here - Flash with Jinja

Installation steps

cd RandoCommentAPP

Create a virtualenv and activate it:

$ python3 -m venv venv
$ . venv/bin/activate
Or on Windows cmd:

$ py -3 -m venv venv
$ venv\Scripts\activate.bat

Install Flaskr:

$ pip install -e .

Run
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask init-db
$ flask run
Or on Windows cmd:

> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask init-db
> flask run

Our Root URL is : http://127.0.0.1:5000/blog/
Open http://127.0.0.1:5000/blog/ in a browser
