# Loop Your Hood

## By AGnes Koinange

## Description
This is a Django application where users from a hood can alert each other on events and other important things happening in the hood.

## Live Link
https://loopyourhood.herokuapp.com/


## User Stories
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.
* Setup and Installation

# To get the project

$ git clone https://github.com/Agneskoinange/loopyourhood.git

Install and activate Virtual
$ python3 -m venv virtual - source virtual/bin/activate  
Install Dependencies
$ pip install -r requirements.txt 
Setup Database
SetUp your database User,Password, Host then make migrate

python manage.py makemigrations hood 
Now Migrate

$ python manage.py migrate 
* Run the application
$ python3 manage.py runserver 
Running the application
$ python3 manage.py runserver 
Testing the application
$ python3 manage.py test 
Open the application on your browser 127.0.0.1:8000.

## Technologies used
* Python3.8
* Django 3.1.2
* Heroku for deployment
* Github
* Bootstrap4
* PostgreSQL DB

## Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug
Contact Information

## Contact
If you have any question or contributions, please email me at [koinangeagnes@gmail.com]

## License
MIT License

Copyright (c) 2022 Agnes Koinange

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.