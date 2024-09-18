from aspirador.entorn import Localitzacio, EstatHabitacio, Sensor, AccionsAspirador
from base import agent, entorn, joc

class AspiradorNoG(joc.JocNoGrafic):

    def __init__(self, agents: list[agent.Agent] | None = None):
        if agents is None:
            agents = []
        super(AspiradorNoG, self).__init__(agents=agents)
        # TODO
        self.posicio = Localitzacio.aleatori()
        self.entorn = {Localitzacio.HABITACIO_ESQ: EstatHabitacio.aleatori(),
                       Localitzacio.HABITACIO_DRET: EstatHabitacio.aleatori()}


    def _draw(self):
        # TODO
        st_hab_esq = "net" if self.entorn[Localitzacio.HABITACIO_ESQ] == EstatHabitacio.NET else "brut"
        st_hab_dre = "net" if self.entorn[Localitzacio.HABITACIO_DRET] == EstatHabitacio.NET else "brut"

        pos_aspirador = "Esquerra" if self.posicio == Localitzacio.HABITACIO_ESQ else "Dreta"

        print(f"Posició Aspirador: {pos_aspirador}")
        print(f"Habitació Esquerra: {st_hab_esq}, Habitació Dreta: {st_hab_dre}")

        pass


    def percepcio(self) -> entorn.Percepcio | dict:
        return {
            Sensor.LLOC: self.posicio,
            Sensor.ESTAT: self.entorn[self.posicio]
        }
        # TODO
        pass


    def _aplica(self, accio: entorn.Accio, params=None, agent_actual=None):

        if accio == AccionsAspirador.ASPIRA:
            self.entorn[self.posicio] = EstatHabitacio.NET
        elif accio == AccionsAspirador.DRETA:
            self.posicio = Localitzacio.HABITACIO_DRET
        elif accio == AccionsAspirador.ESQUERRA:
            self.posicio = Localitzacio.HABITACIO_ESQ
        elif accio == AccionsAspirador.ATURA:
            pass
        pass
        # TODO


