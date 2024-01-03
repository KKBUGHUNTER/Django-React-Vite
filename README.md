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
cd ..
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
```

## Create a App called post
```bash
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
MIDDLEWARE = [
    #...
    'corsheaders.middleware.CorsMiddleware',
    #...
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
# create `.env` file in `/frontend/.env`
```
VITE_API_URL=http://127.0.0.1:8000/api/
```
# write the bellow code
```js
import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}post/`);
        if (!response.ok) {
          throw new Error('Network response was not ok...');
        }
        const result = await response.json();
        console.log(result)
        setData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }

    fetchData(); 
  }, []); 
  return (
    <>
      <h1>Hello World!..</h1>
      {data.map((post) => (
        <div key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.body}</p>
        </div>
      ))}
    </>
  );
}

export default App;
```
## Run the Application 
```bash
python3 manage.py makemigrations
python3 manage.py migrate
npm run dev
python3 manage.py runserver
```

## Open your Browser 
Access the application using http://localhost:5173/ <br>
Access the application django page using http://127.0.0.1:8000/api/ <br>
Access the application django Admin page using http://127.0.0.1:8000/admin/login/?next=/admin/ <br>

<img src="https://github.com/KKBUGHUNTER/Django-React-Vite/assets/91019132/4ae082a4-8b19-4abe-b760-203f468a5cb7" height=250>
<img src="https://github.com/KKBUGHUNTER/Django-React-Vite/assets/91019132/72bfc565-45d4-4a22-8151-c0ce1b4fd7af" height=250>
<img src="https://github.com/KKBUGHUNTER/Django-React-Vite/assets/91019132/30a69f11-ed3b-48fa-871f-314ec845035d" height=250>
