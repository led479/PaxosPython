from controllers.proposer_controller import ProposerController
    
c = ProposerController()

c.create_proposer(10)

print(c.proposers[0].n)
print(c.proposers[0].v)

  
  

