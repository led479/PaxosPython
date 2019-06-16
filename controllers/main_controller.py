from controllers.learner_controller import LearnerController
from controllers.acceptor_controller import AcceptorController
from controllers.proposer_controller import ProposerController


class MainController:

  def __init__(self):
    self.ac = AcceptorController(self)
    self.pc = ProposerController(self)
    self.lp = LearnerController(self)