#   Downtime Monitor Todo Assessment
##  Downtime Monitor
A SaaS that:
-     Monitors, detects and tracks website's up and down times
-     Provides an API that responds with logs of historical stats for up and down times
-     Notifies specific group of people via email (and/or SMS) when a website goes down and comes back up
-     Able to perform operations all operations with the highest level of complications and sophistications applicable considered.

The sophistication expected includes:
- to track multiple websites simultaneously
- allows all common forms of authorization scheme as available on the destination server
- enforces authorization on system-system data exchange via a scheme of choice
- for data exchange interface provided to be able to return a properly encrypted analyzed historical data that is ready for use 
- and every other standard SaaS software requirement

Key target:
- knowledge and use (approach) of software architecture
- a good experience in the use of data analytics, log storage data and retrieval tools, and encryption tools
- use of test suites (unit and e2e test)

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/izudada/downtime_monitor.git
```

Create a virtual environment to install dependencies and activate it use the link below first to install virtualenv [here](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3#:~:text=Virtualenv%20is%20a%20tool%20used,the%20globally%20installed%20libraries%20either).)

After installation create a virtual environment by running:

```sh
$ virtualen env_name
```

Next, activate the virtual enviroment with :

```sh
$ source env_name/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```


Use migrate command to effect database model:

```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

Start the server with:
```sh
$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`

### Cronjob/Crontabs/Schedule Jobs
Ater running the django server and inserting records into the web models,
you can run the web monitoring scheduled job to monitor changes in the 
state of a website by running the crontab command on a new terminal:

```sh
$ python manage.py crontab add
```
The above command will add a monitoring function to its schedule

To deactivate or stop the scheduled job run:
```sh
$ python manage.py crontab remove
```

Note: scheduled job runs every 3 mins. This is so inorder for the observer to get results 
quicker. You can increase the interval by editting the value of CRONJOBS constant 
in the settings.py file.

Also, once the cronjobs is initiated, a cronjob.log file will be created on the root directory
for debugging purposes

##  Documentation

Postman documentation can be found [Here](https://documenter.getpostman.com/view/20677030/2s8ZDR7kSF)

### Import Postman Collection
You can import the postman collection "Inventory Management System.postman_collection.json"
to test the endpoints locally. by importing Web "Monitor.postman_collection.json" into postman

Note: Postman collection also contain tests for each endpoint

##  Test

To run all available tests use:

```sh
(folder_name)$ python manage.py test
```

### Useful resources

- [Medium](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f) - How to use environmental values
- [Django Crontab](https://pypi.org/project/django-crontab/)