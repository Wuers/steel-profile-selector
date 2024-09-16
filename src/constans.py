def constantE(E):
    def Eset(self, value):
        raise TypeError("Cannot modify constant value")
    def Eget(self):
        return E()
    return property(Eget, Eset)

class __Const(object):
    @constantE
    def E():
        return 25000

CONST = __Const()

print(CONST.E)