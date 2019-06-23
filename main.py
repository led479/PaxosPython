from controllers.main_controller import MainController
from time import sleep

valor_para_validar = 8
mc = MainController()

mc.lp.create_learner()
print(f"1 learner foi criado.\n")

i = 0
while (i < 20):
  mc.ac.create_acceptor()
  i += 1
print(f"{len(mc.ac.acceptors)} acceptors foram criados.\n")

j = 1
while j <=5:
    mc.pc.proposers = []
    i = 0
    while i < 10:
      mc.pc.create_proposer(valor_para_validar)
      sleep(0.01)
      i += 1

    mc.pc.prepare_request() # Mudar isso depois
    mc.pc.accept_request() # Mudar isso depois
    j +=1
