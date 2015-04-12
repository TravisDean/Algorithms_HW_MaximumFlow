__author__ = 'Travis'

class Node(object):
    def __init__(self, name, demand=0):
        self.name = name
        self.demand = demand
        self.inc = []
        self.out = []

    def __str__(self):
        return str(self.name) + ": " + str(self.demand)


class Edge(object):
    def __init__(self, source, dest, capacity, minflow=0):
        self.source = source
        self.dest = dest
        self.capacity = capacity
        self.flow = 0
        self.minflow = minflow
        self.source.out.append(self)
        self.dest.inc.append(self)

    def resid(self):
        return self.capacity - self.flow

    def bresid(self):
        return -self.flow

    def __str__(self):
        return str(self.source.name) + " -> " + str(self.dest.name) + ":  " \
               + str(self.flow) + "/" + str(self.capacity) + "\t" \
               + str(self.resid()) + " -- " + str(self.bresid())

class Graph(object):
    def __init__(self):
        self.nodes = []
        self.source = None
        self.terminus = None

    def addNode(self, node):
        self.nodes.append(node)

    def connect(self, source, dest, capacity, minflow=0):
        [self.addNode(n) for n in (source, dest) if n not in self.nodes]
        e = Edge(source, dest, capacity, minflow)
        re = Edge(dest, source, 0, 0)
        e.re = re
        re.re = e

    def findPath(self, f, t, path=None):
        if not path: path = []
        if f is t: return path
        for outedge in f.out:
            if outedge not in path and outedge.resid() > 0:
                result = self.findPath(outedge.dest, t, path + [outedge])
                if result is not None:
                    return result

    def maxFlow(self, f, t):
        path = self.findPath(f, t)
        while path is not None:
            flow = min([e.resid() for e in path])
            for e in path:
                e.flow += flow
                e.re.flow -= flow
            path = self.findPath(f, t)
        return sum(e.flow for e in f.out)

    def __str__(self):
        s = ""
        for n in self.nodes:
            s += str(n) + "\n"
            for e in n.out:
                s += "\t" + str(e) + "\n"
        return s



g = Graph()
nodes = [Node(c) for c in "SUVT"]
s, u, v, t = nodes
g.connect(s, u, 20)
g.connect(s, v, 10)
g.connect(u, v, 30)
g.connect(u, t, 10)
g.connect(v, t, 20)
g.source = s
g.terminus = t
print(str(g))

path = g.findPath(s, t)
for p in path:
    print(str(p))
maxflow = g.maxFlow(s, t)
print(str(maxflow))
print (str(g))
# print(str(p))
