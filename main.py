from controllers.proposer_controller import ProposerController
    
valor_para_validar = 8
c = ProposerController()
i = 0
while i < 20:
  c.create_proposer(valor_para_validar)
  i += 1

for p in c.proposers:
  print(p.v)


  
  

