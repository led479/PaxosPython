from models.proposer import Proposer

class ProposerController:

  def __init__(self, main_controller):
    self.mc = main_controller
    self.proposers = []

  def proposal_number(self):
    # Proposer pode ser aleatório CORRIGIR
    if len(self.proposers) == 0:
      return 1
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
      pass