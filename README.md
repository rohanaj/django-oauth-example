# Django-OAuth-example
# Installation
To install Django-OAuth-toolkit(DOT) run the command in bash
    
    pip install django-oauth-toolkit    
# Project Structure
This project has only one app (Its name is also app). This is a shopping cart app . It is used to write Apis using Django Rest Framework.We can use Django OAuth Toolkit to make a Web OAuth2.0 server.   
To include Django-OAuth-Toolkit the following is added to INSTALLED_APPS =>
    
    INSTALLED_APPS = (
    ...
    'oauth2_provider',
    )

# Steps

I created an application using password based auth. Then after creation of application I received client ID and client secret.Then using these keys I generated access token and refresh token using curl.

    curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/
    
The API gives success response only with Header Authorization : Bearer <access_token>


