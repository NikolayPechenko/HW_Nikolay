import time
import asyncio


async def notification():  # сделали функцию асинхронной
    time.sleep(10)
    print('До доставки осталось 10 минут')


async def main():  # сделали функцию асинхронной
    task = asyncio.create_task(notification())  # запустит функцию notification и продолжит работу функции
    print('Собираемся в поезду')
    print('Едим')


asyncio.run(main())  # запустили функцию специальной запускалкой

# асинхронность позволяет оставлять отложенные задачи с неким условием, можем делать условия по времени и т.д