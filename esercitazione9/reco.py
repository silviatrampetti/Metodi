class Hit:
    
    def __init__(self, m, s, t):
        self.id_modulo = m
        self.id_sensore = s
        self.time = t

    def __lt__(self, other):
        return (self.time < other.time)

    def __gt__(self,other):
        return (self.time>other.time)

class Event:

    def __init__(self, h):
        self.array_hit = h
        self.num = len(array_hit)
        self.time_f = array_hit[0].time
        self.time_l = array_hit[len(array.hit)].time
        
    def info(self):
        print("numero di hit: ", self.num)
        durata = self.time_l - self.time_f
        print("durata temporale: ", durata)
        print("hit:", array_hit)

    

