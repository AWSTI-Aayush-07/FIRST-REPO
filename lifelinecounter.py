
def counter(l1,l2):
 ask=int(input("Which lifeline do you want : "))
 if ask ==1:
    def life1(l1):
       return l1==1,l2==0
 else:
   def life2(l2):
     return l1==0,l2==1
   
print(counter(l1=0,l2=0)+1)