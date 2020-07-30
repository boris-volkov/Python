import time
from matplotlib import pyplot as plt
import sys
from math import ceil, floor, sqrt 
plt.rcParams['axes.facecolor'] = '#471223'
plt.rcParams['figure.figsize'] = 11,11

def factors(start, n):
    mults = []
    facts = []
    for i in range(1, n//2 + 1):
        times = ceil(start/i)
        multiple = i
        if i*times < n:
            while multiple <= n-i:
                multiple = i*times
                times += 1
                mults.append(multiple) 
                facts.append(i)
    for i in range(max(n//2 + 1,start), n + 1):
        mults.append(i)
        facts.append(i)
    return (mults,facts)

def squares(start, n):
    mults = []
    facts = []
    for i in range(ceil(sqrt(start)), floor(sqrt(n)) + 1):
        mults.append(i**2)
        facts.append(i)
    return (mults,facts)

def isolate_parabola(vertex):
    mults = []
    facts = []
    root = round(sqrt(vertex))
    for i in range(root):
        mults.append(vertex-i**2)
        facts.append(root-i)
        mults.append(vertex-i**2)
        facts.append(root+i)
    return (mults,facts)

def plot(bottom, top, parabola = None, save = None):
    X,Y = factors(bottom, top)
    A,B = squares(bottom, top) 
    plt.scatter(X,Y, color = 'yellow', s = 0.5)
    plt.scatter(A,B, color = 'cyan', s = 1)
    if parabola: 
        P,Q = isolate_parabola(parabola)
        plt.scatter(P,Q, color = 'white', s = 17)
    title = str(time.time())
    if save == 's': plt.savefig(title+ '.svg', format='svg', dpi = 1200)
    plt.show()

def plot_text(bottom, top, parabola = None):
    X,Y = factors(bottom, top)
    for x,y in zip(X,Y):
        plt.scatter(x,y, alpha = 0)
        plt.text(x,y, str(y), color = 'yellow', fontsize = 7)
    A,B = squares(bottom,top)
    for a,b in zip(A,B):
        plt.text(a,b, str(b), color = 'cyan', fontsize = 7)
    P,Q = isolate_parabola(parabola)
    for p,q in zip(P,Q):
        plt.text(p,q, str(q), color = 'white', fontsize = 7)
    plt.show()

if __name__ == '__main__':
    if sys.argv[-1] == 'txt':
        plot_text(int(sys.argv[1]), 
                int(sys.argv[2]), int(sys.argv[3]))
    elif len(sys.argv) > 3:
        plot(int(sys.argv[1]), 
                int(sys.argv[2]), int(sys.argv[3]), save = sys.argv[-1])
    else:
        plot(int(sys.argv[1]), int(sys.argv[2]))    
    
