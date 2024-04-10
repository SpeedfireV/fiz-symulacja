
class SimulationController:
    def __init__(self):
        self.running = True
        self.speed = 3000

    def increase_speed(self):
        if self.speed < 10000:
            self.speed += 1

    def decrease_speed(self):
        if self.speed > 1:
            self.speed -= 1

    def double_increase_speed(self):
        if self.speed < 9999:
            self.speed += 2

    def decrease_decrease_speed(self):
        if self.speed > 2:
            self.speed -= 2

    def increase_double_speed(self):
        if self.speed <= 5000:
            self.speed = self.speed * 2

    def decrease_double_speed(self):
        if self.speed > 1:
            self.speed = self.speed // 2

