from models.proposer import Proposer

class ProposerController:

  def __init__(self):
    self.proposers = []

  def proposal_number(self):
    if not self.proposers:     # Se a lista de proposers estiver vazia
      return 1
    else:
      return self.proposers[-1].n + 1    # Pega o número do último proposer da lista e incrementa em 1
  
  def create_proposer(self, v):
    proposer = Proposer(self.proposal_number(), v)
    self.proposers.append(proposer)

  

  
      