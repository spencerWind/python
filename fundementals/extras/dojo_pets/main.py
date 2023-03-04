from ninja import Ninja
from pet import Pet, Dog, Cat
        
sensei = Ninja('Master', 'Oogway', 'biscuits', 'kibble', Pet('Skylar', ['sit','stay','shake']))

sensei.feed().walk().bathe()

print(sensei.pet.health)

testNinja = Ninja('Spencer', 'Wind', 'cheerios', 'kibble', Dog('teddy','sit'))

print(testNinja.pet.pet_sound)