import pickle

def save_budget_to_file(budget, filename='budget.pickle'):
    with open(filename, 'wb') as file:
        pickle.dump(budget, file)

def load_budget_from_file(filename='budget.pickle'):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}