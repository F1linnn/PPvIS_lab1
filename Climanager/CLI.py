import click
from Animal import Animal
from Cell import Cell
import json
from Area import Area
from Plant import Plant

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


world = Area(load_file())


@click.group()
def cli():
    pass


@click.command()
@click.option('--row', default = 0, help='Its row index of cell in area, gets int')
@click.option('--line', default = 1, help='Its line index of cell in area, gets int')
@click.option('--type', default = 'Bison', help='Its type of animal(Bison,Deer,Wolf,Rabbit,Lion), gets string')
@click.option('--sex', default = 'Bison', help='Its sex of animal(m,f), gets string')
def add_animal(row, line, type, sex):
    answer = world.create_animal(row, line, type, sex)
    if answer == "Uncorrect type animal!" or answer == "Uncorrect sex!" or answer == "Max inhabitants on cell(4/4)":
        click.echo(answer)
    else:
        click.echo(answer)


@click.command()
@click.option('--row', default = 0, help='Its row index of cell in area, gets int')
@click.option('--line', default = 1, help='Its line index of cell in area, gets int')
def add_plant(row, line):
    answer = world.create_plant(row,line)
    if answer == "Line index or Row index error!" or answer == "This cell have a plant!":
        click.echo(answer)
    else:
        click.echo(answer)

@click.command()
def next_step():
    world.next_step_in_world()


@click.command()
def save():
    world.save_in_file()

@click.command()
def display_area():
    world.display_area()


cli.add_command(add_animal)
cli.add_command(add_plant)
cli.add_command(next_step)
cli.add_command(save)
cli.add_command(display_area)