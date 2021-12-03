class PersonalComputer:
    #construtor
    def __init__(self, motherboard, videocard, processor, ram, storage):
        self.__motherboard = motherboard
        self.__videocard = videocard
        self.__processor = processor
        self.__ram = ram
        self.__storage = storage

    #setters
    def set_motherboard(self, motherboard):
        self.__motherboard = motherboard

    def set_videocard(self, videocard):
        self.__videocard = videocard

    def set_processor(self, processor):
        self.__precessor = processor

    def set_ram(self, ram):
        self.__ram = ram

    def set_storage(self, storage):
        self.__storage = storage

    #getters
    def get_motherboard(self):
        return self.__motherboard

    def get_processor(self):
        return self.__processor

    def get_videocard(self):
        return self.__videocard

    def get_ram(self):
        return self.__ram

    def get_storage(self):
        return self.__storage

asus = PersonalComputer('ASUS', 'GTX 2070TI', 'i3 11200K', '8GB', 'SSD 128GB')
asrock = PersonalComputer('ASrock', 'RX 5500 XT', 'Ryzen 3 3300X', '16GB', 'SSD 128GB')
aorus = PersonalComputer('AORUS', 'Radeon R5 230', 'Athlon 3000G', '8GB', 'HDD 2TB')
pc = PersonalComputer('', '', '', '', '')

pc.set_motherboard('ASUS')
pc.set_processor('Athlon')
pc.set_videocard('Radeon')
pc.set_ram('8GB')
pc.set_storage('SSD')

print(f"MotherBoard: {asus.get_motherboard()}")
print(f"Processor: {asus.get_processor()}")
print(f"VideoCard: {asus.get_videocard()}")
print(f"RAM: {asus.get_ram()}")
print(f"Storage: {asus.get_storage()}")