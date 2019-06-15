class Acceptor:

  def __init__(self, acceptor_controller, id):
    self.ac = acceptor_controller
    self.id = id
    self.greater_proposer = {}

  def set_greater_proposer(self, proposer):
    self.greater_proposer = {
      'n': proposer.n,
      'v': proposer.v
    }

