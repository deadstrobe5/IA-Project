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

        self.BFS(init[0])
        

        if (tickets == [math.inf,math.inf,math.inf]):

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

    def BFS(self, init):
        start = self.goal[0]
        U = self.model
        qq = []
        altitude = [0 for _ in range(len(U))]
        visited = [False for _ in range(len(U))]
        fathers = [[None]*2 for _ in range(len(U))]


        atual = start
        qq.append(atual)
        visited[atual] = True
        altitude[atual] = 0

        while (len(qq)!=0):
            atual = qq.pop(0)
            '''if (atual == init):
                break'''
            for destino in U[atual]:
                filho = destino[1]
                transporte = destino[0]
                if (not visited[filho]):
                    qq.append(filho)
                    visited[filho] = True
                    altitude[filho] = altitude[atual]+1
                    fathers[filho][1] = atual
                    fathers[filho][0] = transporte

        self.fathers = fathers.copy()
        self.heuristicas = altitude.copy()

 



    '''
    def backtrack(self,expansao):

        item = expansao.pop()
        while(item.length()==0):
            #REMOVE(item)
            pass
        
        return
        '''

	
