import pandas as pd
class tabla:
    def __init__(self,x,y):
        if isinstance(x,int) and 1<x<9:
            self.x=x
        else:
            pass
        if isinstance(y,int) and 1<y<9:
            self.y=y
        else:pass

    def generar(self):
        list1=[]
        list2=[]

        for i in range(self.x):
            list1.append(i)
        for j in range(self.y):
            list2.append(j)

        dt=pd.DataFrame(index=list1,columns=list2)
        for i 
        return dt

tabla1=tabla(5,6)
print(tabla1.generar())