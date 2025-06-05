from itertools import product

statement = "(p or q) and (not p or q)"
results = []

def create_table():
    print("p\tq\tResult")
    print("-" * 25)
    
    for combination in product([True, False], repeat=2):
        p, q = combination
        res = eval(statement, {}, {'p': p, 'q': q})
        print(f"{p}\t{q}\t{res}")
        results.append(res)
    print("-" * 25)

create_table()


if all(results):
    print("Statement is a tautology")
elif not any(results):
    print("Statement is a contradiction")
else:
    print("Statement is satisfiable")