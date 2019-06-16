from models.acceptor import Acceptor
from utilits.message import Message

class AcceptorController:

  def __init__(self, main_controller):
    self.mc = main_controller
    self.acceptors = []

  def generate_id(self):
    if not self.acceptors:     # Se a lista de acceptors estiver vazia
      return 100
    else:
      return self.acceptors[-1].id + 1    # Pega o número do último acceptor da lista e incrementa em 1
  
  def create_acceptor(self):
    acceptor = Acceptor(self, self.generate_id())
    self.acceptors.append(acceptor)

  def prepare_response(self, proposer):
    for acceptor in self.acceptors:
      greater_proposer = acceptor.greater_proposer
      
      # Se acceptor não conter nenhuma outra proposta ele guarda e envia um prepare reponse
      if greater_proposer == {}:
        acceptor.set_greater_proposer(proposer)
        response = {
            Message.message.value: Message.prepareResponse,
            Message.proposer: Message.noPrevious.value
        }
        
        # Se o acceptor ja tiver uma proposta ele fica com a maior
      else:
        
          # Se há proposta recebida for maior ele fica com ela e reponde ao proposer a proposta cujo valor é menor
        if proposer.n > greater_proposer["n"]:
            response = {
            Message.message.value: Message.prepareResponse,
            Message.proposer: acceptor.greater_proposer # Atualizar valor da maior proposta
            }
            acceptor.set_greater_proposer(proposer)
        else:
            
            # Se a nova proposta for menor é ignorada
            response = None
      proposer.responses.append(response) 
  
  def accepted(self, proposer):
        pass

