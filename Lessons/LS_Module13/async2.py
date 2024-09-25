import time
import asyncio


async def get_temp():
    print('Первое показание')
    await asyncio.sleep(2)
    print('25 градусов по Цельсию')


async def get_press():
    print('Второе показание')
    await asyncio.sleep(4)
    print('101 КПа')


async def main():
    print('Старт')
    task1 = asyncio.create_task(get_temp())
    task2 = asyncio.create_task(get_press())
    await task1  # дождались выполнения задача 1 и 2, только после этого завершили программу
    await task2
    print('Финиш')


start = time.time()
asyncio.run(main())
finish = time.time()

print(f'Итог: {round(finish-start, 2)} секунд')