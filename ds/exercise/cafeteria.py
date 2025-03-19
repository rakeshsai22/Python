from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  blocked = set()
  avail = 0
  S.sort()
  
  #for s in S:
  #  left = max(1,s-K)
  #  right = min(N,s+K)
  #  
  #  for seat in range(left,right+1):
  #    blocked.add(seat)
     
  #i=1
  #i=1
  #while i<=N:
  #  if i not in blocked:
  #    free+=1
  #    i+=K+1
  #  else:
  #    i+=1
      
  #return free
  
  first=S[0]
  free_seats = first - K -1
  if free_seats > 0:
    avail += (free_seats + K) // (K+1)
    
  for i in range(1,M):
    free_seats = S[i] - S[i-1] - 2*K-1
    if free_seats >0 :
      avail += (free_seats +K) // (K+1)
      
  last = S[-1]
  free_seats=N-last-K
  if free_seats >0:
    avail+= (free_seats + K) //(K+1)
    
  return avail
