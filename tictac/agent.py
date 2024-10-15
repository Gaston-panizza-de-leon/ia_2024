"""

ClauPercepcio:
    POSICIO = 0
    OLOR = 1
    PARETS = 2
"""

from base import entorn
from tictac import joc


class Agent(joc.Agent):
    def __init__(self, nom):
        super(Agent, self).__init__(nom)

    def pinta(self, display):
        pass

    def actua(
        self, percepcio: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        return joc.Accio.ESPERAR

    """def minimax(estat, torn_de_max):
        if evaluar(estat, torn_de_max) != None:
            return estat, score

        puntuació_fills = [minimax(estat_fill, !torn_de_max) for estat_fill in estat.genera_fills()]
        if torn_de_max:
            return max(puntuació_fills)
        else:
            return min(puntuació_fills)

    def evaluar(estat, jugador):
        if estat.meta():
            return puntuacio(jugador)"""