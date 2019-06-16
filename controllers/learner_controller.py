from utilits.message import Message
from models.learner import Learner
from utilits.message import Message


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
        for learner in self.learners:
            first_value = accepted_values[0]['Accepted'] # Pega primeiro valor do primeiro accept para compara com os deamais
            count_value = 1 # Conta quantos valores iguais foram encontrados
            for accepted_value in accepted_values:
                if accepted_value['Accepted'] == first_value:
                    count_value +=1
                # Verifica quantidade de valores iguais é igual ou maior que a quantidade de respostas minimas, maioria consenso
                if count_value >= self.mc.ac.min_accept_request():
                    print(f"{Message.accepeted_value.value}{accepted_value['Accepted']}")
                    break
                    
