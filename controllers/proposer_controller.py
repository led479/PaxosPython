from models.proposer import Proposer
from utilits.message import Message
import math


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
       self.mc.ac.prepare_response(proposer)
   
   # Verifica se a maioria dos acceptores (metade +1) concordaram com a response
  def accept_request(self):
    for proposer in self.proposers: # Também é possivel fazer para cada proposer assim que for criado chamar esse método.
        
        no_response = proposer.responses.count(None) #Verifica se algum acceptor não respondeu, ignorou a solicitação
        min_accept_request = math.floor(len(self.mc.ac.acceptors) / 2 + 1) # Metade dos acceptors devem ter respondido prepare request
        
        #Verifica se a maioria dos acceptores respondeu ao prepare request
        if min_accept_request > no_response:
            for response in proposer.responses:
                # no previus, acceptor aceito a request pois nao haviam outras propostas
                if response['proposer'] != Message.noPrevious.value:
                    v_response = response['proposer']['v'] #Armazena o valor de v 
                    # Proposer atualiza seu valor com o maior v recebido pelos acceptors
                    if v_response > proposer.v:
                        proposer.v = v_response;
        
        # Depois de atualizado o valor do proposer ele solicita accepted aos acceptors
        self.mc.ac.accepted(proposer)