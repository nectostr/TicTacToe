import numpy as np


class CrossGame:

    def __init__(self, _size=3):
        self.field_length = _size
        self.field_size = self.field_length ** 2
        self.free_places = {i for i in range(1,self.field_size+1)}
        self.field = np.arange(1, self.field_size + 1)
        self.field = self.field.reshape((self.field_length, self.field_length))
        self.field = np.array(self.field, dtype=str)
        self.win = False


    def _print_field(self):
        global field
        global field_length
        res = ""
        sep = "-" * (2 * field_length+1) + "\n"
        res += sep
        for i in field:
            for j in i:
                if j == "x" or j == "y":
                    res += "|x"
                else:
                    res += "| "
            res += "|\n"
            res += sep
        return res


    def _get_data(self):
        retry_count = 5
        user_inp = "none"
        while user_inp not in self.free_places:
            user_inp = input(f"Enter number from 1 to {self.field_size}:\n")
            while not user_inp.isdigit():
                print("Comon, it is not a number")
                user_inp = input(f"Enter number from 1 to  {self.field_size}:\n")
                retry_count -= 1
                if retry_count < 0:
                    print("Too much stupid tries, i'll choose by myself")
                    user_inp = np.random.choice(list(self.free_places))
                    return user_inp

            user_inp = int(user_inp)
            if retry_count < 0:
                print("Too much stupid tries, i'll choose by myself")
                user_inp = np.random.choice(list(self.free_places))
                return user_inp
            if user_inp > self.field_size:
                print(f"Number is too large, closest - {max(self.free_places)}")
            elif user_inp < 1:
                print(f"Number is too small, closest - {min(self.free_places)}")
        return user_inp


    def _step(self, whom="x"):
        print(f"It is {whom} move now")
        # print(print_field())
        print(self.field)
        inp = self._get_data()
        self.field[(inp-1) // self.field_length, (inp-1) % self.field_length] = whom
        self.free_places = self.free_places - {inp}


    def _check_win(self, whom):
        for i in self.field:
            if all(i == whom):#.sum() >= self.field_length:
                print(f"{whom} wins, great")
                return True
        for i in self.field.T:
            if all(i == whom):# >= self.field_length:
                print(f"{whom} wins, great")
                return True
        if all(self.field.diagonal() == whom):# >= self.field_length:
            print(f"{whom} wins, great")
            return True
        if all(np.diag(np.fliplr(self.field)) == whom):# >= self.field_length:
            print(f"{whom} wins, great")
            return True
        return False


    def start_game(self):
        while not self.win:
            self._step("x")
            self.win = self._check_win("x")
            if not self.free_places and not self.win:
                print("No one wins")
                break
            if not self.win:
                self._step("o")
                self.win = self._check_win("o")
                if not self.free_places and not self.win:
                    print("No one wins")
                    break


if __name__ == '__main__':
    gm = CrossGame()
    gm.start_game()