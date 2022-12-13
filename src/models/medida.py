from src.utils.functions import convertZeros
class Unidade:
    def __init__(self, v, u, uc, e):
        self.valor = v
        self.const = uc
        self.exp = e
        self.unit = u

    def converter(self, uc2, p2, u2):
        prop = uc2/self.const
        pot = (convertZeros(u2)*p2)-(convertZeros(self.unit)*self.exp)
        valor = self.valor*prop*(10**pot)
        return round(valor,4)