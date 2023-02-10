
class Node:
    
    def __init__(self, frekvens):
        self.frekvens = frekvens
        
    def __str__(self): # funksjon som har en spesiel funksjon til python språket
        return "Node, frekvens:" + str(self.frekvens)
        
class Rack:
    
    def __init__(self, maks_noder):
        self.maks_noder = maks_noder
        self.noder = []
        
    def har_mer_plass(self):
        return len(self.noder) < self.maks_noder
        
    def legg_til_node(self, frevens):
        self.noder.append(Node(frevens))
        
    def gjennomsnitt_frekvens(self):
        snitt = 0
        for node in self.noder:
            snitt += node.frekvens
        return snitt / len(self.noder)
    
    def __str__(self):
        s = "== Rack =="
        s += "\nPlasser: " + str(self.maks_noder)
        s += "\nInneholder: " + str(len(self.noder)) + " noder: \n"
        for node in self.noder:
            s += str(node) + "\n"
        return s 
    
class Cluster:
    
    def __init__(self):
        self.rack = []
    
    def legg_til_rack(self, maks_plasser):
        self.rack.append(Rack(maks_plasser))
        
    def legg_til_node(self, frekvens):
        for rack in self.rack:
            if rack.har_mer_plass():
                rack.legg_til_node(frekvens)
                return
        print("det er ikke plass til node i noen flere racks")
    
    def gjennomsnitt_frekvens(self):
        snitt = 0
        for rack in self.rack:
            snitt += rack.gjennomsnitt_frekvens()
        snitt = snitt / len(self.rack)
        print("Snittfrekvens i systemet:", snitt)
        
    def __str__(self):
        s += "==== CLUSTER ====\n"
        for rack in self.rack:
            s += str(rack) + "\n"
        return s


if __name__ == "__main__":
    abel = Cluster()
    abel.legg_til_rack(5)
    abel.legg_til_rack(3)
    
    for i in range(5):
        abel.legg_til_node(3.0)
    abel.legg_til_node(2.5)
    abel.legg_til_node(2)
    
    print(abel)


    