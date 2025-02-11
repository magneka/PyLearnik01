import random
          
class uc_faker: 
    _FILENAME_FORNAVN = '../datafiles/ordliste_ssb_norske_fornavn.txt'
    _FILENAME_ETTERNAVN = '../datafiles/ordliste_ssb_norske_etternavn.txt'
    _FILENAME_GATERBG = '../datafiles/GateNavnBg.txt'
    _FILENAME_FIRMANAVN = '../datafiles/fake_companies.txt'
        
    def __init__(self):        
        self._fornavn = None
                
    def _read_fornavn (self):
        pass
                
    def get_fornavn(self):
       pass
       
       
faker = uc_faker();
print (faker.get_fornavn())
print (faker.get_fornavn())

#print (faker.get_etternavn())
#print (faker.get_etternavn())

#print (faker.get_gatenavn())
#print (faker.get_gatenummer())
#print (faker.get_gatenummer())
#print (faker.get_gatenummer())

#print (faker.get_gateadresse())



#rint (f'{faker.get_fornavn()} {faker.get_etternavn()}')