import simpy
from Aviao import Aviao
from Aeroporto import Aeroporto

NUM_PLATAFORMAS = 5
NUM_HANGARES = 3
NUM_PISTAS_P = 2
NUM_PISTAS_G = 1

class Simulacao:
    def __init__(self, env: simpy.Environment):
        self.env = env
        self.recursos = Aeroporto(self.env, NUM_PLATAFORMAS, NUM_HANGARES, NUM_PISTAS_P, NUM_PISTAS_G)
        self.env.process(self.chegadas())

    def chegadas(self):
        with open("./chegadas.csv") as arq:
            arq.readline()
            linha = arq.readline()
            while linha != '':
                nome, tipo, hor = linha.split(",")
                hor = int(hor)
                yield self.env.timeout(hor - self.env.now)
                self.env.process(self.percurso_completo(Aviao(self.env, tipo, nome)))
                linha = arq.readline()

    def percurso_completo(self, aviao: Aviao):
        print(f'{self.env.now}  |  Avião {aviao.modelo} Requer o pouso')
        yield from self.pouso_decolagem(aviao)
        print(f'{self.env.now}  |  Avião {aviao.modelo} Finalizou o pouso')

        print(f'{self.env.now}  |  Avião {aviao.modelo} Requer o desembarque')
        yield from self.desembarque(aviao)
        print(f'{self.env.now}  |  Avião {aviao.modelo} Finalizou o desembarque')

        print(f'{self.env.now}  |  Avião {aviao.modelo} Requer hangar')
        yield from self.estacionar(aviao)
        print(f'{self.env.now}  |  Avião {aviao.modelo} Finalizou o hangar')

        print(f'{self.env.now}  |  Avião {aviao.modelo} Requer embarque')
        yield from self.embarque(aviao)
        print(f'{self.env.now}  |  Avião {aviao.modelo} Finalizou o embarque')

        print(f'{self.env.now}  |  Avião {aviao.modelo} Requer decolagem')
        yield from self.pouso_decolagem(aviao)
        print(f'{self.env.now}  |  Avião {aviao.modelo} Finalizou a decolagem')
        aviao.ev_percurso.succeed()
    
    def pouso_decolagem(self, aviao: Aviao):
        if aviao.tipo == "P":
            req = self.recursos.pistas_peq.request()
        else:
            req = self.recursos.pistas_gran.request()
        yield req
        yield self.env.timeout(aviao.tempo_decolagem)

        if aviao.tipo == "P":
            self.recursos.pistas_peq.release(req)
        else:
            self.recursos.pistas_gran.release(req)

    def desembarque(self, aviao: Aviao):
        with self.recursos.plataformas.request() as req:
            yield req
            yield self.env.timeout(aviao.tempo_desembarque)


    def embarque(self, aviao: Aviao):
        with self.recursos.plataformas.request() as req:
            yield req
            yield self.env.timeout(aviao.tempo_embarque)

    def estacionar(self, aviao: Aviao):
        with self.recursos.hangares.request() as req:
            yield req
            yield self.env.timeout(aviao.tempo_hangar)


if __name__ == "__main__":
    env = simpy.Environment()
    sim = Simulacao(env)
    env.run()