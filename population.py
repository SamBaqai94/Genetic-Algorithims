#!/usr/bin/python2
from __future__ import division
from indivisual_dna import Indivisual_DNA
import random

class Population:

    def __init__(self,target,mut_rate,num):
        self.population=None
        self.mating_pool=None
        self.generations=0
        self.finished=False
        self.target=target
        self.mut_rate=mut_rate
        self.perfect_score=1

        self.best=""

        self.population=[]
        for i in range(num):
            self.population.insert(i,Indivisual_DNA(len(self.target)))
        self.mating_pool=[]
        self.calc_fitness

    def calc_fitness(self):
        for i in range(len(self.population)):
            self.population[i].calc_fitness(self.target)
    
    def maps(self,n,start1,stop1,start2,stop2):
        new_value=((n-start1)/(stop1-start1))*(stop2-start2)+start2
        return new_value

    def natural_selection(self):
        self.mating_pool=[]

        max_fitness=0

        for i in range(len(self.population)):
            if self.population[i].fitness > max_fitness:
                max_fitness=self.population[i].fitness

        for j in range(len(self.population)):
            fitness=self.maps(self.population[j].fitness,0,max_fitness,0,1)
            n=float(fitness*100)  
            for h in range(int(n)):
                self.mating_pool.append(self.population[j])

    def generate(self):
        for i in range(len(self.population)):
            a=random.randrange(len(self.mating_pool))
            b=random.randrange(len(self.mating_pool))
            partner_a=self.mating_pool[a]
            partner_b=self.mating_pool[b]
            child=partner_a.crossover(partner_b)
            child.mutate(self.mut_rate)
            self.population[i]=child

        self.generations=self.generations+1

    def get_best(self):
        return self.best
    
    def evaluate(self):
        record=0.0
        index=0
        for i in range(len(self.population)):
            if self.population[i].fitness > record:
                index=i
                record=self.population[i].fitness
        
        self.best=self.population[index].get_pharse()
        if record==self.perfect_score:
            self.finished=True

    def is_finished(self):
        return self.finished
    
    def get_generations(self):
        return self.generations

    def get_average_fitness(self):
        total=0
        for i in range(len(self.population)):
            total=total+self.population[i].fitness
        return total/len(self.population)
    
    def all_phrases(self):
        everything=""
        
        display_limit=min(len(self.population),50)
        for i in range(display_limit):
            everything +=self.population[i].get_pharse()

        return everything