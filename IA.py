# 89452 89400
import math
import pickle
import time

class SearchProblem:

    heuristicas = []
    fathers = []

    def __init__(self,goal,model,auxheur = []):
        self.goal=goal
        self.model=model
        self.auxheur=auxheur
        pass
    def search(self, init, limitexp=2000, limitdepth = 20,tickets = [math.inf,math.inf,math.inf]):

        # PRIMEIRO EXERCICIO
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



        # SEGUNDO EXERCICIO
        elif (len(init) == 1):
            self.BFS_2(init[0], tickets)

            output1 = []
            node = [[],[init[0]]]
            index = init[0]
            while (index != self.goal[0]):
                index = node[1][0]
                output1.append([node[0],node[1]])
                node = [[self.fathers[index][0]],[self.fathers[index][1]]]



            return output1



        else:
            return []



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

    

    
    def BFS_2(self, init, tickets):
        ### BFS for the 2nd Exercise 

        U = self.model
        atual = self.goal[0]
        qq = []
        print(U[30])

        visited = [False for _ in range(len(U))]
        fathers = [[None]*2 for _ in range(len(U))]
        transports = [[None]*3 for _ in range(len(U))]

        qq.append(atual)
        visited[atual] = True
        transports[atual] = tickets.copy()

        while (len(qq)!=0):
            atual = qq.pop(0)
            if (atual == init):
                break
            for destino in U[atual]:
                filho = destino[1]
                used_transport = destino[0]
                if (not visited[filho]):

                    ticket = transports[atual][used_transport]
                    if(ticket == 0):
                        continue  
                    
                    transports[filho] = transports[atual].copy()
                    transports[filho][used_transport] -= 1
                    
                    qq.append(filho)
                    visited[filho] = True
                    fathers[filho][1] = atual
                    fathers[filho][0] = used_transport
                    if(filho == 60 or filho == 72 or filho == 55 or filho == 56):
                        print(filho)
                        print(transports[filho])

        self.fathers = fathers.copy()


 

        '''
    def A_asterisco(self, goal, U,):
        
        expansao = []
        qq = []
        path = []

        #temos de marcar os indices q ja passamos


        indice = qq.pop()

        while(1>0):
            if (indice == goal):
                return path

            expansao.append(indice)
            path.append(indice)
            lista = U[indice]
            if (lista.length!=0):
                for opcao in lista:
                    #if todas as opção marcadas ---> backtrack
                    transporte = opcao[0]
                    destino = opcao[1]
                    qq.push(destino)
            else :
                backtrack()

        return
        '''


    '''
    def backtrack(self,expansao):

        item = expansao.pop()
        while(item.length()==0):
            #REMOVE(item)
            pass
        
        return
        '''

	
