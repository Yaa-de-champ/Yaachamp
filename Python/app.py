

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


# %%
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

#The file is encoded using ISO-8859-1 character encoding, which is a standard way of representing characters in the file.
#We defined data type of specific columns such as (Div1Airport, Div1TailNum, Div2Airport, and Div2TailNum) to be strings, which ensures that these columns are read as text instead of numbers.
airline_dataset = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
                                encoding='ISO-8859-1',
                                dtype={'Div1Airport':str, 'Div1TailNum':str, 'Div2Airport':str, 'Div2TailNum':str})

#create a dash aplication layout
app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('Total number of flights to the destination state split by reporting airline',
                                        style={'textAlign':'center','color':'#503D36', 'font-size':40}),
                                html.Div(['Input Year: ', dcc.Input(id = 'input-year', value='2010',
                                                                    type='number', style={'height':'50px', 'font-size':35}),],
                                style={'font-size':40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id = 'bar-plot')),
                                ])

#adding callback decorator
@app.callback( Output(component_id='bar-plot', component_property='figure'), 
                Input(component_id='input-year', component_property='value'))

#add computation to callback function and return graph
def get_graph(entered_year):

    
        df =  airline_dataset[airline_dataset['Year']==int(entered_year)]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        bar_data = df.groupby('DestState')['Flights'].sum().reset_index()
        fig = px.bar(bar_data, x= "DestState", y= "Flights", title='Total number of flights to the destination state split by reporting airline') 
        fig.update_layout(title='Flights to Destination State', xaxis_title='DestState', yaxis_title='Flights')
        return fig

#-------------------------------------------------or------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        # bar_data = df.groupby('DestState')['Flights'].sum().reset_index()
        # fig = px.bar(bar_data, x= "DestState", y= "Flights", title='Total number of flights to the destination state split by reporting airline') 
        # fig.update_layout(title='Total number of flights to the destination state split by reporting airline', xaxis_title='States', yaxis_title='Flights')
        # return fig

#run the app
if __name__ == '__main__':
    app.run()




# %%
