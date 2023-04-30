# <div align="center"> 🎬 Netflix movie review service </div>



![image](https://user-images.githubusercontent.com/99783474/235343764-7a0a19f0-9403-4f53-bd73-19f640d24153.png)
![image](https://user-images.githubusercontent.com/99783474/235343928-a4a7f164-8b59-4e63-b06e-4882f7eff801.png)


---

```bash
$ python -m venv venv
```

```bash
$ source venv/Scripts/activate 
(venv)
```

```bash
$ pip install django==3.2.13
```

```bash
$ python.exe -m pip install --upgrade pip
```

```bash
$ pip install django==3.2.13
```

```bash
$ pip install -r requirements.txt
```

```bash
$  django-admin startproject pjt . 
```

```bash
$ python manage.py runserver
```



---


### 1. 앱 생성

   ```bash
   $ python manage.py startapp movie
   ```

   #### 1-1. 앱 등록 (settings.py)

```python
INSTALLED_APPS = [
    'movie',
    # ...
]
```

### 2. 모델 생성 (models.py)

   ```python
   class Review(models.Model):
       title = models.CharField(max_length=80)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   ```

   ```bash
   $ python manage.py makemigrations
   $ python manage.py migrate
   ```

### 3. 주문서 분리(app별 urls.py 생성)

   #### 3-1. project 메인 urls.py에 include

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("movie.urls")),
]
```

   #### 3-2. app 별 urls.py

```python
from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    # ...
]
```

### 4. 주문서 작성 (urls.py)

   #### 4-1. `html` 파일은 `urls.py`를 불러온다

```html
<a href="{% url 'movie:new' %}">리뷰 작성</a>
<!-- {% url '[app_name]:[urls.py의 path name] '%} -->
```

   #### 4-2. `urls.py`에서 `views.py`를 불러온다

```python
urlpatterns = [
    path("new/", views.new, name="new"),
]
# path("new/", views.[views.py의 함수명], name="new"),
```

   #### 4-3. `views.py`에서 해당 함수는 return 값으로 `html 파일` 혹은 `url`을 불러온다

##### 4-3-1. html 불러오기

```python
# html 파일 불러오기

def new(request):
    # ...
    return render(request, "movie/new1.html")
	# render(request, "[templates/폴더명]/[html 파일명]")
```

##### 4-3-2. url 불러오기

```python
# url 불러오기

def create(request):
    # ...
    return redirect("movie:index")
	# redirect("[app_name]:[urls.py의 path name]")
```

### 5. views.py 함수 return

   > render와 redirect의 차이
   >
   > - `render`는 `templates`를 불러온다
   >
   > - `redirect`는 `URL`로 이동한다

   #### 5-1. 내용 보기

##### 5-1-1. index

```python
def index(request)
    return render(request, "movie/index.html", context)
```

##### 5-1-2. detail

```python
def detail(request, review_pk)
    return render(request, "movie/detail.html", context)
```

   #### 5-2. 생성

##### 5-2-1. new

```python
def new(request):
    return render(request, "movie/new1.html")
```

##### 5-2-2. create

```python
def create(request):
    return redirect("movie:index")
```

#### 5-3. 수정

##### 5-3-1. edit

```python
def edit(request, review_pk):
    return render
```

##### 5-3-2. update

```python
def update(request, review_pk):
    return redirect("movie:index")
```

   #### 5-4. 삭제

##### 5-4-1. delete

```python
def delete(request, review_pk):
    return redirect("movie:index")
```


​         
