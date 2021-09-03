#!/usr/bin/env python3

# test_exemple.py

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('exemple') == 'Exemple'