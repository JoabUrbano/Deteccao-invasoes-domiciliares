class BayesNode:
    def __init__(self, name, parents, cpt):
        self.name = name
        self.parents = parents
        self.cpt = cpt

class BayesNet:
    def __init__(self, nodes):
        self.nodes = {name: BayesNode(name, parents, cpt) for name, parents, cpt in nodes}

    def get_node(self, var):
        return self.nodes[var]

    def variable_values(self, var):
        return [True, False]


def enumeration_ask(X, evidence, bn):
    Q = {}
    for xi in [True, False]:
        Q[xi] = enumerate_all(list(bn.nodes), {**evidence, X: xi}, bn)
    # Normalize
    total = sum(Q.values())
    return {k: v / total for k, v in Q.items()}

def enumerate_all(vars, evidence, bn):
    if not vars:
        return 1.0
    Y = vars[0]
    node = bn.get_node(Y)
    if Y in evidence:
        prob = probability(Y, evidence[Y], evidence, bn)
        return prob * enumerate_all(vars[1:], evidence, bn)
    else:
        total = 0
        for y in [True, False]:
            prob = probability(Y, y, evidence, bn)
            total += prob * enumerate_all(vars[1:], {**evidence, Y: y}, bn)
        return total

def probability(var, value, evidence, bn):
    node = bn.get_node(var)
    if not node.parents:
        prob = node.cpt if value else 1 - node.cpt
    else:
        parent_vals = tuple(evidence[parent] for parent in node.parents)
        prob = node.cpt[parent_vals] if value else 1 - node.cpt[parent_vals]
    return prob
