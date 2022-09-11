import pickle
import numpy as np
import re
import argparse
import os
import glob

def train(input_dir, model='model.pickle'):
    data = {}
    for filename in glob.glob(os.path.join(input_dir, '*.txt')):
        with open(os.path.join(os.getcwd(), filename), 'r', encoding='utf-8') as file:
            text = file.read().lower()
            text = re.sub('[!\?]', '.', text)
            sentences = text.split('. ')
            words = []
            for i in range(len(sentences)):
                words.append(re.sub('[\'\"\.:;,\(\)-\[\]\{\}]', '', sentences[i]).split())
        for sentence in words:
            for i in range(len(sentence) - 2):
                data[(sentence[i], sentence[i + 1])] = data.get(sentence[i], []) + [sentence[i + 2]]
    with open(model, 'wb') as file:
        pickle.dump(data, file)
#my_parser = argparse.ArgumentParser(description='Обучение модели')
#my_parser.add_argument('directory', metavar='directory', type=str, help='directory with files')
#my_parser.add_argument('model', type=str, help='file with model')
#args = my_parser.parse_args()
# train(args.directory='data', args.model='model.pickle')
train('data', 'model.pickle')
print('Обучение завершено')