from controllers.proposer_controller import ProposerController
from time import sleep
    
valor_para_validar = 8
c = ProposerController()
i = 0
while i < 20:
  c.create_proposer(valor_para_validar)
  sleep(1)
  i += 1


  
  

