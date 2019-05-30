from random import randint

class Proposer:

  def __init__(self, proposer_controller, n, v):
    self.pc = proposer_controller
    self.n = n

    # o Proposer tem a probabilidade de 10% de ser criado com o valor errado
    random = randint(1, 10)
    if random == 5:
      self.v = v + random
    else:
      self.v = v
    
    print(f"Proposer criado (n: {self.n} v: {self.v})\n")

  def prepare_request(self):
    for acceptor in self.pc.mc.ac.acceptors:
      print(acceptor)