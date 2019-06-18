from controllers.main_controller import MainController
from time import sleep
from utilits.message import Message

valor_para_validar = 8
mc = MainController()

mc.lp.create_learner()
print(f"1 learner foi criado.")

i = 0
while (i < 20):
  mc.ac.create_acceptor()
  i += 1
print(f"{len(mc.ac.acceptors)} acceptors foram criados.")

i = 0
while i < 10:
  mc.pc.create_proposer(valor_para_validar)
  sleep(0.01)
  i += 1



mc.pc.prepare_request() # Mudar isso depois
mc.pc.accept_request() # Mudar isso depois
#
#i =1
#accepted_values = []
#while i < 21:
#    accepted_value = {
#                    Message.message.value: Message.accepted.value, 
#                    Message.accepted.value: 15
#                 }
#    i+=1
#    accepted_values.append(accepted_value)
#
#accepted_values.append({
#                    Message.message.value: Message.accepted.value, 
#                    Message.accepted.value: 11
#                 })
#accepted_values.append({
#                    Message.message.value: Message.accepted.value, 
#                    Message.accepted.value: 11
#                 })
#accepted_values.append({
#                    Message.message.value: Message.accepted.value, 
#                    Message.accepted.value: 11
#                 })
#accepted_values.append({
#                    Message.message.value: Message.accepted.value, 
#                    Message.accepted.value: 11
#                 })
#accepted_values.append({
#                    Message.message.value: Message.accepted.value, 
#                    Message.accepted.value: 11
#                 })
#
#

#mc.lp.accepted_paxos(accepted_values)