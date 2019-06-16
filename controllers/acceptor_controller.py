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

  def prepare_response(self, request):
    # Armazena as repostas de cada acceptor, para ser enviada ao proposer
    responses = [] 
    
    # Extrai da menssagem Prepare Response o n e v da proposta
    request_proposer = request['proposer'] 
    
    for acceptor in self.acceptors:
      # Armazena a maior proposta conhecida pelo acceptor
      greater_proposer = acceptor.greater_proposer
      
      # Se acceptor não conter nenhuma outra proposta ele guarda a proposta e envia um prepare reponse com no previous
      if greater_proposer == {}:
        acceptor.set_greater_proposer(request_proposer)
        # Prepara a mensagem de reposta
        response = {
            Message.message.value: Message.prepareResponse,
            Message.proposer.value: Message.noPrevious.value
        }
        
      else: # Se o acceptor ja tiver uma proposta ele fica com a maior
        
          # Se há proposta recebida for maior, ele fica com ela e reponde ao proposer a proposta cujo n é menor
        if request_proposer['n']> greater_proposer['n']:
            # Prepara a mensagem de reposta
            response = {
            Message.message.value: Message.prepareResponse,
            Message.proposer.value: {
                                'n': acceptor.greater_proposer['n'], # Devolve a proposta cujo n é inferior ao recebido
                                'v': acceptor.greater_proposer['v']  
                              }
            }
            # Acceptor atualiza seu maior valor de proposta recebido
            acceptor.set_greater_proposer(request_proposer)
        else:
            # Se a nova proposta for menor é ignorada
            response = None
      responses.append(response) #Armazena a resposta do acceptor para o proposer recebido
    return responses # Retorna ao proposer prepare response de todos os acceptors

  def accepted(self, accept):
        pass

