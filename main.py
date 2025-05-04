class RowingBoat:

    def __init__(self, max_weight, total_hooks):
        self.__max_weight = max_weight
        self.__total_hooks = total_hooks
        self.__current_free_hooks = total_hooks
        self.__current_weight = 0
        self.in_water = False
        self.__paddles = []

    def is_afloat(self):
        return (self.__max_weight > self.__current_weight) or not self.in_water

    def get_current_free_hooks(self):
        return self.__current_free_hooks

    def sail(self, sail_times):
        for _ in range(0, sail_times):
            for i in self.__paddles:
                i.row()

    def add_paddle(self, new_paddle):
        if not isinstance(new_paddle, Paddle):
            raise TypeError("Only Paddle-type object can be added!")
        self.__paddles.append(new_paddle)
        if self.__current_free_hooks:
            self.__current_free_hooks -= 1

    def remove_paddle(self, paddle):
        if not isinstance(paddle, Paddle):
            raise TypeError("Only Paddle-type object can be removed!")
        self.__paddles.remove(paddle)
        if self.__current_free_hooks < self.__total_hooks:
            self.__current_free_hooks += 1

    def add_weight(self, weight):
        if weight > 0:
            self.__current_weight += weight
        else:
            raise ValueError("Value must be positive!")

    def remove_weight(self, weight):
        if weight > 0:
            self.__current_weight -= weight
        else:
            raise ValueError("Value must be positive!")

class Paddle:
    def row(self):
        print("Plop!")