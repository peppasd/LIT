from django.contrib.auth.models import User

def existsUser(username):
    if User.objects.filter(username=username).exists():
        return True
    
    return False