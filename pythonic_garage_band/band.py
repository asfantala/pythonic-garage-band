from abc import ABC, abstractmethod

class Band:
    """
    instances to track of all Band instances created
    __init__ to Initialize a new instance of the Band
    __str__ Returns the name of the band as a string.
    __repr__ Returns a string representation of the Band instance.
    play_solos(s: Returns a list of solos played by the band's members.
    to_list(cls): Returns a list of all Band instances created
    """    
 
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
    """
    __init__ Initializes a new instance of the Musician class with the specified name.
    
    """
    def __init__(self,name) :
        self.name=name 
    def __str__(self): 
        return self.name
    
    def __repr__(self): 
        return f"Musician . Name = {self.name}" 


class Guitarist (Musician):
    """
     __init__ Initializes a new instance of the Guitarist class with the specified name.
     get_instrument  Returns the instrument played by the guitarist, which is the guitar.
     play_solo(self): Plays a face melting guitar solo.
     __str__(self): Returns a string representation of the Guitarist instance.
     __repr__(self): Returns a string representation of the Guitarist instance.
    
    """
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
    """
     __init__ Initializes a new instance of the Bassist class with the specified name.
     get_instrument  Returns the instrument played by the Bassist, which is the bass.
     play_solo(self): Plays a bom bom buh bom.
     __str__(self): Returns a string representation of the Bassist instance.
     __repr__(self): Returns a string representation of the Bassist instance.
    
    """
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

    """
     __init__ Initializes a new instance of the Drummer class with the specified name.
     get_instrument  Returns the instrument played by the Drummer, which is the bass.
     play_solo(self): Plays a rattle boom crash.
     __str__(self): Returns a string representation of the Drummer instance.
     __repr__(self): Returns a string representation of the Drummer instance.
    
    """
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
    
