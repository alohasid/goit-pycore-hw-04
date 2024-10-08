import pathlib

def total_salary(path: pathlib.Path) -> tuple[int, int]:
    total = 0
    avarage = 0
    employees = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                compensation = int(line.split(',')[1])
                total += int(compensation)
                employees += 1
        
        avarage = total / employees
    except FileNotFoundError:
        print('File not found')
    except ZeroDivisionError:
        print('Wrong data passed')
    except Exception:
        print('Something went wrong')
    

    return total, avarage

total, average = total_salary("compensations.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
