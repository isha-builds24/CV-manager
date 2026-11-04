import os
import django

# This tells Python which Django settings file to use
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings') 
django.setup()

from django.contrib.auth.models import User

# Define the new admin credentials you want to use
username = "Penguin"
password = "Steelbottle98"

# This checks if the user already exists. If not, it creates a superuser. 
# If they do exist, it safely updates their password.
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email="admin@example.com", password=password)
    print("Superuser created successfully!")
else:
    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()
    print("Superuser password updated!")