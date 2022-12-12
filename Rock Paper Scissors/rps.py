moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        import random
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        PlayerChoose = input("rock, paper, scissors? > ").lower()
        if PlayerChoose not in moves:
            return self.move()
        else:
            return PlayerChoose


class ReflectPlayer(Player):
    PredictPlayer = 'rock'

    def move(self):
        return self.PredictPlayer

    def learn(self, my_move, their_move):
        if their_move == 'paper':
            self.PredictPlayer = 'paper'
        elif their_move == 'rock':
            self.PredictPlayer = 'rock'
        elif their_move == 'scissors':
            self.PredictPlayer = 'scissors'
        #self.PredictPlayer = their_move


class CyclePlayer(Player):
    RunningCycle = 'rock'

    def move(self):
        return self.RunningCycle

    def learn(self, my_move, their_move):
        if my_move == 'rock':
            self.RunningCycle = 'paper'
        elif my_move == 'paper':
            self.RunningCycle = 'scissors'
        elif my_move == 'scissors':
            self.RunningCycle = 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.one1 = 0
        self.two2 = 0

    def play_round(self):
        self.move1 = self.p1.move()
        self.move2 = self.p2.move()
        self.p1.learn(self.move1, self.move2)
        self.p2.learn(self.move2, self.move1)
        print(f"You played {self.move1}.")
        print(f"Opponent played {self.move2}.")
        if beats(self.move1, self.move2):
            self.one1 += 1
            print("** PLAYER ONE WIN **")
        elif beats(self.move2, self.move1):
            self.two2 += 1
            print("** PLAYER TWO WIN **")
        else:
            print("** TIE **")
        print(f"Score: Player One {self.one1}, Player Two {self.two2}")

    def play_game(self):
        print("Rock Paper Scissors, Go!")
        for round in range(3):
            print(f"\nRound {round} --")
            self.play_round()


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()