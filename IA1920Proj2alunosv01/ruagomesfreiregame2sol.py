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
                #print(self.q_matrix[st][0:len(aa)])
                a = self.q_matrix[st].index(numpy.max(self.q_matrix[st][0:len(aa)]))
                return a

        # Select one action, used when evaluating
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontoexecute(self,st,aa):
                a = self.q_matrix[st].index(numpy.max(self.q_matrix[st][0:len(aa)]))
                return a


        # this function is called after every action
        # st - original state
        # nst - next state
        # a - the index to the action taken
        # r - reward obtained
        def learn(self,ost,nst,a,r):
                max_b = numpy.max(self.q_matrix[nst][0:len(self.aa)])
                original_q = self.q_matrix[ost][a]

                new_q = original_q + L_RATE*(r + DISCOUNT * max_b)
                #print(new_q)
                self.q_matrix[ost][a] = new_q
                
                return
