
class Graph:

	def __init__(self, V, grid):
		self.V = V
		self.grid = grid

	def minDist(self, dist, Q):
		mini = float('inf')
		for v in range(self.V):
			if dist[v] < mini and not Q[v]:
				mini = dist[v]
		print(v)
		return Q[v]


	def dijkstra(self, source, target):

		Q = []

		dist = [float('inf')] * self.V
		prev = [None] * self.V

		for row in self.grid:
			for cell in row:
				Q.append(cell)

		dist[source.id] = 0

		u = 0
		while Q:
			u = self.minDist(dist, Q)

			Q.remove(u)

			if u == target: break

			for v in u.neighbors:
				alt = dist[u.id] + 1
				if alt < dist[v.id]:
					dist[v.id] = alt
					prev[v.id] = u

		S = []
		u = target
		while prev[u.id]:
			S.insert(0, u)
			u = prev[u.id]
		S.insert(0,u)

		return S



