import config
import player
import math
import species
import operator

class Population:
    def __init__(self,size):
        self.players = []
        self.size = size
        self.generation = 1
        self.species = []
        for i in range(0,self.size):
            self.players.append(player.Player())

    def update_live_players(self):

        for p in self.players:
            if p.alive:
                p.look()
                p.think()
                p.draw(config.window)
                p.update(config.ground)
    def natural_selection(self):
        print('Speciate')
        self.speciate()

        print("Fitness Calculation")
        self.calculate_fitness()

        print("Sort By Fitness")
        self.sort_species_by_fitness()

        print("Children for next gen")
        self.next_gen()
    
    def speciate(self):
        for s in self.species:
            s.players = []
        for p in self.players:
            add_to_species = False
            for s in self.species:
                if s.similarity(p.brain):
                    s.add_to_species(p)
                    add_to_species = True
                    break
            if not add_to_species:
                self.species.append(species.Species(p))
    def calculate_fitness(self):
        for p in self.players:
            p.calculate_fitness()
        for s in self.species:
            s.calculate_average_fitness()
    def sort_species_by_fitness(self):
        for s in self.species:
            s.sort_players_by_fitness()
        
        self.species.sort(key=operator.attrgetter('benchmark_fitness'),reverse=True)
    
    def next_gen(self):
        children = []

        for s in self.species:
            children.append(s.champion.clone())
        
        children_per_species = math.floor((self.size - len(self.species)) / len(self.species))
        for s in self.species:
            for i in range(0,children_per_species):
                children.append(s.offspring())
        while len(children) < self.size:
            children.append(self.species[0].offspring())
        self.players= []
        for child in children:
            self.players.append(child)
        self.generation += 1
    # return true if all players are dead
    def extinct(self):
        extinct = True
        for p in self.players:
            if p.alive: 
                extinct = False
        return extinct
