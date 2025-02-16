import random 
def lifeline1(j):
 n=4
 axs="".join(j[5:6])
 if axs =="a":
    ans=1
 elif axs=="b":
    ans=2
 elif axs=="c":
    ans=3
 else:
    ans=4
 
 
 match ans:
    case 1:
       a=0
       
       while a<=1:
          rand=random.randint(2,n)
          j.pop(rand)
          a=a+1
          
          n=n-1
    case 2:
       a=0
       aks=j[2:3]
       while a<=1:
          rand=random.randint(1,n) 
          new=j[rand:rand+1]
          
          if aks==new:
             a=a+0
             continue
             
          else:
             j.pop(rand)
             a=a+1
          n=n-1
          
    case 3:
       a=0
       aks=j[3:4]
       while a<=1:
          rand=random.randint(1,n) 
          new=j[rand:rand+1]
          
          if aks==new:
             a=a+0
             continue
             
          else:
             j.pop(rand)
             a=a+1
          n=n-1
          
    case 4:
       a=0
       n=3
       while a<=1:
          rand=random.randint(1,n)
          j.pop(rand)
          a=a+1
          
          n=n-1
    case _:
       exit()

 print(f"""
{j[0:1]}
                              {j[1:2]} 
                                     
                                      {j[2:3]}
""")