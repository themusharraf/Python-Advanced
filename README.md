# Advanced_Python

Python-ga chuqurroq sho'ng'ing va kodlash mahoratingizni oshiring.🟢📡

# Python generatori:

• Iterator obyektini qaytaruvchi funksiyaning maxsus turi.
• Qo'ng'iroq qiluvchi tomonidan so'ralganda birma-bir qiymatlar ketma-ketligini ishlab chiqaradi.
• Generatorlar ijroni to'xtatib turish va ketma-ketlikda keyingi qiymatni qaytarish uchun "yield" kalit so'zi yordamida
aniqlanadi.
• Bu xotiradan yanada samarali foydalanish imkonini beradi va cheksiz ketma-ketlikni yaratishi mumkin.

Ilova qilingan gif python generatorlarini ko'rsatadi,

https://github.com/themusharraf/Advanced_Python/assets/122869450/4813cbf1-54ad-4b07-8954-4f9eea043745

# Decorator

Dekoratorlar yuqori darajadagi funktsiyalarni chaqirish uchun oddiy sintaksisni ta'minlaydi .

Ta'rifga ko'ra, dekorator boshqa funktsiyani qabul qiladigan va ikkinchi funktsiyaning harakatini aniq o'zgartirmasdan
kengaytiradigan funktsiyadir.

Bu chalkash tuyuladi, lekin aslida unday emas, ayniqsa dekorativlar qanday ishlashiga oid bir nechta misollarni
ko'rganingizdan keyin. Ushbu maqoladagi barcha misollarni bu erda topishingiz mumkin .

      def hello(name):
          # ichki funksiya
          def get_name():
              return f"Hello, {name}!"

          # ichki funksiyani qaytarish
          return get_name


      hello_func = hello("Sarvar")
      print(hello_func())

<img width="539" alt="image" src="https://github.com/themusharraf/Advanced_Python/assets/122869450/7ad2db79-74a5-4660-a414-dcfef0edf978">

Decorator funksiya argument sifatida funksiya qabul qiladi.

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

Bitta funksiyada bir nechta decorator ishlatishimiz ham mumkin, bunda birinchisidan boshlab decoratorlar ishlab keladi.

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

# typing modul

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