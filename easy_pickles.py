import pickle


def create_pickle(varible, filename):
    if len(filename) > 7:
        if filename[-7:] == '.pickle':
            with open(filename, 'wb') as f:
                pickle.dump(varible, f)
        else:
            with open(filename + '.pickle', 'wb') as f:
                pickle.dump(varible, f)
    else:
        with open(filename + '.pickle', 'wb') as f:
            pickle.dump(varible, f)


def read_pickle(filename):
    if len(filename) > 7:
        if filename[-7:] == '.pickle':
            with open(filename, 'rb') as f:
                pickle.load(f)
        else:
            with open(filename + '.pickle', 'rb') as f:
                pickle.load(f)
    else:
        with open(filename + '.pickle', 'rb') as f:
            pickle.load(f)
