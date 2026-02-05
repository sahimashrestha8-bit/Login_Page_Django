import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login_project.settings')
django.setup()

from django.contrib.auth.models import User
from django.test import Client

client = Client()

print("TEST: Accessing /login/")
resp = client.get('/login/')
print('Status:', resp.status_code)

print('\nTEST: Accessing / (home), follow redirects')
resp = client.get('/', follow=True)
print('Final path:', resp.request.get('PATH_INFO'))
print('Status:', resp.status_code)

print('\nTEST: Creating test user')
User.objects.filter(username='autotest').delete()
user = User.objects.create_user('autotest', password='testpass')
print('Created:', user.username)

print('\nTEST: Logging in with correct credentials')
resp = client.post('/login/', {'username': 'autotest', 'password': 'testpass'})
print('Status:', resp.status_code)

print('\nTEST: Logging in with incorrect credentials')
resp = client.post('/login/', {'username': 'autotest', 'password': 'wrong'})
print('Status:', resp.status_code)
