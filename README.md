# Advanced_Python
Python-ga chuqurroq sho'ng'ing va kodlash mahoratingizni oshiring.🟢📡
# Python generatori:

• Iterator obyektini qaytaruvchi funksiyaning maxsus turi.
• Qo'ng'iroq qiluvchi tomonidan so'ralganda birma-bir qiymatlar ketma-ketligini ishlab chiqaradi.
• Generatorlar ijroni to'xtatib turish va ketma-ketlikda keyingi qiymatni qaytarish uchun "yield" kalit so'zi yordamida aniqlanadi.
• Bu xotiradan yanada samarali foydalanish imkonini beradi va cheksiz ketma-ketlikni yaratishi mumkin.

Ilova qilingan gif python generatorlarini ko'rsatadi,


https://github.com/themusharraf/Advanced_Python/assets/122869450/4813cbf1-54ad-4b07-8954-4f9eea043745


# Decorator
Dekoratorlar yuqori darajadagi funktsiyalarni chaqirish uchun oddiy sintaksisni ta'minlaydi .

Ta'rifga ko'ra, dekorator boshqa funktsiyani qabul qiladigan va ikkinchi funktsiyaning harakatini aniq o'zgartirmasdan kengaytiradigan funktsiyadir.

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

