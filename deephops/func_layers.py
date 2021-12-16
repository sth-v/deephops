
import func_content as fc

"""func_layers -
"""


class Func:
    def __init__(self, definition):
        self.f = definition


class FuncLayer(Func):
    def __init__(self, definition, name: str) -> None:
        super().__init__(definition)
        self.name = name

    def __f__(self, data, p):
        return self.f(data, p)


def f_polygon_read(data, p):
    fa = fc.p_kmeans(data, p)
    labels = fa.labels_
    fb = fc.get_clusters(data, labels)
    min_bound_rec_results = []
    for i in fb:
        min_bound_rec_results.append(fc.minimum_bounding_rectangle(i))
    return min_bound_rec_results, fb


FL_PolygonRead = FuncLayer(f_polygon_read, 'polygon_read')
