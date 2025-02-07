from dataclasses import Dataclass

@Dataclass
class Dataclass:
    matizp : object
    context : str
    fname : str
    id : str
    label : str 



    @property
    def matzip(self) -> object:
        return self._matzip
    
    @matzip.setter
    def matzip(self, matzip):
        self._matzip = matzip



    @property
    def context(self) -> str:
        return self._context
    
    @context.setter
    def context(self, context):
        self._context = context 


    @property
    def fname(self) -> str:
        return self._fname
    
    @fname.setter
    def fname(self, fname):
        self._fname = fname 


    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id 


    @property
    def lebal(self) -> str:
        return self._lebal
    
    @lebal.setter
    def lebal(self, lebal):
        self._lebal = lebal 
         
        