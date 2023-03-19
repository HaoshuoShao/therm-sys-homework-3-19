from iapws import IAPWS97 as ip
import numpy as np

def get_alpha_1(p1, p2):
    x = 0.8950
    h3 = 2789.45
    h1 = 2796.61
    h2pp = 2783.77
    h2p = 798.5
    h7 = ip(P = p2, x = 0).h
    h8 = ip(P = p1, x = 0).h
    ho3 = ip(P = p1, s = 6.534).h
    beta = 0.4152
    return ((x + beta - beta*x)*h7 + (1-beta)*(1-x)*h2p - h8)/(h7 - ho3)

def get_alpha_2(a1, p1, p2):
    x = 0.8950
    h3 = 2789.45
    h1 = 2796.61
    h2pp = 2783.77
    beta = 0.4152
    h2p = 798.5
    h6 = 121.4
    h7 = ip(P = p2, x = 0).h
    h8 = ip(P = p1, x = 0).h
    ho2 = ip(P = p2, s = 6.534).h
    ho3 = ip(P = p1, s = 6.534).h
    return ((x+beta-beta*x-a1)*h6 - (x+beta-beta*x-a1)*h7)/(h6 - ho2)

def get_q_2(b, a1, a2):
    x = 0.895
    h4 = 1967.77
    h5 = 121.40
    return (1 - (1-b)*(1-x)-a1-a2)*(h4 - h5)

def get_w(q2):
    return (1 - q2/2075.59)

mat = np.empty([5,5], dtype = float) 

for i in range(5):
    for j in range(5):

        m = [0.6, 0.7, 0.8, 0.9, 1.0]
        n = [0.01, 0.1, 0.2, 0.3, 0.4]
        p_01 = m[i]
        p_02 = n[j]
        
        b = 0.4152
        a1 = get_alpha_1(p_01, p_02)
        a2 = get_alpha_2(a1, p_01, p_02)

        q2 = get_q_2(b, a1, a2)

        w_t = get_w(q2)
        if i == 2 and j == 2:
            print(b, a1, a2, w_t, q2)
        mat[i][j] = w_t

print(mat)
