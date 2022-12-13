class Unidade:
    def __init__(self, v, uc, e):
        self.valor = v
        self.const = uc
        self.exp = e

    def converter(self,u2, p2):
        prop = u2/self.const
        pot = p2-self.exp
        valor = self.valor*prop*(10**pot)
        return round(valor,4)