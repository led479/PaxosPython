class Acceptor:

  def __init__(self, acceptor_controller, id):
    self.ac = acceptor_controller
    self.id = id
    self.greater_proposer = {}

  def set_greater_proposer(self, request_proposer):
    self.greater_proposer = {
      'n': request_proposer['n'],
      'v': request_proposer['v']
    }

