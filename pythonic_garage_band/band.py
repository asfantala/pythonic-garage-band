from abc import ABC, abstractmethod

class Band: 
    instances =[]
    def __init__(self,name,members) :
        self.name=name  
        self.members=members or []
        Band.instances.append(self)

    def __str__(self): 
        return self.name
    
    def __repr__(self): 
        return f"Band instance. Name = {self.name}"
    
    def play_solos (self):
        solos = []
        for member in self.members:
            solo = member.play_solo()
            solos.append(solo)
        return solos
    @classmethod
    def to_list(cls):
         return cls.instances

class Musician (ABC):
    def __init__(self,name) :
        self.name=name  


class Guitarist (Musician):
    def __init__(self, name):
        super().__init__(name)

    def get_instrument(self):
            return "guitar"
    
    def play_solo(self):
         return "face melting guitar solo"

    def __str__(self): 
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist (Musician):
    def __init__(self, name):
        super().__init__(name)

    def get_instrument(self):
            return "bass"
    def play_solo(self):
         return "bom bom buh bom"
     
    def __str__(self): 
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    
class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
    def get_instrument(self):
            return "drums"
    def play_solo(self):
         return "rattle boom crash"
    def __str__(self): 
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    
