class PersonalComputer:
    def __init__(self, motherboard, videocard, processor, ram, storage):
        self.__motherboard = motherboard
        self.__videocard = videocard
        self.__processor = processor
        self.__ram = ram
        self.__storage = storage

    def __repr__(self):
        print(f'''        ----- Computer -----
        MotherBoard: {self.__motherboard}
        Processor: {self.__processor}
        VideoCard: {self.__videocard}
        RAM: {self.__ram}
        Storage: {self.__storage}
        ''')
        

asus = PersonalComputer('ASUS', 'GTX 2070TI', 'i3 11200K', '8GB', 'SSD 128GB')
asrock = PersonalComputer('ASrock', 'RX 5500 XT', 'Ryzen 3 3300X', '16GB', 'SSD 128GB')
aorus = PersonalComputer('AORUS', 'Radeon R5 230', 'Athlon 3000G', '8GB', 'HDD 2TB')

asrock.__repr__()