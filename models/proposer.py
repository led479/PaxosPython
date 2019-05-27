from random import randint

class Proposer:

  def __init__(self, n, v):
    self.n = n

    # o Proposer tem a probabilidade de 10% de ser criado com o valor errado
    random = randint(1, 10)
    if random == 5:
      self.v = v + random
    else:
      self.v = v
    
    print(f"Proposer criado (n: {self.n} v: {self.v})\n")