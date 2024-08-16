# Advanced Python

## Python-ga chuqurroq sho'ng'ing va kodlash mahoratingizni oshiring.📡

## Python generatori:

- Iterator obyektini qaytaruvchi funksiyaning maxsus turi.
- Qo'ng'iroq qiluvchi tomonidan so'ralganda birma-bir qiymatlar ketma-ketligini ishlab chiqaradi.
- Generatorlar ijroni to'xtatib turish va ketma-ketlikda keyingi qiymatni qaytarish uchun "yield" kalit so'zi yordamida
  aniqlanadi.
- Bu xotiradan yanada samarali foydalanish imkonini beradi va cheksiz ketma-ketlikni yaratishi mumkin.

https://github.com/themusharraf/Advanced_Python/assets/122869450/4813cbf1-54ad-4b07-8954-4f9eea043745

# Decorator

#### Dekoratorlar yuqori darajadagi funktsiyalarni chaqirish uchun oddiy sintaksisni ta'minlaydi. Ta'rifga ko'ra, dekorator boshqa funktsiyani qabul qiladigan va ikkinchi funktsiyaning harakatini aniq o'zgartirmasdankengaytiradigan funktsiyadir.Bu chalkash tuyuladi, lekin aslida unday emas, ayniqsa dekorativlar qanday ishlashiga oid bir nechta misollarni ko'rganingizdan keyin. Ushbu maqoladagi barcha misollarni bu erda topishingiz mumkin.

```python
  def hello(name):
    # ichki funksiya
    def get_name():
        return f"Hello, {name}!"

    # ichki funksiyani qaytarish
    return get_name


hello_func = hello("Sarvar")
print(hello_func())
```

<img width="539" alt="image" src="https://github.com/themusharraf/Advanced_Python/assets/122869450/7ad2db79-74a5-4660-a414-dcfef0edf978">

### Decorator funksiya argument sifatida funksiya qabul qiladi.

```python
   def make_decorator(func):
    def inner():
        # Ichki funksiya orqali func xususiyatlarini o'zgartirishimiz mumkin
        print("Dekorator ishlayapti")

        func()

    # Ichki funksiya qaytariladi
    return inner


def my_func():
    print("Dekorator uchun ishlatiladigan funksiya")


decorated_func = make_decorator(my_func)
decorated_func()

# Dekorator ishlayapti
# Dekorator uchun ishlatiladigan funksiya
```

### Bitta funksiyada bir nechta decorator ishlatishimiz ham mumkin, bunda birinchisidan boshlab decoratorlar ishlab keladi.

```python

def divide_decorator(func):
    def divide_inner(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            print("Nolga bo'lish mumkin emas!")

    return divide_inner


def second_zero(func):  # zero 0 - > 1 function
    def inner(a, b):
        if b == 0:
            b += 1
        return func(a, b)

    return inner


@second_zero


@divide_decorator
def divider(a, b):
    return a / b


print(divider(10, 5))  # 2.0
print(divider(10, 0))  # 10.0
```

# Typing modul

## Asosiy turlar

- `int`: Butun son
- `float`: O'nli son
- `bool`: Mantiqiy qiymat (True/False)
- `str`: Matn

## Ro'yxatlar va Lug'atlar

- `List[int]`: Butun sonlardan iborat ro'yxat
- `Dict[str, int]`: Kalitlari matn, qiymatlari butun son bo'lgan lug'at

## Union

### O'zgaruvchining bir nechta turda bo'lishi mumkinligini belgilash uchun Union dan foydalaniladi.

```python
from typing import Union


def foo(x: Union[int, str]) -> None:
    print(x)
```

## Optional

### O'zgaruvchi ma'lum bir turda yoki None bo'lishi mumkinligini belgilash uchun Optional dan foydalaniladi.

```python
from typing import Optional


def foo(x: Optional[int]) -> None:
    print(x)
```

## Tuple

### Aniq uzunlikdagi va ma'lum turlardagi elementlardan iborat tuple belgilash uchun Tuple dan foydalaniladi.

```python
from typing import Tuple


def foo(x: Tuple[int, float, str]) -> None:
    print(x)
```

## Any

### Har qanday turdagi bo'lishi mumkin bo'lgan o'zgaruvchi belgilash uchun Any dan foydalaniladi.

```python
from typing import Any


def foo(x: Any) -> None:
    print(x)
```

## Type Aliases

### Murakkab turlarni o'qilishi osonroq qilish uchun tur ta'riflari ishlatilishi mumkin.

```python
from typing import List

Vector = List[float]


def foo(v: Vector) -> None:
    print(v)
```

## Misol

```python
from typing import List, Dict, Union, Optional


def process_data(data: List[Dict[str, Union[int, float]]]) -> Optional[float]:
    if not data:
        return None
    return sum(item['value'] for item in data) / len(data)
```

## Xulosa

### typing moduli Python kodlaringizni tushunarliroq, qulayroq va xatolarni kamaytirish uchun juda foydali. Bu modul bilan yozilgan kodlar kelajakdagi o'zgarishlar uchun yanada aniqroq tuzilmani ta'minlaydi.

# Unpacking and packing

## Unpacking va packing - Python dasturlash tilida juda foydali texnikalar bo‘lib, ular ob’ektlarni ochish va yig‘ish jarayonlarini osonlashtiradi.

