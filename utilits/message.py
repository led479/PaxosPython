from enum import Enum

class Message(Enum):
    acceptorsCreate = "acceptors foram criados."
    proposer = "proposer"
    message = "message"
    prepareResponse = "Prepare Response"
    noPrevious = "no previous"
    prepareRequest = "Prepare Request"
