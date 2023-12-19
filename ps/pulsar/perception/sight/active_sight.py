


class Vision:
    def __init__(self, robot_name, robot_age):
        self.robot_name = robot_name
        self.robot_age = robot_age

    def config(self):
        print(f"This robots name is: {self.robot_name}, and he is {self.robot_age} years old")