## Unpacking

### Unpacking ob’ektni bir necha qismlarga ajratish va har bir qismni alohida o‘zgaruvchiga tayinlash imkonini beradi. Bu ko‘pincha ro‘yxatlar va tuple (to‘plam)lar bilan ishlatiladi.

## Tuple bilan unpacking

```python
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # 1
print(b)  # 2
print(c)  # 3
```

## Ro'yxat bilan unpacking

```python
my_list = [4, 5, 6]
x, y, z = my_list
print(x)  # 4
print(y)  # 5
print(z)  # 6
```

## Funksiya chaqirilishi natijasini unpacking qilish

```python
def get_coordinates():
    return (50.4501, 30.5234)


lat, lon = get_coordinates()
print(f"Latitude: {lat}, Longitude: {lon}")
```

## Packing

### Packing esa aksincha, bir nechta qiymatlarni bitta tuple yoki ro‘yxatga yig‘ish imkonini beradi.

## Tuple bilan packing

```python
a, b, c = 1, 2, 3
my_tuple = (a, b, c)
print(my_tuple)  # (1, 2, 3)
```

## Ro'yxat bilan packing

```python
x, y, z = 4, 5, 6
my_list = [x, y, z]
print(my_list)  # [4, 5, 6]
```

## Funksiya orqali packing

```python
def create_point(x, y, z):
    return (x, y, z)


point = create_point(7, 8, 9)
print(point)  # (7, 8, 9)
```

# *args va **kwargs bilan ishlash

### Unpacking va packing ko‘pincha *args va **kwargs bilan birgalikda ishlatiladi.

### - `*args` funksiyaga kiritilgan argumentlarni tuple ko‘rinishida qabul qiladi,

### - `**kwargs` esa kalit-qiymat juftliklarini dictionary ko‘rinishida qabul qiladi.

```python
def my_function(*args, **kwargs):
    print(args)
    print(kwargs)


my_function(1, 2, 3, name="Alice", age=30)

# (1, 2, 3)
# {'name': 'Alice', 'age': 30}

```

## Unpacking va packingni birgalikda ishlatish

```python
def calculate_sum(a, b, c):
    return a + b + c


my_numbers = [1, 2, 3]
result = calculate_sum(*my_numbers)
print(result)  # 6


# **kwargs bilan unpacking # noqa
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")


info = {"name": "Alice", "age": 30}
print_info(**info)
# Name: Alice, Age: 30
```

## Django'da select_related va prefetch_related optimizatsiya metodlari bo'lib, ular ORM (Object-Relational Mapping) so'rovlarining samaradorligini oshirish uchun ishlatiladi. Ular har xil turdagi ma'lumotlar bazasi so'rovlarini oldindan yuklab olish orqali so'rovlar sonini kamaytiradi, bu esa bajarilish vaqtini tezlashtiradi.

### select_related
Nimani ishlatadi: select_related odatda ForeignKey yoki OneToOneField maydonlar bilan ishlatiladi.
Qanday ishlaydi: Bu metod bog'langan modelni JOIN operatori yordamida bitta so'rovda oladi. Bu esa bog'liq bo'lgan ma'lumotlarni olish uchun kerak bo'ladigan alohida so'rovlar sonini kamaytiradi.
Qachon ishlatish kerak: Agar sizda ForeignKey yoki OneToOneField bilan bog'langan ma'lumotlar mavjud bo'lsa va siz ularga tez-tez murojaat qilmoqchi bo'lsangiz, select_relatedni ishlatishingiz kerak.
Misol:

# Model example
```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# Query with select_related
books = Book.objects.select_related('author').all()

for book in books:
    print(book.author.name)  # Author ma'lumotlari bitta JOIN so'rovda keladi
```
### prefetch_related
Nimani ishlatadi: prefetch_related ManyToManyField yoki ForeignKey maydonlar uchun ishlatiladi, lekin u select_relateddan farqli o'laroq, so'rovlarni ikkita alohida so'rov sifatida yuboradi, keyin esa natijalarni Python tarafida bog'laydi.
Qanday ishlaydi: U bog'langan ob'ektlarni alohida so'rovda yuklab oladi va asosiy so'rov bilan natijalarni bog'laydi. Bu katta hajmdagi bog'langan ob'ektlar mavjud bo'lgan holatlarda yaxshi ishlaydi.
Qachon ishlatish kerak: Agar sizda ManyToMany yoki katta hajmdagi ForeignKey bog'lanishlar mavjud bo'lsa, prefetch_relatedni ishlatish samarali bo'ladi.
Misol:

# Model example
```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

#Query with prefetch_related
books = Book.objects.prefetch_related('authors').all()

for book in books:
    for author in book.authors.all():
        print(author.name)  # Authors alohida so'rovda yuklab olinadi
```
### Xulosa
- `select_related` bir-to-bir yoki bir-to-ko'p bog'lanishlar uchun optimal va bitta so'rovda ma'lumotlarni olib keladi.
- `prefetch_related` ko'p-to-ko'p bog'lanishlar yoki katta hajmdagi bog'langan ob'ektlar uchun ishlatiladi va so'rovlar sonini kamaytiradi, lekin ularni alohida-alohida bajaradi.





