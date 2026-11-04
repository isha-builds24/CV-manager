# import os
# import django

# # This tells Python which Django settings file to use
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings') 
# django.setup()

# from django.contrib.auth.models import User

# # Define the new admin credentials you want to use
# username = "Penguin"
# password = "Steelbottle98"

# # This checks if the user already exists. If not, it creates a superuser. 
# # If they do exist, it safely updates their password.
# if not User.objects.filter(username=username).exists():
#     User.objects.create_superuser(username=username, email="admin@example.com", password=password)
#     print("Superuser created successfully!")
# else:
#     user = User.objects.get(username=username)
#     user.set_password(password)
#     user.save()
#     print("Superuser password updated!")


import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Fetch credentials from environment variables or use safe defaults
username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'Penguin')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'Steelbottle98')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created successfully!")
else:
    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()
    print(f"Superuser '{username}' password updated successfully!")