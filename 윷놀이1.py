import sys
import numpy as np
import matplotlib.pyplot as plt
import math


mo_truth=0 
do_truth=0
gae_truth=0
geol_truth=0
yut_truth=0
def binomial_dist(n, k, p):
    if k > n:
        print ('k can not be greater than n')
        sys.exit(1)
    else: 
        pp = (3/2)*(1/(math.factorial(4-k)*math.factorial(k)))
        return pp  ## else -> find real probablity value & restore in variable pp
    
    
    
   

def yutNori(step, prob_head=0.5):
  """
  np.random.binomial() 함수를 이용하여 윷놀이 실험을 구현하고
  matplotlib를 이용하여 윷놀이 실험 결과를 그래프로 나타내시오.
  """
  mocount=0
  docount=0
  gaecount=0
  geolcount=0
  yutcount=0


  a=np.random.binomial(4, 0.5, step)
  for j in range (step):
    if(a[j]==0):
      mocount+=1
    elif(a[j]==1):
      docount+=1
    elif(a[j]==2):
      gaecount+=1
    elif(a[j]==3):
      geolcount+=1
    elif(a[j]==4):
      yutcount+=1  ## step사이즈크기의 배열을 선언하고 배열의 인자의 범위를 4로 잡는다. 
                   ## 0인자는 모, 1인자는 도, 이런식으로 인자를 카운트해서 변수에 넣는다.  find experimental value 1
                     
  mo_truth = binomial_dist(4, 0, 0.5)
  do_truth = binomial_dist(4, 1, 0.5)
  gae_truth = binomial_dist(4, 2, 0.5)
  geol_truth = binomial_dist(4, 3, 0.5)
  yut_truth = binomial_dist(4, 4, 0.5)  ## find real value 

  mo=mocount/step
  do=docount/step
  gae=gaecount/step
  geol=geolcount/step
  yut=yutcount/step   ## find experimental value 2

  sum_of_probability = mo + do + gae + geol + yut
  
  if sum_of_probability != 1:
    print ('Sum of probability is zero')
    sys.exit(1)
  
  
  print ('Probability mo: %f, %f' %(mo, mo_truth) + \
        '\nProbability do: %f, %f' %(do, do_truth) + \
        '\nProbability gae: %f, %f' %(gae, gae_truth) + \
        '\nProbability geol: %f, %f' %(geol, geol_truth) + \
        '\nProbability yut: %f, %f' %(yut, yut_truth))

  

  x=['mo', 'do', 'gae', 'geol', 'yut']
  y1=[mo_truth, do_truth, gae_truth, geol_truth, yut_truth]
  y2=[mo, do, gae, geol, yut]  ## make arrangement for graph
  

  plt.subplot(2,1,1)
  plt.bar(x,y1)
  plt.title("Experiment")
  plt.subplot(2,1,2)
  plt.bar(x,y2)
  plt.title("Truth") # setting two graphs
  
  
  

def main():
  if len(sys.argv) != 2:
    print ('usage: ./yut.py step')
    sys.exit(1)

  step = int(sys.argv[1])

  yutNori(step=step)


if __name__ == '__main__':
  main() 


plt.show()  ## showing graphs over window
