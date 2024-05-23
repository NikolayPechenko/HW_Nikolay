cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for i in range(len(cars)):
    cars_count += 10
    if cars_count == 50:
        cars_count += 2
        print(f'{cars_count} и этот город наш')
    else:
        print(f'Я езжу на автомабиле марки {cars[i]}, у меня их {cars_count} штук')
