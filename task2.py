import pathlib

def get_cats_info(path: pathlib.Path) -> list[dict[str, str, int]]:
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cats.append({
                    'id': id,
                    'name': name,
                    'age': age
                })
    except FileNotFoundError:
        print('File not found')
    except Exception:
        print('Something went wrong')

    return cats

cats_info = get_cats_info("cats.txt")
print(cats_info)
