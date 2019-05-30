from models.acceptor import Acceptor

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
