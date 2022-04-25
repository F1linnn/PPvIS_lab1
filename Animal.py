class Animal:
    type: str
    move_or_no: bool
    sex: str
    id: int
    lvl: int
    max_lvl: int
    hp: int
    satiety: int
    max_satiety: int

    def __init__(self, type_animal: str, sex: str,animal_id: int, move_or_no: bool = True):
        self.type = type_animal
        self.move_or_no = move_or_no
        self.sex = sex.replace("\n","")
        self.id = animal_id

        if type_animal == 'Lion\n':
            self.lvl = 1
            self.max_lvl = 5
            self.speed = 4
            self.hp = 1
            self.satiety = 10
            self.max_satiety = self.lvl * 5

        elif type_animal == 'Wolf\n':
            self.lvl = 1
            self.max_lvl = 3
            self.speed = 2
            self.hp = 1
            self.satiety = 10
            self.max_satiety = self.lvl * 3

        elif type_animal == 'Lynx\n':
            self.lvl = 1
            self.max_lvl = 3
            self.speed = 3
            self.hp = 1
            self.satiety = 10
            self.max_satiety = self.lvl * 3

        elif type_animal == 'Rabbit\n':
            self.lvl = 1
            self.max_lvl = 2
            self.speed = 3
            self.hp = 1
            self.satiety = 8
            self.max_satiety = 4 + (self.lvl * 2)

        elif type_animal == 'Deer\n':
            self.lvl = 1
            self.max_lvl = 3
            self.speed = 3
            self.hp = 1
            self.satiety = 8
            self.max_satiety = 4 + (self.lvl * 2)

        elif type_animal == 'Bison\n':
            self.lvl = 1
            self.max_lvl = 6
            self.speed = 3
            self.hp = 1
            self.satiety = 8
            self.max_satiety = 4 + (self.lvl * 2)
        else:
            print(type_animal, '!')


    def get_speed(self) -> int:
        return self.speed

    def get_animal_id(self) -> int:
        return self.id

    def set_animal_id(self, id: int):
        self.id = id

    def get_move_or_no(self) -> bool:
        return self.move_or_no

    def set_move_or_no(self, yes_no: bool):
        self.move_or_no = yes_no

    def info(self) -> str:
        nameanim = self.type.replace("\n","")
        info_string = nameanim + ' ' + str(self.id) + ' Sex:'
        if self.sex == 'f':
            info_string +=  ' female'
        else:
            info_string += ' male'
        info_string += ' Satiety:'
        info_string += str(self.satiety)
        return info_string

    def next_step(self) -> bool:
        if self.satiety <= 0:
            return False
        else:
            self.satiety -= 2
            return True

    def move_choise(self) -> str:
        move_choise = ' '

        if not self.get_move_or_no():
            move_choise = 'I cant move'

        elif self.satiety > self.max_satiety // 2:
            move_choise = 'Find partner'

        elif self.satiety <= self.max_satiety // 2:
             move_choise = 'Find eat'

        elif self.satiety in [1, 0]:
            move_choise = "Dead"
            
        return move_choise

    def get_animal_type(self)->str:
        return self.type

    def get_satiety(self) -> int:
        return self.satiety

    def get_sex(self) -> str:
        return self.sex

    def get_max_satiety(self) -> int:
        return self.max_satiety

    def set_satiety(self, satiety_num: int):
        self.satiety = satiety_num
