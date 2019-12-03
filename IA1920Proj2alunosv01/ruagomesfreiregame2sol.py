import random
import numpy

DISCOUNT = 0.9
L_RATE = 0.1


# LearningAgent to implement
# no knowledeg about the environment can be used
# the code should work even with another environment
class LearningAgent:

        # init
        # nS maximum number of states
        # nA maximum number of action per state
        def __init__(self,nS,nA):

                self.aa = []
                self.nS = nS
                self.nA = nA
                self.q_matrix = [[0 for i in range(nA)] for j in range(nS)]
                '''
                for i in range (0, nS):
                        for j in range (0, nA):
                                self.q_matrix[i][j] = numpy.random.uniform(low = -2, high = 0)
                '''
                
              
        
        # Select one action, used when learning  
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontolearn(self,st,aa):
                self.aa = aa
                lista = []
                #print(self.q_matrix[st][0:len(aa)])
                for i in range(0,len(aa)):
                        print(self.q_matrix[st][aa[i]])
                        lista.append(self.q_matrix[st][aa[i]])
                
                a = self.q_matrix[st].index(numpy.max(lista))
                return a

        # Select one action, used when evaluating
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontoexecute(self,st,aa):
                lista = []
                #print(self.q_matrix[st][0:len(aa)])
                for i in range(0,len(aa)):
                        lista.append(self.q_matrix[st][aa[i]])
                
                a = self.q_matrix[st].index(numpy.max(lista))
                return a


        # this function is called after every action
        # st - original state
        # nst - next state
        # a - the index to the action taken
        # r - reward obtained
        def learn(self,ost,nst,a,r):
                lista = []
                #print(self.q_matrix[st][0:len(aa)])
                for i in range(0,len(self.aa)):
                        lista.append(self.q_matrix[nst][self.aa[i]])
                
                max_b = self.q_matrix[nst].index(numpy.max(lista))
                original_q = self.q_matrix[ost][a]

                new_q = original_q + L_RATE*(r + DISCOUNT * max_b)
                #print(new_q)
                self.q_matrix[ost][a] = new_q
                
                return
