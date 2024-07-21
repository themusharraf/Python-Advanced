"""
Unpacking va packing - Python dasturlash tilida juda foydali texnikalar bo‘lib,
ular ob’ektlarni ochish va yig‘ish jarayonlarini osonlashtiradi.

Unpacking
Unpacking ob’ektni bir necha qismlarga ajratish va har bir qismni alohida o‘zgaruvchiga
tayinlash imkonini beradi. Bu ko‘pincha ro‘yxatlar va tuple (to‘plam)lar bilan ishlatiladi.
"""  # noqa

# Tuple bilan unpacking # noqa
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # 1
print(b)  # 2
print(c)  # 3

# Ro'yxat bilan unpacking # noqa
my_list = [4, 5, 6]
x, y, z = my_list
print(x)  # 4
print(y)  # 5
print(z)  # 6


# Funksiya chaqirilishi natijasini unpacking qilish # noqa
def get_coordinates():
    return (50.4501, 30.5234)


lat, lon = get_coordinates()
print(f"Latitude: {lat}, Longitude: {lon}")

"""
Packing
Packing esa aksincha, bir nechta qiymatlarni bitta tuple yoki ro‘yxatga yig‘ish imkonini beradi.
"""  # noqa
# Tuple bilan packing  # noqa
a, b, c = 1, 2, 3
my_tuple = (a, b, c)
print(my_tuple)  # (1, 2, 3)

# Ro'yxat bilan packing # noqa
x, y, z = 4, 5, 6
my_list = [x, y, z]
print(my_list)  # [4, 5, 6]


# Funksiya orqali packing # noqa
def create_point(x, y, z):
    return (x, y, z)


point = create_point(7, 8, 9)
print(point)  # (7, 8, 9)

"""
*args va **kwargs bilan ishlash
Unpacking va packing ko‘pincha *args va **kwargs bilan birgalikda ishlatiladi.
*args funksiyaga kiritilgan argumentlarni tuple ko‘rinishida qabul qiladi,
**kwargs esa kalit-qiymat juftliklarini dictionary ko‘rinishida qabul qiladi.
"""  # noqa


def my_function(*args, **kwargs):
    print(args)
    print(kwargs)


my_function(1, 2, 3, name="Alice", age=30)


# (1, 2, 3)
# {'name': 'Alice', 'age': 30}

# Unpacking va packingni birgalikda ishlatish # noqa
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
