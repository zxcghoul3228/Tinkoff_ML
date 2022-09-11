import pickle
import argparse
import numpy as np
def generate(prefix, length, model='model.pickle'):
    with open(model, 'rb') as file:
        data = pickle.load(file)
    words = prefix.split()
    for _ in range(length):
        if len(words) > 1 and (words[-2], words[-1]) in data:
            words.append(np.random.choice(data[(words[-2], words[-1])]))
        else:
            words.extend(list(data.keys())[np.random.randint(0, len(data))])
    result = ' '.join(words)
    return result
my_parser = argparse.ArgumentParser(description='Генерация текста')
my_parser.add_argument('Prefix', metavar='prefix', type=str, help='start of generation')
my_parser.add_argument('Length', metavar='lenth', type=int, help='length of sentence')
my_parser.add_argument('Name', type=str, default='model.pickle', help='name of file with model')
args = my_parser.parse_args()
print(generate(args.Prefix, args.Length, args.Name))