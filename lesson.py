import asyncio

# async def do_something(task_name, seconds):
#     print(f"{task_name} boshlandi. Kutib olish uchun {seconds} sekund kutilmoqda.")
#     await asyncio.sleep(seconds)
#     print(f"{task_name} tugatildi. Kutib olish uchun {seconds} sekund o'tildi.")
#
# async def main():
#     # Asinxron vazifalarni yaratish
#     task1 = asyncio.create_task(do_something("Vazifa 1", 2))
#     task2 = asyncio.create_task(do_something("Vazifa 2", 1))
#
#     # Asinxron vazifalarni bajarish
#     await task1
#     await task2
#
# # Asinxron dasturni ishga tushirish
# asyncio.run(main())