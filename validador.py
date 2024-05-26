import datetime

class Validador:
    def validarFecha(self,fecha):
        try:
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
            return True
        except:
            return False
    
    def isEmpty(self,data):
        if data.strip() == "":
            return False
        else:
            return True
    
    def isNumber(self,data):
        if type(data) == 'int':
            return True
        else:
            return False
        
    def isPositive(self,data):
        if data > 0:
            return True
        else:
            return False
        
    def isMoney(self,data):
        if self.isNumber(data):
            if self.isPositive(data):
                return True
            else:
                return False
        else:
            return False