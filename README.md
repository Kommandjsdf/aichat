# template_django
A template for Django project

1. Створити теку
   -
      `D:` - перейти на обраний диск <br/>
      `cd <розміщення/назва теки>` - зайти до директорії <br/>
      `cd..` - вийти до попередньої дерикторії <br/>
      `dir` - показати вміст поточної дерикторії <br/>
2. Створити теку
   -
      ```bash
      md <Назва теки>
      ```
3. Клонувати
   -
      ```bash
      https://github.com/Kommandjsdf/template_django.git
      ```
4. Віртуальне середовище
   -
      - Створити віртуальне середовище `.venv` або підключити існуюче
         ```bash
         #створення віртуального середовища
         python -m venv .venv
         ```
      - Активація віртуального середовище
         ```bash
         #Windows
         .venv/Scripts/activate
         
         #Linux & MacOS
         .venv/bin/activate
         ```
   
5. Встановлення необхідних модулей
   -
    ```bash
    pip install request
    ```

6. Створення нового проекту Django
   -

[//]: # (      ```bash)

[//]: # (         django-admin startproject <найменування_сайту> .)

[//]: # (      ```)

[//]: # (      ```bash)

[//]: # (         python manage.py startapp <назва_додатку>)

[//]: # (      ```)