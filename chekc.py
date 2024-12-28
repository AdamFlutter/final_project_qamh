import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)
url = "https://qamh.ma/wp-login.php"
def post(username,password):
    data = {
        'log':username,
        'pwd':password,
        'wp-submit':'Se connecter',
        'testcookie':'1'
    }
    cockie = {
        'wordpress_test_cookie':'WP%20Cookie%20check'
    }
    proxy = { 'https':'https://127.0.0.1:8080','http':'http://127.0.0.1:8080'}
    re = requests.post(url,data=data,verify=False,cookies=cockie)
    if re.text.find('<form name="loginform" id="loginform" action="https://qamh.ma/wp-login.php" method="post">') == -1:
        return 1
    else:
        return re.text

