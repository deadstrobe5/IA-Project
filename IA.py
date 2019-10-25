# 89452 89400
import math
import pickle
import time
import bisect

class SearchProblem:

    heuristicas = []
    fathers = []

    def __init__(self,goal,model,auxheur = []):
        self.goal=goal
        self.model=model
        self.auxheur=auxheur
        pass
    def search(self, init, limitexp=2000, limitdepth = 20,tickets = [math.inf,math.inf,math.inf]):

        # EXERCICIO 1
        if (tickets == [math.inf,math.inf,math.inf] and len(init) == 1): 

            self.BFS_1(init[0])

            output1 = []
            node = [[],[init[0]]]
            index = init[0]
            while (index != self.goal[0]):
                index = node[1][0]
                output1.append([node[0],node[1]])
                node = [[self.fathers[index][0]],[self.fathers[index][1]]]

            return output1



        # EXERCICIO 2
        
        elif (len(init) == 1): 
            print(self.model[55])
            self.BFS_2(init[0])
            self.fathers.clear()
            self.Aast_2(init[0], tickets)

            goal = self.goal[0]
            first = init[0]
            fathers = self.fathers

            output1 = []
            node = [[], [goal]]
            index = goal

            while (index != first):
                print(index)
                index = node[1][0]
                node[0] = [fathers[index][0]]
                output1.insert(0, node)
                node = [[],[fathers[index][1]]]
                
            output1[0][0] = []

            return output1
        
        else:
            return []

        # EXERCICIO 3
    '''
        elif(len(init) == 3 and tickets == [math.inf,math.inf,math.inf]):

            self.heuristicas = [[0]*3 for _ in range(len(self.model))]
            self.fathers = [[[None]*2]*3 for _ in range(len(self.model))]

            self.BFS_3(init[0], 0)
            self.BFS_3(init[1], 1)
            self.BFS_3(init[2], 2)

            output1 = []

            node = [[],[init[0], init[1], init[2]]
            index0 = init[0]
            index1 = init[1]
            index2 = init[2]
            while (index0 != self.goal[0]):
                index = node[1][0]
                output1.append([node[0],node[1]])
                node = [[self.fathers[index][0]],[self.fathers[index][1]]]

            return output1

    '''
    

#################################################

    def BFS_1(self, init):
        ### BFS for the 1st Exercise

        atual = self.goal[0]
        U = self.model
        qq = []
        #altitude = [0 for _ in range(len(U))]
        visited = [False for _ in range(len(U))]
        fathers = [[None]*2 for _ in range(len(U))]

        qq.append(atual)
        visited[atual] = True
        #altitude[atual] = 0

        while (len(qq)!=0):
            atual = qq.pop(0)
            if (atual == init):
                break
            for destino in U[atual]:
                filho = destino[1]
                transporte = destino[0]
                if (not visited[filho]):
                    qq.append(filho)
                    visited[filho] = True
                    #altitude[filho] = altitude[atual]+1
                    fathers[filho][1] = atual
                    fathers[filho][0] = transporte

        self.fathers = fathers.copy()
        #self.heuristicas = altitude.copy()


#######################################################

    def BFS_3(self, init, n):
        ### BFS for the 3rd Exercise

        atual = self.goal[0]
        U = self.model
        qq = []
        
        altitude = self.heuristicas.copy()
        fathers = self.fathers.copy()
        visited = [False for _ in range(len(U))]

        qq.append(atual)
        visited[atual] = True
        altitude[atual][n] = 0

        while (len(qq)!=0):
            atual = qq.pop(0)
            if (atual == init):
                break
            for destino in U[atual]:
                filho = destino[1]
                transporte = destino[0]
                if (not visited[filho]):
                    qq.append(filho)
                    visited[filho] = True
                    altitude[filho][n] = altitude[atual][n]+1
                    fathers[filho][n][1] = atual
                    fathers[filho][n][0] = transporte

        self.fathers = fathers.copy()
        self.heuristicas = altitude.copy()

  
    def BFS_2(self, init):
        ### BFS to calculate the depth (Used as heuristic for Aast_2)

        U = self.model
        atual = self.goal[0]
        qq = []

        altitude = [0 for _ in range(len(U))]
        visited = [False for _ in range(len(U))]
        

        qq.append(atual)
        visited[atual] = True
        altitude[atual] = 0

        while (len(qq)!=0):
            atual = qq.pop(0)
            for destino in U[atual]:
                filho = destino[1]
                if (not visited[filho]):
                    qq.append(filho)
                    visited[filho] = True
                    altitude[filho] = altitude[atual]+1

        self.heuristicas = altitude.copy()
 
    def Aast_2(self, init, ticks):
        
        U = self.model
        goal = self.goal[0]
        h = self.heuristicas

        qq = []
        qq.append((h[init], init, ticks))

        visited = [[] for _ in range(len(U))]
        fathers = [[None]*2 for _ in range(len(U))]
        tickets = [[0]*3 for _ in range(len(U))]

        tickets[init] = ticks.copy()
        visited[init].append(tickets)
  

        while (len(qq) != 0):
            l = qq.pop(0)
            atual = l[1]
            tickets[atual] = l[2]

            if (atual == goal):
                break
            for caminho in U[atual]:
                filho = caminho[1]
                transporte = caminho[0]

                ticks = tickets[atual].copy()
                ticks[transporte] -= 1
                if (tickets[atual][transporte] != 0 and visited[filho].count(ticks) == 0 and fathers[atual][1] != filho):

                    tickets[filho] = ticks.copy()

                    bisect.insort(qq, (h[filho], filho, tickets[filho]))
                    
                    fathers[filho][1] = atual
                    fathers[filho][0] = transporte
                    visited[filho].append(tickets[filho])

        self.fathers = fathers.copy()

	
