import csv

def posterior(prior, likelihood, observation):
    true = prior
    false = 1 - prior
    for i in range(len(likelihood)):
        if observation[i]:
            true *= likelihood[i][True]
            false *= likelihood[i][False]
        else:
            true *= 1 - likelihood[i][True]
            false *= 1 - likelihood[i][False]            
        
    return true / (true+false)
    
def learn_prior(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    return ([row[-1] for row in training_examples].count('1') + pseudo_count) \
           / (len(training_examples) - 1 + 2 * pseudo_count)

def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
        
    num_spam = [row[-1] for row in training_examples].count('1')
    num_not_spam = len(training_examples) - num_spam - 1
    likelihood = []
    for i in range(len(training_examples[0])-1):
        true_count = [(row[i], row[-1]) for row in training_examples].count(('1', '1'))
        false_count = [(row[i], row[-1]) for row in training_examples].count(('1', '0'))
        prob_when_spam = (true_count+pseudo_count) / (num_spam+2*pseudo_count)
        prob_when_not_spam = (false_count+pseudo_count) / (num_not_spam+2*pseudo_count)
        likelihood.append((prob_when_not_spam, prob_when_spam))
    return likelihood

def nb_classify(prior, likelihood, input_vector):
    prob = posterior(prior, likelihood, input_vector)
    if prob > 0.5:
        return ("Spam", prob)
    else:
        return ("Not Spam", 1-prob)
    
def main():
    prior = learn_prior("spam-labelled.csv")
    likelihood = learn_likelihood("spam-labelled.csv")
    
    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]
    
    predictions = [nb_classify(prior, likelihood, vector) 
                   for vector in input_vectors]
    
    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))
        
    prior = learn_prior("spam-labelled.csv", pseudo_count=1)
    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)
    
    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]
    
    predictions = [nb_classify(prior, likelihood, vector) 
                   for vector in input_vectors]
    
    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))    

if __name__ == '__main__':
    main()