from math import sqrt
from statistics import mode

def euclidean_distance(v1, v2):
    return sqrt(sum((v1[i] - v2[i])**2 for i in range(len(v1))))

def majority_element(labels):
    return mode(labels)

def knn_predict(input, examples, distance, combine, k):
    sorted_examples = sorted(examples, key=lambda x: distance(input, x[0]))
    i = 0
    while i < len(examples) and (i < k or 
                                 distance(input, sorted_examples[i-1][0]) == 
                                 distance(input, sorted_examples[i][0])):
        i += 1
    neighbours = sorted_examples[:i]
    prediction = combine([neighbour[1] for neighbour in neighbours])
    return prediction
        

def main():
    examples = [
        ([2], '-'),
        ([3], '-'),
        ([5], '+'),
        ([8], '+'),
        ([9], '+'),
    ]

    distance = euclidean_distance
    combine = majority_element
    
    for k in range(1, 6, 2):
        print("k =", k)
        print("x", "prediction")
        for x in range(0,10):
            print(x, knn_predict([x], examples, distance, combine, k))
        print()
    
    examples = [
        ([1], 5),
        ([2], -1),
        ([5], 1),
        ([7], 4),
        ([9], 8),
    ]
    
    def average(values):
        return sum(values) / len(values)
    
    distance = euclidean_distance
    combine = average
    
    for k in range(1, 6, 2):
        print("k =", k)
        print("x", "prediction")
        for x in range(0,10):
            print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
        print()
        
    examples = [([-2], '+'), ([-1], '+'), ([0], '-'), ([1], '+'), ([2], '-'), ([3], '-')]
    distance = euclidean_distance
    combine = majority_element
    print("k = 3")
    print("x", "prediction")
    print(1.2, knn_predict([1.2], examples, distance, combine, 3))
    
if __name__ == '__main__':
    main()