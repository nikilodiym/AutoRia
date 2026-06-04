# AutoRia (Django)

Документація-провідник для проєкту AutoRia — простого демо-сервісу для оголошень авто.

---

## Зміст

- Огляд проекту
- Швидкий старт (локальна розробка)
- Залежності
- Налаштування оточення (`.env`)
- База даних (Supabase / Postgres)
- Медіа (зображення)
- Адмін панель — додавання машин
- Маршрути / API
- Міграції та керування БД
- Рекомендації для продакшену
- Додаткові ресурси

---

## Огляд проекту

AutoRia — Django-проєкт з додатком `cars`, який зберігає оголошення про автомобілі у PostgreSQL. Ключові можливості:

- Модель `Car` з полями: бренд, модель, рік, ціна, пробіг, мотор, регіон, тип палива, коробка передач, фото, дата додавання.
- Адмін панель для додавання/редагування/видалення машин.
- Головна сторінка показує машини з бази даних.
- Endpoint для фільтрації: `/filter/?brand=...&year=...&fuel=...&transmission=...&max_price=...`.

---

## Швидкий старт (локальна розробка)

1) Клон проекту та перехід до директорії:

```powershell
cd C:\Users\Admin\PycharmProjects\AutoRia\AutoRiaClone
```

2) Створіть і активуйте віртуальне оточення (опціонально):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3) Встановіть залежності:

```powershell
pip install -r requirements.txt
```

4) Створіть файл `.env` у корені `AutoRiaClone` (приклад є в `SUPABASE_SETUP.md`):

```.env
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=<YOUR_DB_PASSWORD>
DB_HOST=<DB_HOST>
DB_PORT=5432
DEBUG=True
SECRET_KEY=<your-secret-key>
```

5) Запустіть міграції і створіть суперюзера:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

6) Запустіть сервер розробки:

```powershell
python manage.py runserver
```

Перейдіть у браузері:
- Сайт: http://localhost:8000/
- Admin: http://localhost:8000/admin/

---

## Залежності

Перелік у `requirements.txt`. Основні:

- Django==6.0.5
- psycopg2-binary (Postgres драйвер)
- python-dotenv (читає `.env`)
- Pillow (обробка зображень)
- опціонально: django-cloudinary-storage / cloudinary / django-storages (для зовнішнього сховища)

---

## Налаштування оточення (`.env`)

Приклад мінімального `.env`:

```
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=aws-0-eu-west-1.pooler.supabase.com
DB_PORT=5432
DEBUG=True
SECRET_KEY=django-insecure-...
```

Файл `.env` вже створений у репозиторії під час налаштування, але **не комітьте** реальні ключі у git.

---

## База даних

Проєкт налаштований на використання PostgreSQL (приклад: Supabase pooler). Параметри читаються з `.env` у `autoria_clone/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

Якщо ви використовуєте Supabase, connection string має вигляд:

```
postgresql://<user>:<password>@<host>:5432/<database>
```

Див. також файл `SUPABASE_SETUP.md` у корені проєкту для прикладів і тестування.

---

## Медіа (зображення)

В проєкті налаштовано локальне зберігання медіа в режимі розробки:

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

У `autoria_clone/urls.py` додано обслуговування медіа коли `DEBUG=True`.

Якщо хочете використовувати зовнішнє сховище (бЕзкоштовні варіанти): Cloudinary (25GB безкоштовно), Backblaze B2 (10GB free), Firebase (5GB free). Інструкції для Cloudinary можна знайти у `README` раніше у розмові — можу автоматично додати конфіг при вашому бажанні.

---

## Адмін панель — як додавати машини

1. Перейдіть у http://localhost:8000/admin/ і увійдіть під суперюзером.
2. Виберіть `Cars` → `Add Car`.
3. Заповніть поля: `brand`, `model`, `year`, `price`, `mileage`, `engine`, `region`, `fuel`, `transmission`, `image`.
4. Натисніть `Save`.

Машина з'явиться на головній сторінці.

---

## Маршрути / API

Основні URL-и додатку `cars` знаходяться у `cars/urls.py`:

- `/` — головна сторінка (відображає список машин)
- `/filter/` — фільтрація (HTTP GET, повертає JSON). Параметри: `brand`, `year`, `fuel`, `transmission`, `max_price`
- `/car/<id>/` — сторінка деталей авто

Приклад виклику фільтрації:

```
GET /filter/?brand=Toyota&year=2020&max_price=20000
```

Отримаєте JSON з полями: `id`, `brand`, `model`, `price`, `year`, `mileage`, `engine`, `region`, `image`.

---

## Міграції та керування БД

- Створити міграції після змін у моделях:

```powershell
python manage.py makemigrations
python manage.py migrate
```

- Переглянути стан:

```powershell
python manage.py showmigrations
```

- Запустити Django shell для взаємодії з моделями:

```powershell
python manage.py shell
>>> from cars.models import Car
>>> Car.objects.all()
```

---

## Тестові дані

Щоб швидко наповнити БД тестовими оголошеннями, можна використати скрипти, які вже були створені в проєкті під час налаштування (видалялися після використання). Також додавайте записи через Admin.

---

## Рекомендації для продакшену

1. Використовуйте зовнішнє S3-сумісне сховище (AWS S3 / DigitalOcean Spaces / Cloudinary) для зображень.
2. Не зберігайте `.env` в Git — використовуйте змінні оточення на сервері.
3. Налаштуйте HTTPS, захист від CORS, та обмежуйте доступ до admin (IP allow/2FA).
4. Для статичних файлів використовуйте `collectstatic` та CDN.

Примірні кроки для деплою:

- Встановіть gunicorn та nginx
- Налаштуйте systemd сервіс для gunicorn
- Nginx сьєкрити SSL та проксувати запити до gunicorn
- Зовнішнє сховище для медіа

---

## Додаткові файли в репозиторії

- `SUPABASE_SETUP.md` — інструкція налаштування Supabase/Postgres (створена раніше)
- `ADMIN_GUIDE.md` — детальна інструкція для адміна з прикладами
- `QUICK_START.md` — коротка інструкція запуску
- `CHANGELOG.md` — журнал змін
- `COMPLETION_REPORT.md` — звіт про зроблені зміни

---

## Часті проблеми та рішення

- **"Image not showing"** — перевірте `MEDIA_URL`, `MEDIA_ROOT`, та чи виводите ви `{{ car.image.url }}` у шаблоні.
- **Помилки миграцій** — переконайтесь, що не залишилось незбережених `.pyc`, і повторно виконайте `makemigrations`.
- **Проблеми з psycopg2 на Windows** — використовуйте `psycopg2-binary` або інсталюйте PostgreSQL dev tools (pg_config).

---

## Хочете, щоб я налаштував безкоштовне зовнішнє сховище?

Рекомендую Cloudinary (25GB free) — можу автоматично додати конфігурацію й інструкцію. Напишіть "налаштуй Cloudinary" і я додам всі зміни (в `settings.py`, `requirements.txt`, `.env.example` і README) + приклади використання.

---

Якщо потрібно — зроблю переклад на англійську або згенерую коротку версію `README` для GitHub.

