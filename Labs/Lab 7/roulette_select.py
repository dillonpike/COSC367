def roulette_wheel_select(population, fitness, r):
    running_totals = [fitness(population[0])]
    for i in range(1, len(population)):
        running_totals.append(fitness(population[i]) + running_totals[i-1])
    r *= running_totals[-1]
    for i in range(len(running_totals)):
        if running_totals[i] > r:
            return population[i]
    
def main():
    population = ['a', 'b']

    def fitness(x):
        return 1 # everyone has the same fitness
    
    for r in [0, 0.33, 0.49999, 0.5, 0.75, 0.99999]:
        print(roulette_wheel_select(population, fitness, r))
        
    population = [0, 1, 2]
    
    def fitness(x):
        return x
    
    for r in [0, 0.33, 0.34, 0.5, 0.75, 0.99]:
        print(roulette_wheel_select(population, fitness, r))    

if __name__ == '__main__':
    main()