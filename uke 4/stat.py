#4.8
import numpy as np

def mean(x_list):
    """
    setter opp summen fra oppgave a som en funksjon, der N er lengden av summen,
    og x_list er mengden
    """
    a = 1/len(x_list)*sum(x_list)
    return a

def test_mean():
    """
    Lager en testfunkjson for likningen i a
    """
    test_x_values = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.mean(test_x_values)
    computed = mean(test_x_values)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f'computed area={computed} != {expected}(expected)'
    assert success, msg
test_mean()

def standard_deviation(x_list):
    """
    Lager en funksjon for den nye likningen i oppgave c) ved å kalle på likningen i
    oppgave a), og definerer hvilke x verdier vi bruker her.
    """
    c = [np.sqrt(1/len(x_list)*sum((x - np.mean(x_list))**2 for x in x_list))]
    return c

def test_standard_deviation():
    test_x_values = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.std(test_x_values)
    computed = standard_deviation(test_x_values)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f'computed area={computed} != {expected}(expected)'
    assert success, msg
test_standard_deviation()
