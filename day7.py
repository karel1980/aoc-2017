import re

LINE_PATTERN = re.compile("(.*) \((.*)\)( -> (.*))?")

def read_input():
    lines = [ l.strip() for l in open('day7.input').readlines() ]

    return [ parse_line(l) for l in lines ]

def build_tree(nodes):
    return dict([(node[0],node) for node in nodes])

def parse_line(line):
    match = LINE_PATTERN.match(line)
    parts = match.groups()
    id = parts[0]
    weight = int(parts[1])
    children = [] if parts[3]==None else [ c.strip() for c in parts[3].split(',') ]

    return [id, weight, children]

def find_root(nodes):
    nodes = build_tree(nodes)
    all_ids = set([n[0] for n in nodes.values()])
    nodes_with_parents = set()

    for k,v in nodes.iteritems():
        nodes_with_parents = nodes_with_parents.union(set(v[2]))

    return list(all_ids.difference(nodes_with_parents))[0]

def solve_part1(nodes):
    return find_root(nodes)

def solve_part2(nodes):
    root_id  = find_root(nodes)
    print root_id
    nodes = build_tree(nodes)
    calculate_weights_recursively(nodes, root_id)

    find_unbalanced_node(nodes, root_id)

def calculate_weights_recursively(nodes, node_id):
    node = nodes[node_id]
    child_ids = node[2]

    for child_id in child_ids:
        calculate_weights_recursively(nodes, child_id)

    node.append(node[1] + sum([ nodes[child_id][3] for child_id in child_ids ]))

def find_unbalanced_node(nodes, node_id):
    node = nodes[node_id]
    child_ids = node[2]
    child_weights = [ nodes[child_id][3] for child_id in child_ids ]

    if len(child_weights) > 0 and not all_equal(child_weights):
        print node_id, child_weights
        print "TTT", [ nodes[child_id][1] for child_id in node[2] ]

    for child_id in child_ids:
        find_unbalanced_node(nodes, child_id)

def all_equal(weights):
    return all(w == weights[0] for w in weights)

#print solve_part1(read_input())
print solve_part2(read_input())
