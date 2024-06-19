
class SimulationController:
    def __init__(self):
        self.running = False
        self.speed = 100 # max 1000000

    def increase_speed(self):
        if self.speed >= 100_000:
            if self.speed >= 999_900:
                self.speed = 1_000_000
            else:
                self.speed += 100
        elif self.speed >= 100_00:
            self.speed += 10
        else:
            self.speed += 1

    def decrease_speed(self):
        if self.speed >= 100_000:

            self.speed -= 100
        elif self.speed >= 100_00:
            self.speed -= 10
        elif self.speed > 1:
            self.speed -= 1


    def double_increase_speed(self):
        if self.speed >= 100_000:
            if self.speed >= 999_500:
                self.speed = 1_000_000
            else:
                self.speed += 500
        elif self.speed >= 100_00:
            self.speed += 50
        else:
            self.speed += 5

    def double_decrease_speed(self):
        if self.speed >= 100_000:

            self.speed -= 500
        elif self.speed >= 100_00:
            self.speed -= 50
        elif self.speed > 5:
            self.speed -= 5

    def increase_double_speed(self):
        if self.speed <= 500_000:
            self.speed = self.speed * 2
        else:
            self.speed = 1_000_000

    def decrease_double_speed(self):
        if self.speed > 100_000:
            self.speed = self.speed // 200
            self.speed *= 100
        elif self.speed > 10_000:
            self.speed = self.speed // 200
            self.speed *= 100
        elif self.speed > 1:
            self.speed = self.speed // 2

