from models.proposer import Proposer

class ProposerController:

  def __init__(self, main_controller):
    self.mc = main_controller
    self.proposers = []

  def proposal_number(self):
    if len(self.proposers) == 0:
      return 1
    return self.proposers[-1].n + 1
  
  def create_proposer(self, v):
    proposer = Proposer(self, self.proposal_number(), v)
    self.proposers.append(proposer)

  