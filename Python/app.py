

# # ----------------------------------------------rock scissors paper game----------------------------------
# class Participant:
#     def __init__(self):
#         self.points = 0
#         self.choice = ""
    
# # class GameRound:
# class Game:
#     def __init__(self):
#         self.endgame = False
#         self.participant = Participant()
#         self.secondparticipant = Participant()

    
# # class Square:
# #      def __init__(self):
# #          self.height = 2
# #          self.width = 2
# #      def set_side(self, new_side):
# #          self.height = new_side
# #          self.width = new_side

# # square = Square()
# # square.height = 3 # not a square anymore


# class Square:
#       def __init__(self):
#           self.__height = 2
#           self.__width = 2
#       def set_side(self, new_side):
#           self.__height = new_side
#           self.__width = new_side

# square = Square()
# square.__height = 3 # raises AttributeError

# class Square:
#       def __init__(self):
#           self.__height = 2
#           self.__width = 2
#       def set_side(self, new_side):
#           self.__height = new_side
#           self.__width = new_side
#       def get_height(self):
#           return self.__height
#       def set_height(self, h):
#           if h >= 0:
#               self.__height = h
#           else:
#               raise Exception("value needs to be 0 or larger")

# square = Square()
# square.__height = 3 # raises AttributeError

class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        self.choice = input("{name}, select rock, paper or scissor: ".format(name= self.name))
        print("{name} selects {choice}".format(name=self.name, choice = self.choice))

class GameRound:
    def __init__(self, p1, p2):
        p1.choose()
        p2.choose()
    def compareChoices(self):
        print("implement")
    def awardPoints(self):
        print("implement")

class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")
    def start(self):
        game_round = GameRound(self.participant, self.secondParticipant)

    def checkEndCondition(self):
        print("implement")
    def determineWinner(self):
        print("implement")

game = Game()
game.start()