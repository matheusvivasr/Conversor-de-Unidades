from gi import require_version as Gtk_version
Gtk_version("Gtk", "3.0")

from gi.repository import Gtk
from src.models.medida import Unidade
from src.utils.functions import lerMedidas, lerPotencias,pegarTipos

def ligar(nome):
    ligar = BoraMofio(nome)
    Gtk.main()

class BoraMofio: 
    def __init__(self,name:str):
    #   Gtk iniciadores
        self.builder = Gtk.Builder()
        fileName = 'src/scripts/'+name+'.glade'
        self.builder.add_from_file(fileName)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('janela')  
        self.window.show()

    #   setando tipos de unidades disponíveis
        self.uTipos = self.builder.get_object('unit_type')
        self.list = Gtk.ListStore(str)
        for n in pegarTipos():
            self.list.append([n.capitalize()])
        self.comboText(self.uTipos,self.list,-1)

    #   unidades
        self.unitInput = self.builder.get_object('unit_in')
        self.unitOutput = self.builder.get_object('unit_out')

    #   ordem de grandeza   
        self.pows = lerPotencias()
        self.powInput = self.builder.get_object('pow_in')
        self.powOutput = self.builder.get_object('pow_out')

    #   valores
        self.numInput = self.builder.get_object('value_in')
        self.numOutput = self.builder.get_object('value_out')

    def distruiu(self, *args):Gtk.main_quit()
    
#   funcao para atualizar o setstore (usada para cada um dos 4 comboBox)
    def comboText(self,combo,store,n):
        combo.set_model(store)
        renderer_text = Gtk.CellRendererText()
        combo.pack_start(renderer_text, True)
        combo.add_attribute(renderer_text, "text", 1)
        combo.set_active(n)

#   usada para setar as medidas a partir do tipo de medida selecionado em cima
#       comprimento: metro, milha, polegada etc
    def mudou(self, box):

        self.numInput.set_text('')
        self.numOutput.set_text('')
        self.powOutput.set_active(-1)

        unitType = box.get_active_text()
        self.liststore = Gtk.ListStore(str)
        self.units = lerMedidas(unitType.lower())
        for n in self.units.index.values:
            self.liststore.append([n.capitalize()])
        self.comboText(self.unitInput,self.liststore,0)
        self.comboText(self.unitOutput,self.liststore,-1)

#   usada para setar as grandezas da entrada
#      metro: km, cm, μm etc
    def mudouUnitIn(self, box):
        unit = box.get_active_text()
        liststorePow = Gtk.ListStore(str)
        for n in range(len(self.pows.index.values)):
            liststorePow.append([self.pows.values[n][0]+self.units.loc[unit].iat[0]])
        self.comboText(self.powInput,liststorePow,7)
#   usada de maneira similar para a saida
    def mudouUnitOut(self, box):
        unit = box.get_active_text()
        liststorePow = Gtk.ListStore(str)
        for n in range(len(self.pows.index.values)):
            liststorePow.append([self.pows.values[n][0]+self.units.loc[unit].iat[0]])
        self.comboText(self.powOutput,liststorePow,7)
    
    #   funcao para converter os valores
    def converte(self, botao):
        valor = float(self.numInput.get_text())

        #   pega a constante de proporcionalidade de cada constante
        unitconstIn = self.units.loc[self.unitInput.get_active_text()]
        unitconstOut = self.units.loc[self.unitOutput.get_active_text()]

        #   pega a potencia da ordem de grandeza
        expoIn = int(self.pows.values[self.powInput.get_active()][1])
        expoOut = int(self.pows.values[self.powOutput.get_active()][1])

        #   converte a unidade e joga o valor 
        a = Unidade(valor,unitconstIn.iat[0],unitconstIn.iat[1],expoIn)
        valorOut = a.converter(unitconstOut.iat[1], expoOut,unitconstOut.iat[0])

        self.numOutput.set_text(str(valorOut))
        
    #   funcao para trocar as unidades da entrada e saida
    def inverte(self, botao):
        #   salvar os ids ativos nos box de Unidade
        unitIn = self.unitInput.get_active()
        unitOut = self.unitOutput.get_active()

        powIn = self.powInput.get_active()
        powOut = self.powOutput.get_active()

        #   salvar o  valor do input
        valorIn = self.numInput.get_text()
        valorOut = self.numOutput.get_text()

        #   trocar os ids ativos das unidades
        self.unitInput.set_active(unitOut)
        self.unitOutput.set_active(unitIn)

        #   troca os ids ativos nas ordens de grandeza
        self.powInput.set_active(powOut)
        self.powOutput.set_active(powIn)

        #   colocar o valor do input no output
        self.numInput.set_text(valorOut)
        self.numOutput.set_text(valorIn)

#   Coisasa a arrumar se der tempo
#       - trocar a Entry do Output para um Label
#       - adicionar botao de copiar unidade formatada com unidade 
#           '15.8ft' - Copiado!
#       - adicionar uma label que forme uma frase com a conversao
#           '300g equivalem a 0.3kg'
#           essa label pode ser pra colocar a frase de copiar tambem
#       - tirar os Handlers 'aa' e 'aaaaa' da Entry de input