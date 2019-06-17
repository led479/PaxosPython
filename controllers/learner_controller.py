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
            count_value_equals = 0 # Conta quantos valores iguais foram encontrados
            position_list = 0 # Conta posição na lista de valores recebidos
            total_values = len(accepted_values) # Armazena a quantidade de valores que
            i = 0
            
            for accepted_value in accepted_values:
                if accepted_value['Accepted'] == first_value:
                    count_value_equals +=1
                
                position_list +=1    # Adiciona a quantidade de elementos percorridos na lista
                min_acceptors_response = self.mc.ac.min_accept_request() # Armazena a quantidade minima de acceptors que devem responder ao prepare request

                # Verifica quantidade de valores iguais é igual ou maior que a quantidade de respostas minimas, maioria consenso
                if count_value_equals >= min_acceptors_response:
                    print(f"{Message.accepeted_value.value}{accepted_value['Accepted']}")
                    break
                
                lack_elements = total_values - position_list # Armazena a quantidade de elementos restantes da lista (falta para acabar)
                lack_response = min_acceptors_response - count_value_equals # Armazena a quantidade de respostas que falta para v ser aceito pelo paxos

                # Se quantidade de respostas que falta para v ser aceito for menor que a quantidade de elementos na lista
                if lack_elements < lack_response:
                    if i == total_values:
                        print(F"{Message.no_consensus.value}")
                    else:
                        i+=1 
                        first_value = accepted_value[i]['Accepted']
                    