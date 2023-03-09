import math
# class Vertex:
#     def __init__(self, name):
#         self._links = []
#         self.name = name
#
#     @property
#     def links(self):
#         return self._links
#
#     def __repr__(self):
#         return f'{self.name}'

class Vertex:
    def __init__(self, ):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, val):
        self._dist = val

    def __eq__(self, other):
        return self.v1 in (other.v1, other.v2) and self.v2 in (other.v1, other.v2)

    def __repr__(self):
        return f'{self.v1} to {self.v2}'


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if link not in self._links:
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)
            self._links.append(link)

    def find_path(self, start_v, stop_v):
        visited = [start_v]
        vertices = {start_v: {'weight': 0, 'links': [], 'vertices': [start_v]}}
        queue = [start_v]
        while queue:
            temp_dict = {k: v for k,v in vertices.items() if k in queue}
            current_node = min(temp_dict, key=lambda k: temp_dict[k]['weight'])
            queue.remove(current_node)
            for link in current_node.links:
                if current_node == link.v1:
                    new_node = link.v2
                else:
                    new_node = link.v1

                if new_node not in visited:
                    if new_node not in vertices:
                        # создание новой вершины
                        vertices[new_node] = {'weight': math.inf, 'links': [], 'vertices': []}
                        vertices[new_node]['links'] = vertices[current_node]['links'] + [link]
                        vertices[new_node]['vertices'] = vertices[current_node]['vertices'] + [new_node]
                    weight = vertices[current_node]['weight'] + link.dist
                    if vertices[new_node]['weight'] > weight:
                        vertices[new_node]['weight'] = weight
                        vertices[new_node]['links'] = vertices[current_node]['links'] + [link]
                        vertices[new_node]['vertices'] = vertices[current_node]['vertices'] + [new_node]
                    queue.append(new_node)
            visited.append(current_node)

        return vertices[stop_v]['vertices'], vertices[stop_v]['links']

    @staticmethod
    def get_min(d):
        lst = []
        for k, v in d.items():
            lst.append(v['weight'])


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self.dist = dist
