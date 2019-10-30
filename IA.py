# 89452 Guilherme Palma | 89400 Afonso Ribeiro

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
                node = [[self.fathers[index][0][0]],[self.fathers[index][0][1]]]
            
            return output1



        # EXERCICIO 2
        
        elif (len(init) == 1): 
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
                node[0] = [fathers[index][0][0]]
                output1.insert(0, node)
                node = [[],[fathers[index][0][1]]]
                
            output1[0][0] = []

            return output1


        # EXERCICIO 3
    
        elif(len(init) == 3 and tickets == [math.inf,math.inf,math.inf]):

            self.heuristicas = [[0]*3 for _ in range(len(self.model))]
            self.paths = [[] for _ in range(3)]
            self.fathers = [[[0, 0],[0, 0],[0, 0]] for _ in range(len(self.model))]

            return [] # o codigo para este exercicio nao esta funcionar

            self.BFS_3(init[0], 0)
            self.BFS_3(init[1], 1)
            self.BFS_3(init[2], 2)

            self.Aast_3(init[0], 0)
            self.Aast_3(init[1], 1)
            self.Aast_3(init[2], 2)

            caminhoA1 = self.paths[0]
            caminhoA2 = self.paths[1]
            caminhoA3 = self.paths[2]


            caminhos = [caminhoA1,caminhoA2,caminhoA3]


            while(1>0):

                size1 = len(caminhos[0])
                size2 = len(caminhos[1])
                size3 = len(caminhos[2])

                sizes = [size1,size2,size3]

                maxS = max(sizes)

                for i in range(3):
                    if (sizes[i]<maxS):
                        conseguiu = self.rePath(caminhos[i], i, maxS, self.goal[i])
                        if(not conseguiu):
                            Index = i
                            break
                if (Index!=-1):
                    caminhos[Index] = self.AumentaCaminho2(caminhos[Index])
                else:
                    break
                

            return output1
        
        else:
            return []

    def AumentaCaminho2(self, path):
        path.insert(2,[path[1][0],path[0][1]])
        path.insert(3,path[1].copy)
        return path
    
    def rePath(self, path, n, size, goal):

        
        model = self.model
        alt = self.heuristicas[path[0][1][0]][n]
        destinos = []

        if((size-len(path))%2 == 0):
            for i in range((size-len(path))//2):
                path = self.AumentaCaminho2(path)
            return True
        else:
            for elem in path:
                destinos.append(elem[1][0])
            while (alt > 0):
                nivelAnt = False
                ligado = None
                for i in range(len(model)):
                    node = model[i]
                    if (self.heuristicas[i][n]==alt):
                        for j in range(len(node)) :
                            if (self.heuristicas[node[j][1]][n] == alt-1):
                                nivelAnt = True
                            if (node[j][1] in destinos):
                                ligado = node[j][1]

                        if (nivelAnt and ligado!=None):
                            path = self.meterNoPath(i,path,goal,ligado,n)
                            return True


                alt-=1

            return False

    def meterNoPath(self, MainNo, path, goal, ligado, n):

        FinalPath = []
        NoC = 0

        for i in range(len(path)):
            ligacao = path[i]
            if (ligacao[1]==ligado):
                NoC=i
                parte = path.copy()
                FinalPath = parte[0:i+1]
                break
        
        for j in range(len(self.model[i])):
            ligacao = path[j]
            if (ligacao[1]==MainNo):
                FinalPath.append[ligacao]
                break
        
        
        node = self.fathers[MainNo][n]

        

        while(node[1]!=goal):
            FinalPath.append(node)
            node = self.fathers[node[1]][n]

        return FinalPath.copy()
    

#################################################

    def BFS_1(self, init):
        ### BFS for the 1st Exercise

        atual = self.goal[0]
        U = self.model
        qq = []
        #altitude = [0 for _ in range(len(U))]
        visited = [False for _ in range(len(U))]
        fathers = [[[0, 0],[0, 0],[0, 0]] for _ in range(len(U))]

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
                    lst = [atual, transporte]
                    fathers[filho][0][1] = atual
                    fathers[filho][0][0] = transporte
                    

        self.fathers = fathers.copy()
        #self.heuristicas = altitude.copy()


#######################################################

    def BFS_3(self, init, n):
        ### BFS for the 3rd Exercise

        atual = self.goal[n]
        U = self.model
        qq = []
        
        visited = [False for _ in range(len(U))]

        qq.append(atual)
        visited[atual] = True
        self.heuristicas[atual][n] = 0

        while (len(qq)!=0):
            atual = qq.pop(0)
            for destino in U[atual]:
                filho = destino[1]
                transporte = destino[0]
                if (not visited[filho]):
                    qq.append(filho)
                    visited[filho] = True
                    self.heuristicas[filho][n] = self.heuristicas[atual][n]+1



    def Aast_3(self, init, n):

        U = self.model
        goal = self.goal[n]
        h = self.heuristicas
        path = self.paths
        g = False
        qq = []
        qq.append((h[init], init))
        i=0

        visited = [False for _ in range(len(U))]


        
        
        while (len(qq) != 0):

        
            l = qq.pop(0)
            atual = l[1]

            for k in range(0,3):
                if (k < n and len(path[k]) > i):
                    if(path[k][i][1][0] == atual):
                        if (self.resolve_conflict(self.fathers[atual][n][1], atual, init, n, k)):
                            g = True
                            break
            if(g):
                break

            if (atual == goal):
                break
            for caminho in U[atual]:
                filho = caminho[1]
                transporte = caminho[0]

                if (not visited[filho]):
                    
                        
                    bisect.insort(qq, (h[filho][n], filho))
                    
                    self.fathers[filho][n][1] = atual
                    self.fathers[filho][n][0] = transporte
                    visited[filho] = True
            i+=1


        output1 = []
        node = [[], [goal]]
        index = goal

        while (index != init):
            index = node[1][0]
            node[0] = [self.fathers[index][n][0]]
            output1.insert(0, node)
            node = [[],[self.fathers[index][n][1]]]
            
        output1[0][0] = []

        self.paths[n] = output1.copy()

    def resolve_conflict(self, atual, col, pai, n, path_ind):
        k1 = atual
        k2 = self.fathers[col][path_ind][1]
        U = self.model
        h = self.heuristicas
        paths = self.paths

        while(1):
            for caminho in U[k1]:
                
                nut = caminho[1]
                if (h[nut][n] == h[col][n] and nut != col):
                   if (self.Aast_3_aux(nut, n)):
                       return True
            for caminho in U[k2]:
                
                nut = caminho[1]
                if (h[nut][path_ind] == h[col][path_ind] and nut != col):

                    self.Aast_3_aux(nut, path_ind)
                    

            if(k1 == pai or k2 == self.init[path_ind]):
                break
            k1 = self.fathers[k1][n][1]
            k2 = self.fathers[k2][n][1]

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
            filho = 0

            if (not visited[filho]):
                    for k in range(0,3):
                        if (k < n and len(path[k]) > i and path[k][i][1][0] == filho):
                            if ( self.resolve_conflict(atual, filho, init, n, k)):
                                g = True
                                break
            if(g):
                break
            if (atual == goal):
                break
            for caminho in U[atual]:
                filho = caminho[1]
                transporte = caminho[0]
                        
                bisect.insort(qq, (h[filho][n], filho))
                
                self.fathers[filho][n][1] = atual
                self.fathers[filho][n][0] = transporte
                visited[filho] = True
            i+=1
        
        output1 = []
        node = [[], [goal]]
        index = goal

        while (index != init):
            index = node[1][0]
            node[0] = [self.fathers[index][n][0]]
            output1.insert(0, node)
            node = [[],[self.fathers[index][n][1]]]
            
        output1[0][0] = []

        self.paths[n] = output1.copy()

        return g





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
        fathers = [[[0, 0],[0, 0],[0, 0]] for _ in range(len(U))]
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
                if (tickets[atual][transporte] != 0 and visited[filho].count(ticks) == 0 and fathers[atual][0][1] != filho):
                        
                    tickets[filho] = ticks.copy()
                    ticks.reverse()
                    bisect.insort(qq, (h[filho], filho, ticks))
                    
                    fathers[filho][0][1] = atual
                    fathers[filho][0][0] = transporte

                    visited[filho].append(tickets[filho])

        
        self.fathers = fathers.copy()

	
