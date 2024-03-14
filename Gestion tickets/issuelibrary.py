class issue():
    def __init__(self,id=0,nom=None,category=None,problem=None,descrition=None) :
        self.id=id
        self.nom=nom
        self.category=category
        self.problem=problem
        self.descrition=descrition
    def getID(self):
        return self.id
    def getNom(self):
        return self.nom
    def getcategory(self):
        return self.category
    def getproblem(self):
        return self.problem
    def getdescription(self):
        return self.descrition
    def setId(self,id):
        self.id=id
    def setNom(self,nom):
        self.nom=nom
    def setcategory(self,category):
        self.category=category
    def setproblem(self,problem):
        self.problem=problem   
    def setdescrition(self,descrition):
        self.descrition=descrition  
    def __str__(self):
        return('{}{}{}{}{}'.format(self.id,self.nom,self.category,self.problem,self.descrition))