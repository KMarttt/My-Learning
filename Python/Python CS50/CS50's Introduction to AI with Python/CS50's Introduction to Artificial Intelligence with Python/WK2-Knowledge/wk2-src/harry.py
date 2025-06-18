from logic import *

rain = Symbol("rain") # it rains
hagrid = Symbol("hagrid") # harry visits hagrid
dumbledore = Symbol("dumbledore") # harry visits dumbledore

knowledge = And(
    Implication(Not(rain), hagrid), # if it did not rain then harry will visit hagrid
    Or(hagrid, dumbledore), # harry can visit hagrid or dumbledore
    Not(And(hagrid, dumbledore)), # but harry cannot visit both hagrid and dumbledore at the same time
    dumbledore # harry visited dumbledore
)

print(model_check(knowledge, rain))
