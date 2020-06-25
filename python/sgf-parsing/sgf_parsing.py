class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string: str) -> SgfTree:
    """
    Examples:
    (;FF[4]C[root]SZ[19];B[aa];W[ab])
    ['(', 'FF[4]C[root]SZ[19]', 'B[aa]', 'W[ab])']
    node 3 props FF[4] c[root] SZ[19]
      - child node 1 prop B[aa]
        - child node 1 prop W[ab]

    (;FF[4](;B[aa];W[ab])(;B[dd];W[ee]))
    ['(', 'FF[4](', 'B[aa]', 'W[ab])(', 'B[dd]', 'W[ee]))']

    (;FF[4];AB[aa][ab][ba])
    ['(', 'FF[4]', 'AB[aa][ab][ba])']
    """
    nodes = input_string[1:-1].split(';')
    last_node = None
    while len(nodes) > 0:
        node_str = nodes.pop()
        if not node_str:
            continue
        new_node = SgfTree()
        if last_node:
            new_node.children.append(last_node)
        prop_strs = node_str.split('[')
        new_node.properties[prop_strs[0]] = []
        for prop in prop_strs[1:]:
            new_node.properties[prop_strs[0]].append(prop[:-1])
        last_node = new_node
    return last_node
