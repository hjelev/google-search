
import pickle
import random
from googlesearch import search
import os, sys


def get_position(counter_file, step):
    with open(counter_file, 'rb') as f:
        counter = pickle.load(f)

    start = counter * step - step

    return(start,  counter)


def search_keyword(keyword, step, start, domain):
    results = []
    print(f"Keyword: {keyword.strip()}")
    pause = random.randint(2,5)
    print(start,step)
    for j in search(keyword.strip(), tld="com", start=start, stop=step, pause=pause):
        print(j)
        results.append(j)

    return(results)

def save_results(data, results_folder, domain):
    results_folder = os.path.join(sys.path[0] + '/' + results_folder , domain + '.txt')
    print(data)
    with open(results_folder, 'w') as f:
        for line in data:
            print(line)
            f.write(line + '\n')

def main():
    counter_file = "data/counter.dat"
    results_folder = "results"
    counter_file = os.path.join(sys.path[0], counter_file)
    step = 10
    keywords = {
        "com":"Customs"
    }

    start, counter = get_position(counter_file, step)
    
    for lang in keywords:
        print(f"Language: {lang}")
        for keyword in keywords[lang].split(','):
            data = search_keyword(keyword, step, start, lang)
            print(data)
            save_results(data, results_folder, lang)
 
    counter += 1

    with open( counter_file, "wb") as f:
        pickle.dump(counter, f)


if __name__ == '__main__':
    main()