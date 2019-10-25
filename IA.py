# 89452 89400
import math
import pickle
import time
import bisect

class SearchProblem:

    heuristicas = []
    fathers = []
    paths = []

    def __init__(self,goal,model,auxheur = []):
        self.goal=goal
        self.model=model
        self.auxheur=auxheur
        
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
                index = node[1][0]
                node[0] = [fathers[index][0]]
                output1.insert(0, node)
                node = [[],[fathers[index][1]]]
                
            output1[0][0] = []

            return output1


        # EXERCICIO 3
    
        elif(len(init) == 3 and tickets == [math.inf,math.inf,math.inf]):

            self.heuristicas = [[0]*3 for _ in range(len(self.model))]
            self.paths = [[] for _ in range(3)]
            self.init = init

            self.BFS_3(init[0], 0)
            self.BFS_3(init[1], 1)
            self.BFS_3(init[2], 2)

            self.Aast_3(init[0], 0)
            print(self.paths[0])
            self.Aast_3(init[1], 1)
            self.Aast_3(init[2], 2)


            print(self.paths[0])
            print(self.paths[1])
            print(self.paths[2])

            return [] 

        else:
            return []

    
    

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

        self.heuristicas = altitude.copy()


    def Aast_3(self, init, n):

        U = self.model
        goal = self.goal[n]
        h = self.heuristicas
        path = self.paths

        qq = []
        qq.append((h[init], init))
        i=0

        visited = [False for _ in range(len(U))]


        
        
        while (len(qq) != 0):
        
            l = qq.pop(0)
            atual = l[1]
            j = False

            if (atual == goal):
                break
            for caminho in U[atual]:
                filho = caminho[1]
                transporte = caminho[0]

                if (not visited[filho]):
                    for k in range(0,3):
                        if (k < n and len(path[k]) > i and path[k][i][1][0] == filho):
                            return self.resolve_conflict(atual, filho, init, n, k)
                        
                    bisect.insort(qq, (h[filho][n], filho))
                    
                    self.fathers[filho][1] = atual
                    self.fathers[filho][0] = transporte
                    visited[filho] = True
            i+=1


        output1 = []
        node = [[], [goal]]
        index = goal

        while (index != init):
            index = node[1][0]
            node[0] = [self.fathers[index][0]]
            output1.insert(0, node)
            node = [[],[self.fathers[index][1]]]
            
        output1[0][0] = []

        self.paths[n] = output1.copy()

    def resolve_conflict(self, atual, col, pai, n, path_ind):
        k1 = atual
        print(self.fathers[col])
        k2 = self.fathers[col][1]
        U = self.model
        h = self.heuristicas
        print(pai)
        paths = self.paths

        while(1):
            print("father")
            print(k1)
            print("Nuts")
            for caminho in U[k1]:
                nut = caminho[1]
                print(nut)
                if (h[nut][n] == h[col][n] and nut != col):
                   print("yo")
                   return self.Aast_3_aux(nut, n)

            for caminho in U[k2]:
                nut = caminho[1]
                print(nut)
                if (h[nut][n] == h[col][n] and nut != col):
                   print("yo")
                   self.Aast_3_aux(nut, n)
                   return self.Aast_3_aux(self.init[path_ind], n)

            if(k1 == pai and k2 == self.init[path_ind]):
                break
            k1 = self.fathers[k1][1]
            k2 = self.fathers[k2][1]

        return False

    def Aast_3_aux(self, init, n):

        U = self.model
        goal = self.goal[n]
        h = self.heuristicas
        path = self.paths

        qq = []
        qq.append((h[init], init))
        i=0

        visited = [False for _ in range(len(U))]
        
        
        while (len(qq) != 0):
        
            l = qq.pop(0)
            atual = l[1]

            if (atual == goal):
                break
            for caminho in U[atual]:
                filho = caminho[1]
                transporte = caminho[0]

                if (not visited[filho]):
                    for k in range(0,3):
                        if (k < n and len(path[k]) > i and path[k][i][1][0] == filho):
                            return self.resolve_conflict(atual, filho, init, n, k)
                        
                    bisect.insort(qq, (h[filho][n], filho))
                    
                    self.fathers[filho][1] = atual
                    self.fathers[filho][0] = transporte
                    visited[filho] = True
            i+=1
        
        return True





############################################################

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
        t = ticks.copy()
        t.reverse() 
        qq.append((h[init], init, t))

        visited = [[] for _ in range(len(U))]
        fathers = [[None]*2 for _ in range(len(U))]
        tickets = [[0]*3 for _ in range(len(U))]

        tickets[init] = ticks.copy()
        visited[init].append(tickets)

        # Os reverse() melhoram a eficiencia quando existe o mesmo no' na qq, mas com transportes diferentes, 
        # porque ele assim vai escolher taxis antes de metros.
        # Como os metros sao geralmente "mais valiosos" que os taxis, faz mais sentido escolher um taxi (ou um bus)
  
        while (len(qq) != 0):
            l = qq.pop(0)
            atual = l[1]
            tickets[atual] = l[2]

            tickets[atual].reverse()

            if (atual == goal):
                break
            for caminho in U[atual]:
                filho = caminho[1]
                transporte = caminho[0]

                ticks = tickets[atual].copy()
                ticks[transporte] -= 1
                if (tickets[atual][transporte] != 0 and visited[filho].count(ticks) == 0 and fathers[atual][1] != filho):
                        
                    tickets[filho] = ticks.copy()
                    ticks.reverse()
                    bisect.insort(qq, (h[filho], filho, ticks))
                    
                    fathers[filho][1] = atual
                    fathers[filho][0] = transporte
                    visited[filho].append(tickets[filho])

        self.fathers = fathers.copy()

	
