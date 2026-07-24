import simpy

class Aeroporto:
    def __init__(self, 
                 env: simpy.Environment, 
                 num_plataformas: int, 
                 num_hangares: int, 
                 num_pistas_peq: int, 
                 num_pistas_gran: int):
        self.env = env
        self.plataformas = simpy.Resource(self.env, num_plataformas)
        self.hangares = simpy.Resource(self.env, num_hangares)
        self.pistas_peq = simpy.Resource(self.env, num_pistas_peq)
        self.pistas_gran = simpy.Resource(self.env, num_pistas_gran)