adjacencyList = [
    {"id": 1, "parentId": None},
    {"id": 2, "parentId": 1},
    {"id": 3, "parentId": 1},
    {"id": 4, "parentId": 1},
    {"id": 5, "parentId": 2},
    {"id": 6, "parentId": 2},
    {"id": 7, "parentId": 3},
    {"id": 8, "parentId": 3},
    {"id": 9, "parentId": 3},
    {"id": 10, "parentId": 4},
    {"id": 11, "parentId": 5},
    {"id": 12, "parentId": 5},
    {"id": 13, "parentId": 7},
    {"id": 14, "parentId": 7},
    {"id": 15, "parentId": 8},
    {"id": 16, "parentId": 11},
    {"id": 17, "parentId": 11},
    {"id": 18, "parentId": 13},
    {"id": 19, "parentId": 16},
    {"id": 20, "parentId": 16}
]


def convertingAdjacencyListToMaterializedPath(adjList):
    nodes = {i["id"]: i for i in adjList}
    def foundPath(node):
        fullPath = []
        id = node
        while id != None:
            fullPath += [str(id)]
            id = nodes[id]["parentId"]
        fullPath = fullPath[::-1]
        return ','.join(fullPath)

    materializedPath = [] 
    for i in nodes:
        path = foundPath(i)
        materializedPath.append({"id": i, "path": path})
    return materializedPath


materialPath = convertingAdjacencyListToMaterializedPath(adjacencyList)
print("material path:",materialPath)
def convertingMaterializedPathToAdjacencyList(matPath):
    adjList = []
    for i in matPath:
        if len(i["path"]) == 1:
            adjList.append({"id": i["id"], "parent": None})
        else:
            adjList.append({"id": i["id"], "parent": int(i["path"].split(',')[-2])})
    return adjList

adjList = convertingMaterializedPathToAdjacencyList(materialPath)
print("adjacency list:", adjList)