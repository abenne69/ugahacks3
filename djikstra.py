import sys
import csv
import collections  

class Graph:
  def __init__(self):
    self.nodes = set() #initialize nodes list (unique only)
    self.edges = collections.defaultdict(list) #initialize dictionary that will create keys on acces (nokeyerror)
    self.distances = {} #distances dictionary

  def add_node(self, value):
    self.nodes.add(value) #add node to list by #

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node) #add edge from src to dst
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance #add weight to current edge src->dst


def dijsktra(graph, initial):
  visited = {initial: 0} #init vistited dict with initial node
  path = {} #dictionary for current path

  nodes = set(graph.nodes) #localize graph nodes list

  while nodes: 
    min_node = None
    for node in nodes: #iterate through all nodes
      if node in visited: #if the node is in visited dictionary - (initial node makes true first)
        if min_node is None: #if min node is not initialized - set min to initial
          min_node = node
        elif visited[node] < visited[min_node]: #else if the current visited node edge weight is less than previous edge weight
          min_node = node #set min_node = to new node

    if min_node is None: #if there is no node found break
      break

    nodes.remove(min_node) #remove the current min_node from nodes (traveled to)
    current_weight = visited[min_node] #set current weight to weight up to current min_node

    for edge in graph.edges[min_node]:  #iterate all possible next nodes in edges dictionary from min_node
      try:
        weight = current_weight + graph.distances[(min_node, edge)] #set weight = current weight + weight of next step
      except:
        continue
      if edge not in visited or weight < visited[edge]: #if next step is not in visited or new weight < current least weight next step
        visited[edge] = weight #store edge as next step key and weight of step as value
        path[edge] = min_node #add the next minimum node as t

  return visited, path

def shortestPath(graph,origin,destination):
  visited, paths = dijsktra(graph, origin)
  path = []
  pathToDestination = paths[destination]

  path.append(destination)
  while pathToDestination != origin:
      path.append(pathToDestination)
      pathToDestination = paths[pathToDestination]

  path.append(origin)
  path = path[::-1]

  return visited[destination], list(path)


"""
def connectNodeGraph(graph,nodesToConnect, reader):
      for x in nodesToConnect:
          for line in reader:
              print("connection acheived")
              if int(line[0]) in nodesToConnect[0]:
                nodesToConnect[x][line[0]].append(line[3])
      for z in nodesToConnect:
          for k in nodesToConnect[z]:
            if(len(nodesToConnect[z][k])>0):
                graph.add_edge(z,k,sum(nodesToConnect[z][k]/len(nodesToConnect[z][k])))

def checkCompleteness(graph):
  needToAdd = {}
  for i in graph.nodes:
      for x in graph.nodes:
        if x != i:
          if x not in graph.edges[i]:
            needToAdd[i] = {x:[]}
  return needToAdd
"""
def isNumber(number):
  try:
    Int(number)
    return True
  except ValueError:
    return False

def main():
    graph = Graph()

    hour = int(sys.argv[1])
    startNode = int(sys.argv[2])
    endNode = int(sys.argv[3])
    print(hour, " - ", startNode, " - ", endNode)
    filepath = "cincinnati-censustracts-2017-3-All-HourlyAggregate.csv"

    reader = csv.reader(open(filepath, "r"))
    counter = 0
    for line in reader:
      try:
        if int(line[2]) == hour:
          counter +=1 
          graph.add_node(int(line[0]))
          graph.add_node(int(line[1]))
          graph.add_edge(int(line[0]),int(line[1]),int(line[3]))
      except:
        continue
    """
    
    nodesToConnect = checkCompleteness(graph)

    print(len(nodesToConnect))
    if(len(nodesToConnect) != 0):
      print(len(nodesToConnect))
      connectNodeGraph(graph,nodesToConnect,reader)
    """

    print (shortestPath(graph, startNode, endNode))


main()