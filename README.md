# Conversor de Unidades
Trabalho final da disciplina SEL0456.
O objetivo do projeto é desenvolver um conversor de unidades de medida que suporte ao menos 2 conversões entre tipos de unidade distintos.

## Dependências
São necessários para que o código funcione em sua máquina:
- Python 3
- Python GTK+ 3
- Glade XML
- Pandas

## Funcionalidades
1. [Converter](#converter)
2. [Inverter](#inverter)
2. [Copiar](#copiar)
3. [Arquivo de texto](#texto)

### <a id = "converter"></a>Converter
Ao dar início pelo `main.py` a interface abre na forma de uma janela onde é necessário primeiro escolher o tipo de unidade (Volume, Comprimento ou Massa, inicialmente) e, logo depois, selecionar pelo menos a unidade para qual o valor será convertido. Uma vez selecionadas, basta clicar no botão 'Converter' que o resultado sairá na caixa de texto inferior. 

### <a id = "inverter"></a>Inverter
Algumas vezes precisamos converter unidades em ambas as 'direções', precisando, numa mesma consulta converter, por exemplo, de milhas para metros, fazer as contas necessárias no SI e depois retornar o valor para milhas.
O botão 'Inverter', como o prório nome sugere, inverte as unidades que estão sendo convertidas: coloca a unidade e potência do input no output e vice versa sem alterar a medida convertida, trocando também as suas posições (10 metros não são 10 milhas).

### <a id = "copiar"></a>Copiar
Ainda não há nada para ver aqui

## <a id = "texto"></a>Arquivo de texto
Ainda não há nada para ver aqui