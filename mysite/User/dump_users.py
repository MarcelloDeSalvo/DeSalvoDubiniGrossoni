from models import User

user = User.objects.create_user(username='john', email='john@example.com', password='password',first_name='John', last_name='Doe')
