import numpy
import math
import copy

#similarity score
highSimilarity=1
mediumSimilarity=0.5
nothing=0

pc = numpy.corrcoef([1,2,3], [1,5,7])
print numpy.corrcoef([1,2,3], [1,5,7])

#testando algoritmo do calculo do coeficiente de Pearson
def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)


def similarity(pUsers):
    '''find the most user similarity based on Pearson of pUser analysed '''
    return min(pUsers, key=lambda x: abs(x - highSimilarity))





class User(object):

    def __init__(self):
        self.itens=[]

    def addItem(self,item):
        self.itens.append(item)

    def __repr__(self):
        return 'User(itens:"%s")' % (self.itens)

def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    print 'avarage x:',avg_x,' | avarage y:',avg_y
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)


def evaluation(v):

    if v<2:
        print 'not recommended item'
    elif v == 5:
        print'highly recommended item'
    else:
        'recommended item'


def moountAnalisys(userTarget,itemPos,users):
    analysis=[]
    pUsers=[]  #pearson users list
    itensUserTarget = userTarget.itens[:itemPos] + userTarget.itens[itemPos + 1:] #get itens except
    for u in users:
        #calculate pearson's correlation of users except the user analised
        #get users's itens except thar will be recommended
        itensUser=u.itens[:itemPos]+u.itens[itemPos+1:]
        pearson = pearson_def(itensUserTarget, itensUser)
        print 'itens user target:',itensUserTarget
        print 'itens user iterat:',itensUser
        print 'pearson:',pearson
        pUsers.append(pearson)

    print 'pearson calculated to userTarget:'
    print pUsers
    moreSimilar=similarity(pUsers)

    if moreSimilar >= 0:
        print 'more similarity:', moreSimilar
        userThatRecommend=users[pUsers.index(moreSimilar)]
        print 'the user target would be recommend item {0} based on {1} comportament'.format(itemPos + 1, userThatRecommend)
        print 'based on colaborative:'
        evaluation(userThatRecommend.itens[itemPos])


    else:
        print 'nothing can be predicted'









print 'pearson cor:',pearson_def([3,4,3,2], [4,4,4,2])


u1=User()
u1.itens=[3,0,4,3,2]

u2=User()
u2.itens=[4,5,4,4,2]

u3=User()
u3.itens=[5,1,1,5,4]

u4=User()
u4.itens=[4,5,3,3,3]

u5=User()
u5.itens=[1,3,0,2,0]

users=[u1,u2,u3,u4,u5]



def registrarItens():
    nItens = int(raw_input('digite o numero de itens a serem avaliados:\n'))
    nUsers = int(raw_input('digite o numero de usuarios do sistema:\n'))
    matriz = []
    n = 2
    for i in range(nUsers):
        tmp = []
        for j in range(nItens):
            elemento = input("Digite a avaliacao do item {1} do usuario  {0}  na escala 1-5:\n".format(i + 1, j + 1))
            tmp.append(elemento)

        matriz.append(tmp[:])

    print matriz


print 'usuarios:\n'
for u in users:
    print u
print 'mount analysis'
userTarget=users[0]
temp=copy.deepcopy(users)
temp.remove(temp[0])
print 'list of users to be analysed:',temp
moountAnalisys(userTarget,1,temp)

