<div align=center>
  <h1>Create ReactJS Vite and Django project</h1>
  <h3>  YouTube Video https://youtu.be/eXrwF4LXF5c</h3>
</div>


## Create ReactJS Vite project
frontend  - name of the project
```bash
npm create vite@latest 
cd frontend
npm install
npm run dev
```
## Create and Activate Virtual Environment

```bash
virtualenv env
cd env
source bin/activate
pip install django djangorestframework django-cors-headers serializer
```
## Create Django project
backend  - name of the project
```bash
django-admin startproject backend
cd backend/
```
## Run the Development Server
```bash
python3 manage.py migrate
python3 manage.py runserver
python3 manage.py createsuperuser
python3 manage.py startapp post
```

### Update Backend Settings
In `backend/backend/settings.py`:
```python
INSTALLED_APPS = [
    # ...,
    'rest_framework',
    'corsheaders',
    'post',
    # ...,
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',  # Adjust as per your frontend URL
]
```

### Create Models
In `backend/post/models.py`:
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f"Post: {self.title}"
```

### Admin Configuration
In `backend/post/admin.py`:
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

### Serializers
Create `backend/post/api/serializers.py`:
```python
from rest_framework import serializers
from ..models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body')
```

### Views and URLs
Create `backend/post/api/views.py`:
```python
from rest_framework.viewsets import ModelViewSet
from ..models import Post
from .serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

Create `backend/post/api/urls.py`:
```python
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = router.urls
```

### Root URLs
In `backend/backend/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('post.api.urls')),
]
```

### Run the Application
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

