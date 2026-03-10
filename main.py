from typing import Dict
import models

SHAPES = list()
SHAPES_DICT = {"1": "point", "2": "line", "3": "circle", "4": "square"}

def check_values(params: dict):
    try:
        for key, value in params.items():
            params[key] = float(value)
    except Exception as exc:
        raise ValueError
    

def enter_data_shape(shape) -> Dict[str, str]:
    param = dict()
    print(f"\n{'='*80}\n")

    param["x"] = input("Введите X:")
    param["y"] = input("Введите Y:")

    if shape == "line":
        param["x_end"] = input("Введите X конца линии:")
        param["y_end"] = input("Введите Y конца линии:")
    elif shape == "circle":
        param["radius"] = input("Введите радиус:")
    elif shape == "square":
        param["side"] = input("Введите длинну стороны:")
    

    return param

def create_shapes(num_shape):
    global SHAPES_DICT, SHAPES
    try:
        shape = SHAPES_DICT[num_shape]
        param = enter_data_shape(shape)
        check_values(param)

        if shape == "point":
            new_shape = models.Point(**param)
        elif shape == "line":
            new_shape = models.Line(**param)
        elif shape == "circle":
            new_shape = models.Circle(**param)
        elif shape == "square":
            new_shape = models.Square(**param)
        
        SHAPES.append(new_shape)
        print("\nФигура создана")

    except Exception:
        raise ValueError

def delete_shapes(id_shape: int):
    global SHAPES

    for num, value in enumerate(SHAPES, start=1):
        if num == id_shape:
            SHAPES.pop(num-1)
            print(f"Фигура удалена")
            return
    else:
        print(f"Фигуры с номером {id_shape} не найдено")


def list_shapes():
    global SHAPES
    print("\nСписок фигур:")
    if len(SHAPES) == 0:
        print("Нет созданых фигур")
        return 
    for num, value in enumerate(SHAPES, start=1):
        print(f"{num}. {value}")
    


while True:
    try:
        print(f"\n{'='*80}\n")
        num = int(input("Выберите действие:\n"
            "1. Создать фигуру\n"
            "2. Удалить фигуру\n"
            "3. Посмотреть список созданных фигур\n"
            "4. Выход\n"
            "> "))

        if num == 1:
            shape_num = input("\nКакую фигуру создать?\n"
                            "1. Точка\n"
                            "2. Линия\n"
                            "3. Круг\n"
                            "4. Квадрат\n"
                            "> ")
            
            create_shapes(shape_num)

        elif num == 2:
            id_shape = int(input("\nВведите порядковый номер фигуры\n"
                                "> "))
            delete_shapes(id_shape)

        elif num == 3:
            list_shapes()

        elif num == 4:
            break
        else:
            raise ValueError

    except ValueError as exc:
        print("Ошибка ввода")

