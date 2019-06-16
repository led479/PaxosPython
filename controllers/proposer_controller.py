from models.proposer import Proposer
from utilits.message import Message


class ProposerController:

  def __init__(self, main_controller):
    self.mc = main_controller
    self.proposers = []

  def proposal_number(self):
    # Proposer pode ser aleatório CORRIGIR
    if len(self.proposers) == 0:
      return 40 #1
    #return self.proposers[-1].n + 1
    return self.proposers[-1].n + 1
  
  def create_proposer(self, v):
    proposer = Proposer(self, self.proposal_number(), v)
    self.proposers.append(proposer)

# Cada proposer envia prepare_request aos acceptors
  def prepare_request(self):
    for proposer in self.proposers: # Também é possivel fazer para cada proposer assim que for criado chamar esse método.
       
       request = {
           Message.message.value: Message.prepareRequest.value,
           Message.proposer.value: {
                                   'n': proposer.n,
                                   'v': proposer.v
                                   }
       }
       responses = self.mc.ac.prepare_response(request)
       proposer.responses = responses

   # Verifica se a maioria dos acceptores (metade +1) concordaram com a response
  def accept_request(self):
    for proposer in self.proposers: 
        
        min_accept_request = self.mc.ac.min_accept_request() # Metade dos acceptors devem ter respondido prepare request com prepare response

        #Verifica se a maioria dos acceptores respondeu ao prepare request
        if len(proposer.responses) >= min_accept_request:
            for response in proposer.responses:
                
                # no previus, acceptor aceitou a request pois nao haviam outras propostas
                if response['proposer'] != Message.noPrevious.value:
                    v_response = response['proposer']['v'] #Armazena o valor de v recebido no prepare response do acceptor
                    
                    # Proposer atualiza seu valor com o maior v recebido pelos acceptors
                    if v_response > proposer.v:
                        proposer.v = v_response;
                    
            # Prepara Messagem accept request
            accept = {
                Message.message.value : Message.acceptRequest.value,
                Message.proposer.value : {
                                        'n': proposer.n,
                                        'v': proposer.v
                                         } 
                }                
        
            # Depois de atualizado o valor do proposer ele solicita accepted aos acceptors
            self.mc.ac.accepted(accept)