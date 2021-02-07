# Django-OAuth-example
# Installation
To install Django-OAuth-toolkit(DOT) run the command in bash
    pip install django-oauth-toolkit    
# Project Structure
This project has only one app (Its name is also app). This is a shopping cart app. It is used to write Apis using Django Rest Framework.We can use Django OAuth Toolkit to make a Web OAuth2.0 server. 
For this example I have used grant_type as password.
    
    
 To include Django-OAuth-Toolkit the following is added to INSTALLED_APPS =>
    INSTALLED_APPS = (
    ...
    'oauth2_provider',
    )

