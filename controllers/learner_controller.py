from utilits.message import Message
from models.learner import Learner
from utilits.message import Message
import collections


class LearnerController:
  
    def __init__(self, main_controller):
        self.mc = main_controller
        self.learners = []

    def generate_id(self):
        if not self.learners:     # Se a lista de learners estiver vazia
          return 200
        else:
          return self.learners[-1].id + 1    # Pega o número do último learner da lista e incrementa em 1
  
    def create_learner(self):
        learner = Learner(self, self.generate_id())
        self.learners.append(learner)

    def accepted_paxos(self, accepted_values):
        print(accepted_values)
        for learner in self.learners:
            values = []
            for accepted_value in accepted_values:
                values.append(accepted_value['Accepted'])
            
            # Conta quais os valores que mais aparecem na lista
            counter = collections.Counter(values)
            most_accepted_values = list(counter.keys())

            # Pega o valor que apareceu mais vezes
            value = most_accepted_values[0]

            if counter[value] >= self.mc.ac.min_accept_request():
                print(f"Learner {learner.id} aceitou o valor {value}")
            else:
                print(f"Learner {learner.id} não aceitou nenhum valor")
        
                
                