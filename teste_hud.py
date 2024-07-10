from rich.console import Console 
from rich.panel import Panel
from rich.text import Text
from rich.box import *
from Inimigo import *
from rich.box import ROUNDED
from rich.table import Table
from rich.emoji import Emoji
from rich.align import Align
from Textos import *
from classes import * 
from Raridadesf import *
from Acoes import *
from six import *

#from Acoes import combate_MagoObscuro

equip_adaga_i()
gerar_raridades_itens(equipamentos, armas)
equip_bot()
equip_cap()
equip_pet()
equip_cal()


"""Hud_player()
tamanho = 0
for c in player['armaduras_equipadas']:
    for letra in c:
        tamanho += len(letra)
print(tamanho)"""


c = Console()

text = Text()

text.append(f"{player['golpes'][0]}  : DANO : {player['dano'][0]}   | {player['golpes'][1]}  : DANO : {player['dano'][1]}   | {player['golpes'][2]}  : CURA: {player['cura']}   | {player['golpes'][3]} : ABRIR INVENTÁRIO ")

p = Panel(
    text,
    title='Menu de ações',
    title_align='center',
    subtitle='Escolha o que deseja fazer',
    subtitle_align='center'
)

c.print(p)

#combate_MagoObscuro()




