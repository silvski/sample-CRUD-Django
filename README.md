This is a sample web application demonstrating CRUD API operations via the Django Python package. Sample images are at the bottom of this readme.

<hr>
<h3>Code Notes:</h3>

**guest_register > views.py**
* contains the code for the different CRUD operations

**guest_register > urls.py**
* contains the code for linking the different view functions (CRUD operations) to the front end.

**guest_register > templates > guest_register**
* contains the html files used for the front end developlment of the application

**guests_project > settings.py**
* contains the applications to be loaded into the project as well as the postgresql database credentials.

**guest_register > models.py**
* contains the django model necessary to create and or update a table in the database.
  * fields specifications must also be entered here.

**guest_register > forms.py**
* creates a django form out of the specified django model.

<hr>
Once the server is running, 2 pages will be made accessible namely:

* http://ip_address:8000/guest/
* http://ip_address:8000/guest/list/

<h3>Sample Image: Guest List</h3>
<img src=https://raw.githubusercontent.com/silvski/sample-CRUD-Django/master/guest_list.JPG>

<h3>Sample Image: Guest Form</h3>
<img src=https://github.com/silvski/sample-CRUD-Django/blob/master/guest_list.JPG?raw=true>
