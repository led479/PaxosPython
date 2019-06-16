from models.learner import Learner
from utilits.message import Message


class LearnerController:
  
    def __init__(self, main_controller):
        self.mc = main_controller
        self.learners = []

    def generate_id(self):
        if not self.learners:     # Se a lista de acceptors estiver vazia
          return 200
        else:
          return self.learners[-1].id + 1    # Pega o número do último acceptor da lista e incrementa em 1
  
    def create_learner(self):
        learner = Learner(self, self.generate_id())
        self.acceptors.append(acceptor)

    def accepted_paxos(self, accepted_value):
        pass

