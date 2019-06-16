from enum import Enum

class Message(Enum):
    acceptorsCreate = "acceptors foram criados."
    proposer = "proposer"
    message = "message"
    prepareResponse = "Prepare Response"
    prepareRequest = "Prepare Request"
    noPrevious = "no previous"
    acceptRequest = "Accept Request"
    accepted = "Accepted"
    accepeted_value = "Accepetd value: v:"
    no_consensus = "Não houve consenso dos acceptors na escolha de valor v."
