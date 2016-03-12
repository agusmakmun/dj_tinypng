:sunglasses: Implement API TinyPNG on Django. The basic implementation to optimization of the images using API TinyPNG.

> Please Checkout on this official to get the API https://tinypng.com/developers
> Docs API: https://tinypng.com/developers/reference/python

###Technology Stack
* Python 2.7.6
* Django==1.8.7
* tinify==1.2.0

###Instalation
I assume you already setup your django development with virtual enviroment (virtualenv).

**1. Create virtual enviroment and activate it.**

```
$ virtualenv your_env
$ source bin/activate
```

**2. Cloning this project**

```
$ git clone git@github.com:agusmakmun/dj_tinypng.git
```

**3. Install all requirements**

```
$ pip install -r requirements.txt
```

**4. Database migrations**

```
$ ./manage.py makemigrations
$ ./manage.py migrate
```

**5. Run the server**

```
$ ./manage.py runserver
```

###Example Output images (auto delete and not auto delete)
* [Please Check this path](https://github.com/agusmakmun/dj_tinypng/tree/master/gallery/photos/2016/03/12/)

###Usage on Templates
You can use it with `{{ photo.get_image_optimized }}` on your templates, it will auto return image optimized. Please check this function in `tesapp/models.py` for more.

```python
def get_image_optimized(self):
    """In your templates: {{ photo.get_image_optimized }}"""
    if self.auto_delete == True:
        return str(self.photo.url)
    return str(os.path.splitext(str(self.photo.url))[0])+'_optimized_' + str(os.path.splitext(str(self.photo.url))[1])
```

###License
* [MIT](https://github.com/agusmakmun/dj_tinypng/blob/master/LICENSE)
