from controllers.main_controller import MainController
from time import sleep
    
valor_para_validar = 8
mc = MainController()

i = 0
while (i < 3):
  mc.ac.create_acceptor()
  i += 1
print(f"{len(mc.ac.acceptors)} acceptors foram criados")

i = 0
while i < 3:
  mc.pc.create_proposer(valor_para_validar)
  sleep(0.25)
  i += 1


# Proposers enviar prepare_request para todos os acceptors
mc.pc.prepare_request()

#mc.ac.acceptors[0].set_greater_proposer(mc.pc.proposers[0])
#mc.pc.proposers[0].prepare_request()

#mc.ac.acceptors[0].set_greater_proposer(mc.pc.proposers[0])
#print(mc.ac.acceptors[0].greater_proposer)

