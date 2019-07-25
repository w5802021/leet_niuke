
def Kruskal(graph):
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]
    mst,edges = [],[]
    for vi in range(vnum):
        for v,w in graph.out_edges(vi):
            edges.append((w,vi,v))

    edges.sort()
    for w,vi,vj in edges:
        if reps[vi] != reps[vj]:
            mst.append((vi,vj),w)
            if len(mst) == vnum-1:
                break
            rep,orep = reps[vi], reps[vj]
            for i in range(vnum):
                if reps[i] == orep:
                    reps[i] = rep
    return mst

if __name__ == '__main__':
    graph_w = {'A': {'B': 5, 'C': 1}, 'B': {'A': 5, 'C': 2, 'D': 1}, 'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
               'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
               'E': {'C': 8, 'D': 3}, 'F': {'D': 6}}

    res = Kruskal(graph_w)
    print(res)