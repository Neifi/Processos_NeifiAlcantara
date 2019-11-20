from multiprocessing import Pool, TimeoutError
#-*- coding: utf8 -*-

from datetime import datetime



def primers(num):
    for i in range(2, num/2):
        if num % i == 0:
            return False
        else:
            pass
    return True

if __name__ == '__main__':
    pool = Pool(4)
    
    l = range(40000000, 400000100)#[45445535, 56534563, 43566487, 43635453, 52346557, 53454433, 43546453, 26847357, 54577647]
    start = datetime.now()
    
    piscina = pool.map(primers,l)

    for k in l:
        for i in piscina:
            print (k,i)
        
   
    print datetime.now() - start
    """
    Per afegir mes o menys procesos a la pool a l'hora dinstanciar la clase Pool li pases per parametres el numero de procesos que vols
    que tingui la pool, el mes optim es ficar el maxim de cores en el numero de processos, ja que ficant un num major al num de cores de la cpu
    es bloquejara el pc i si no es bloqueja tampoc es fara més rápid. 
    """
