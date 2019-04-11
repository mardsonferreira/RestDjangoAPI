# RestDjangoAPI

If you wish to run your own build, first ensure you have python globally installed in your computer.

After doing this, confirm that you have installed virtualenv globally as well. If not, run this command: 
```
  $ pip install virtualenv
```

Then, save this repository to your PC using git clone 
```
  $ git clone git@github.com:mardsonferreira/RestDjangoAPI.git
```

Enter into your the cloned repository as such: 
```
  $ cd RestDjangoAPI 
```

Create and fire up your virtual environment: 
```
  $ virtualenv venv -p python3
  $ source venv/bin/activate
```
Install the dependencies needed to run the app: 
```
  $ pip install -r requirements.txt
```
Install Django rest-framework: 
```
  $ pip install djangorestframework
```
Make those migrations work 
 ```
  $ python manage.py makemigrations
  $ python manage.py migrate
```  
Running the App Start the server: 
```
  $ python manage.py runserver
```

You can now access the file api service on your browser by using 
```
  http://127.0.0.1:8000/companies/
```

## Following are some examples of queries in API: 
* http://127.0.0.1:8000/companies/ 
* http://127.0.0.1:8000/companies/{id} 
* http://127.0.0.1:8000/versions/ 
* http://127.0.0.1:8000/versions/{id} 
* http://127.0.0.1:8000/publications/ 
* http://127.0.0.1:8000/publications/{date} - (yyyy-mm-dd) 
* http://127.0.0.1:8000/publications/{code_version} 
* http://127.0.0.1:8000/publications/{name_company}

Observation: the parameter between braces must be replaced by the value by which you want to perform the search.

## If you want to execute the test file, type: 
```
  $ python manage.py test
```

