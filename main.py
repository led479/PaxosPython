from controllers.main_controller import MainController
from time import sleep
from utilits.message import Message

valor_para_validar = 8
mc = MainController()

i = 0
while (i < 2):
  mc.ac.create_acceptor()
  i += 1
print(f"{len(mc.ac.acceptors)} {Message.acceptorsCreate.value}")

i = 0
while i < 3:
  mc.pc.create_proposer(valor_para_validar)
  sleep(0.25)
  i += 1


mc.pc.prepare_request() # Mudar isso depois
mc.pc.accept_request() # Mudar isso depois

# Proposers enviar prepare_request para todos os acceptors


#mc.ac.acceptors[0].set_greater_proposer(mc.pc.proposers[0])
#mc.pc.proposers[0].prepare_request()

#mc.ac.acceptors[0].set_greater_proposer(mc.pc.proposers[0])
#print(mc.ac.acceptors[0].greater_proposer)


