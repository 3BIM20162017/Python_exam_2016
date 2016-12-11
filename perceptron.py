#! /usr/bin/env python
#-*- coding:utf-8 -*-

from random import randint, gauss, shuffle


class Perceptron:
  """docstring for Perceptron"""
  def __init__(self, dataset, b, alpha):
    
    self.alpha = alpha
    self.b = b
    self.dataset = dataset
    self.wm = [[gauss(0,self.b) for _ in range(len(self.dataset[0])-1)] for _ in range(len(self.dataset))]
    self.bin = [None]*len(self.dataset)

    self.assign_bin()

  def assign_bin(self):
    for i, elt in enumerate(self.dataset):
      s_w = 0
      for j, dim in enumerate(elt) :
        if dim != elt[-1]:
          s_w += dim*self.wm[i][j]
      self.bin[i] = 1 if s_w > 0 else -1

  def compute_weights(self):
    for i, elt in enumerate(self.dataset):
      gam = self.bin[i]
      y = elt[-1]
      for j, dim in enumerate(elt):
        if dim != elt[-1]:
          self.wm[i][j] += self.alpha*(y-gam)*dim


def generate_dataset(a,b,c,d,le):
  """Generates a dataset based on normal normal distributions"""
  m1 = []
  p1 = []
  for _ in range(le/2):
    m1.append((gauss(a,1),gauss(b,1),-1))
    p1.append((gauss(c,1),gauss(d,1),1))
  dataset = m1+p1
  shuffle(dataset)
  return dataset

def get_bin_dataset(dataset): 
  """Returns an array with the last element of every element in dataset"""
  bi = []
  for elt in dataset:
    bi.append(elt[-1])
  return bi

if __name__ == '__main__':
  

  # my_dataset =  [[1,2,3,-1],[2,4,3,-1],[4,5,6,1],[8,9,4,1],[1,2,3,-1],[2,4,3,-1],[4,5,6,1],[8,9,4,1],[1,2,3,-1],[2,4,3,-1],[4,5,6,1],[8,9,4,1]]
  dataset = generate_dataset(2,10,8,3,200)
  #print dataset  
  test = Perceptron(dataset, 0.1, 0.3)
  #print test.wm
  print test.bin
  for i in range(5):
    print "current: ", test.bin
    print "WANTED : ", get_bin_dataset(test.dataset)
    print "-----------------------------"
    test.compute_weights()
    test.assign_bin()
  for li in test.wm:
    print li
    
### REPONSE AUX QUESTIONS

"""
Je plot pas la matrice de confusion car l'algo converge à 100% avec généralement peu d'itérations
même pour un dataset de plusieurs centaines d'individus.

le param alpha du modèle permet de mettre plus ou moins de poids sur une mauvaise réponse. En d'autres
termes, si alpha est très grand, le système aura du mal à converger.
"""