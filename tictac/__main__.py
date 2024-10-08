from tictac import agent, joc


def main():
    quatre = joc.Taulell([agent.Agent("Jugador 1"), agent.Agent("Jugador 2")], mida_taulell=(3, 3), dificultat=3)
    quatre.comencar()


if __name__ == "__main__":
    main()
