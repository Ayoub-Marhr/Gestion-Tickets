class admin():
    def __init__(self,id=0,nom=None,password=None) :
        self.id=id
        self.nom=nom
        self.password=password
    def getID(self):
        return self.id
    def getNom(self):
        return self.nom
    def getPassword(self):
        return self.password
    def setId(self,id):
        self.id=id
    def setNom(self,nom):
        self.nom=nom
    def setPassword(self,password):
        self.password=password
    def __str__(self):
        return('{}{}{}'.format(self.id,self.nom.self.password))