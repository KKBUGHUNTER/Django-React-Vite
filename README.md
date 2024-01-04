# Run Django-React-Vite Repo
Open your Terminal and Run below commands
```bash
git clone https://github.com/KKBUGHUNTER/Django-React-Vite.git
cd Django-React-Vite
```

Run the Front-End 
```bash
cd frontend
npm install
npm run dev
```
Run the backend
```bash
virtualenv env
cd env
source bin/activate
pip install django djangorestframework django-cors-headers serializer
cd ..
cd backend/
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
Open your Browser and type the following to access the page.
```bash
http://localhost:5173/
http://127.0.0.1:8000/admin/
UserName: testing
Password: testing
```
To Post the data
```bash
http://127.0.0.1:8000/api
http://127.0.0.1:8000/api/post/
http://127.0.0.1:8000/api/post/post/
```


# Thank you...
