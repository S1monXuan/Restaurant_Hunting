##### final project for U OF I IS 439

1. Running Environment
This project developed in Python 3.9.2 and Django 3.2.5

2.Description of Hunt Your Meal System
	Hunt Your Meal System is a restaurant rating system where users can share their comments on specific restaurant. Users would be group as customers and restaurant holders.
	For customers, they can upload their comments to specific restaurant from restaurant page or comment list pages. For holders, they have the right to add new restaurant and view customers’ view. Besides, I also set system manager can edit both comment and restaurant information. 

3. List of user ID and password

Roles             AccountName	    Password


tester(SuperUser)	tester	        iSchoolUI

SuperUser	        sysadmin	      secret1!

Customer	        customer	      secret1!

Reataurant_Holder	holder	        secret1!

Manager	          manager	        secret1!


4 Instructor for testing data usage
	For customer user:
	After logging using customer roles account. Customer can view the list of restaurants, holder, place, cuisines, sections list clicking link on the menu list. Customer can see the details of restaurant, holder, restaurant places by clicking the link presented below. For example, to see the detail of restaurant Burger King 1106 West Univ Ave – YUM, user can first click the Restaurant menu, find the restaurant from restaurant list, and click it. The restaurant detail page would show the details of the restaurant and all its rate. Customer also can click the rate text to see the details of the rate.  However, customer user cannot edit other data. When the user click link other than customer and comment, the edit, add and delete bottom would not show up.
	For Restaurant holder:
	As a restaurant holder, user have the right to edit both restaurant and holder information. Such a bottom for add, delete and update would show up after click restaurant and holder information link. In order to protect customer privacy, restaurant holders do not have the right to see the list of customers. The customer link in the menu would not show up. The restaurant holder cannot get access to the customer list page.
	For Manager and SuperUser:
	Manager and super user share the same right in frontend, which means they have the full right to do the create, update, delete actions for all tables. However, super use has the right to edit year and season tables in the backend. Managers only have the full right in frontend.
