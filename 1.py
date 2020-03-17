def final_salary():
    try:
        time = float(input('Часы работы: '))
        hourly_salary = float(input('часовая ставка '))
        bonus = float(input('Размер премии: '))
        salary = time * hourly_salary + bonus
        print(f'заработная плата сотрудника  {salary}')
    except ValueError:
        return print('Введите корректные данные')
final_salary()
