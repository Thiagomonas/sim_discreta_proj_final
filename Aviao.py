import simpy

class Aviao:
    def __init__(self, env: simpy.Environment, tipo: str, modelo: str):
        self.env = env
        self.tipo = tipo
        self.modelo = modelo
        self.ev_percurso = self.env.event()
        if self.tipo == "P":
            self.tempo_decolagem = 40
            self.tempo_desembarque = 20
            self.tempo_hangar = 35
            self.tempo_embarque = 30
        else:
            self.tempo_decolagem = 60 
            self.tempo_desembarque = 40
            self.tempo_hangar = 70
            self.tempo_embarque = 60