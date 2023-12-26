# Day twenty five of the advent of code 2023
#
#
import networkx as nx

def main() -> None:
    print('Christmas Day!')

    g = nx.Graph()

    for line in open('data/wired.txt'):
        left, right = line.split(':')
        for node in right.strip().split():
            g.add_edge(left, node)
            g.add_edge(node, left)    

    g.remove_edges_from(nx.minimum_edge_cut(g))
    a, b = nx.connected_components(g)

    print(len(a) * len(b))

    return 

if __name__ == '__main__':
    main()