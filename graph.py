# implement dijkstra using undirected graph
# vertices stored using adjacency matrix

class Graph:

	def __init__(self, verticeCount, grid):
		self.V = verticeCount 
		self.graph = [[0 for col in range(verticeCount)]
					  for row in range(verticeCount)]



	def printSolution(self, dist):
		print("Vertex tDistance from Source")
		for node in range(self.V):
		    print(node,"t",dist[node])

	# helper function to find vertex with 
	# min distance in set of vectors not 
	# in shortest path tree 
	def __minDistance(self, dist, spTree):

		minDist = float("inf")
		minIndex = 0
		for v in range(self.V):
			if dist[v] < minDist and not spTree[v]:
				minDist = dist[v]
				minIndex = v

		return minIndex

	# Single source shortest path
	# - graph represented using adjacency matrix
	def dijkstra(self, src):

		# set all distances to infinity
		dist = [float("inf")] * self.V 
		dist[src] = 0
		spTree = [False] * self.V

		for c in range(self.V):

			# choose min distance vertex from from set of unprocessed vertices
			u = self.__minDistance(dist, spTree)

			# put the min distance vertex in the spTree
			spTree[u] = True

			# update dist value of the adj. vertices of the chosen vertex only
			# if the current distance > new distance and the vertex is not 
			# in the spTree
			for v in range(self.V):
				if self.graph[u][v] > 0 and spTree[v] == False and dist[v] > dist[u] + self.graph[u][v]:
					dist[v] = dist[u] + self.graph[u][v]

		self.printSolution(dist)


if __name__ == '__main__':
	g = Graph(10)
	g.dijkstra(0)

