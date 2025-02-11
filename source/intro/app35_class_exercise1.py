import json
import random

class poststed_generator:
    
    _FILENAME = '../datafiles/postnummer.json'
        
    def __init__(self):        
        self._postnummer_register = None;
        
    def _read_data (self):
        print ("loading data")
        pass     
            
    def get_random_poststed(self):
        pass
    
    def get_poststed(self, postnr):
        pass
        
        
        
pnr_gen = poststed_generator()

print (pnr_gen.get_poststed('5235'))
print (pnr_gen.get_poststed('5995'))
print (pnr_gen.get_poststed('2020'))

(postnr, poststed) = pnr_gen.get_random_poststed()
print (postnr, poststed)

(postnr, poststed) = pnr_gen.get_random_poststed()
print (postnr, poststed)

(postnr, poststed) = pnr_gen.get_random_poststed()
print (postnr, poststed)