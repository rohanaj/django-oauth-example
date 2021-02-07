import requests
url = "http://127.0.0.1:8000/o/token/"
data = {"client_id":"UDsSIzFBbeZwDzS19502dRkO8aenJ6ZP63c8IIez","client_secret":"ijM2DMkDTMz867XVoFnJBXRfZFyeRQ6r8H9QJ4ZQ6FRdJXnnmh6rdTVsrLkKp4ai0xpSHXiFAhlnDeLDNrPbUdEf3y4tw0ePBvHQOxZPnB1v8se18qxp2YNyTYFfznZ8","grant_type":"password","redirect_uri":"http://django-oauth-toolkit.herokuapp.com/consumer/exchange/","username":"lenovo","password":"12345","scope":"read "}
r = requests.post(url=url,data=data)
print(r.json())