from Animal import Animal
from Cell import Cell
import json
from Area import Area
from Plant import Plant
import numpy as np


def load_file_():
    f = open('size.txt', 'r')
    row = int(f.readline())
    line_num = row
    with open('load.json') as infile:
        data = json.load(infile)
        world = []
        plants = data['Plant']


        Animals = data['Animal']
        sexs = data['sex']
        position = data['position']
        counter = 0
        list_anim = []
        for row_i in range(row):
            list_cell = []
            for line in range(row):
                cell = None
                if plants[counter] == 'YES':
                    cell = Cell(row_i, line, Plant(0))
                else:
                    cell = Cell(row_i, line, None)
                    for i in range(len(position)):
                        animal = Animal(Animals[i], sexs[i], 0, True)
                        pos = position[i]
                        if position[i] == position[i+1]:
                            cell.add_animal_to_cell(animal)
                        else:
                            cell.add_animal_to_cell(animal)
                            del Animals [0:i]
                            del position [0:i]
                            del sexs [0:i]
                            break

                list_cell.append(cell)
                counter += 1
            world.append(list_cell)



        print("STOP")
        return world







# row = int(input("Input row: "))
# line = int(input("Input line: "))
# animal = Animal('Bison', 'm', 0)
# second_cells = []
# list_animal = [animal]
def load_file():
    f = open('save.txt', 'r')
    row = int(f.readline())
    line_num = int(f.readline())

    row_list = []
    for num in range(row):
        line_list = []
        for line in range(line_num):
            is_plant = f.readline()
            if is_plant == 'Yes\n':
                plant = Plant(0, True)
            else:
                plant = None
            list_animals = []
            amount_animals = int(f.readline())
            if amount_animals != 0:
                for num_anim in range(amount_animals):
                    type = f.readline()
                    sex = f.readline()
                    animal = Animal(type, sex, 0, True)
                    list_animals.append(animal)
                cell = Cell(num, line, plant, list_animals)
                line_list.append(cell)
            else:
                list_animals = []
                cell_else = Cell(num, line, plant, list_animals)
                line_list.append(cell_else)
        row_list.append(line_list)
    return row_list
# for num in range(row):
#   first_cells = []
# for num_line in range(line):
#   animal = Animal('Bison', 'm', 0)
# list_animal = [animal]
# cell = Cell(num, num_line, None, list_animal)
# first_cells.append(cell)
# second_cells.append(first_cells)


World = Area(load_file())
World.display_area()
World.menu()
