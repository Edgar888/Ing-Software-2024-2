class MarcadorTenis:
    def __init__(self, jugador1, jugador2, sets_a_jugar):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.sets_a_jugar = sets_a_jugar
        self.puntos = {jugador1: 0, jugador2: 0}
        self.sets = {jugador1: 0, jugador2: 0}
        self.saca = None

    def punto(self, jugador):
        if jugador not in [self.jugador1, self.jugador2]:
            raise ValueError("El nombre del jugador no es válido.")
        if self.puntos[self.jugador1] == 40 and self.puntos[self.jugador2] == 40:  # Deuce
            self.puntos[jugador] = "Adv."
        elif self.puntos[jugador] == "Adv." and self.puntos[self.oponente(jugador)] == 40:  # Ganar desde ventaja
            self.gana_juego(jugador)
        elif self.puntos[jugador] == 40:  # Ganar juego normal
            self.gana_juego(jugador)
        else:
            if self.puntos[jugador] == 30:
                self.puntos[jugador] = 40
            elif self.puntos[jugador] == 15:
                self.puntos[jugador] = 30
            else:
                self.puntos[jugador] = 15

    def gana_juego(self, jugador):
        self.sets[jugador] += 1
        self.puntos = {self.jugador1: 0, self.jugador2: 0}  # Reiniciar puntos para el siguiente juego
        if max(self.sets.values()) >= (self.sets_a_jugar + 1) // 2:
            raise ValueError(f"¡{jugador} gana el partido!")

    def oponente(self, jugador):
        return self.jugador2 if jugador == self.jugador1 else self.jugador1

    def determinar_saque(self):
        if self.ultimo_saque is None:
            self.saca = random.choice([self.jugador1, self.jugador2])
        elif self.ultimo_saque == self.jugador1:
            self.saca = self.jugador2
        else:
            self.saca = self.jugador1
        self.ultimo_saque = self.saca


if __name__ == "__main__":
    jugador1 = input("Nombre del jugador 1: ")
    jugador2 = input("Nombre del jugador 2: ")

    # Verificar que los nombres de los jugadores sean diferentes
    while jugador1 == jugador2:
        print("Los nombres de los jugadores deben ser diferentes.")
        jugador2 = input("Nombre del jugador 2: ")

    # Solicitar el número de sets a jugar hasta que se ingrese un número impar
    sets_a_jugar = None
    while sets_a_jugar is None or sets_a_jugar % 2 == 0:
        sets_a_jugar = int(input("Número de sets a jugar (debe ser impar): "))
        if sets_a_jugar % 2 == 0:
            print("El número de sets debe ser impar.")

    marcador = MarcadorTenis(jugador1, jugador2, sets_a_jugar)
    marcador.saca = jugador1

    try:
        while max(marcador.sets.values()) < (sets_a_jugar + 1) // 2:
            jugador = input(f"Punto para {jugador1} o {jugador2}: ")
            marcador.punto(jugador)
            print(f"Marcador actual: {marcador.puntos[jugador1]}-{marcador.puntos[jugador2]} "
                  f"en el set {marcador.sets[jugador1]}-{marcador.sets[jugador2]}")
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingresa un jugador válido.")
