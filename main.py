
class Laptop:
    def __init__(self, model):
        self.model = model
        self.color = None
        self.size = None
        self.weight = None
        self.parameters = None
        self.year = None
        self.price = None
        self.new = False
        self.is_running = False
        self.sensor_display = False

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.pr

        # features
    def running(self):
        if not self.is_running:
            self.is_running = True
        else:
            self.is_running = False

    def is_new(self):
        if not self.new:
            self.new = True
        else:
            self.new = False

    def play_game(self):
        print('Playing game.....')

    def go_internet(self):
        print('browsing internet....')

    def __str__(self):
        return f'Laptop {self.model}'


