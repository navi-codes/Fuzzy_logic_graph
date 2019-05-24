"""
Title:     fuzzy logic Program
Author:    A Navaneethraj, RV Parthasarathi
Version:   5.1.0 (Arithmetic operations)
python Version: 3.5.2
"""
import matplotlib.pyplot as mpl
import matplotlib.patches as mpatches

class FuzzyLogic():

    def __init__(self):
        self.graph_type = 0
        self.fuzzy_no = 0
        self.n_gonal = 0

    def plot_cross(self,graph_x,graph_y,crossColor):
        #vertical cutting line
        for i in range (0,len(graph_x)):      #To plot the multiple cutting line
            temp_x=[graph_x[i],graph_x[i]]          #for sending the y value it plot for each cutting line it will move to the next y value
            temp_y=[0,graph_y[i]]
            mpl.plot(temp_x,temp_y,crossColor)
        #horizontal cutting line
            temp_y=[graph_y[i],graph_y[i]]          #for sending the y value it plot for each cutting line it will move to the next y value
            temp_x=[0,graph_x[i]]
            mpl.plot(temp_x,temp_y,'--c')

    def on_complete(self,graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,label):
    #plotting the graph
        mpl.plot(graph_xc,graph_yc,color="blue",label=label)
        mpl.plot(graph_xa,graph_ya,color="red",label="A")
        mpl.plot(graph_xb,graph_yb,color="green",label="B")
    #printing the result
        self.print_result(graph_xa,graph_ya,name="A")
        self.print_result(graph_xb,graph_yb,name="B")
        self.print_result(graph_xc,graph_yc,name=label)
    #plotting the cross cutting line
        self.plot_cross(graph_xa,graph_ya,'--r')
        self.plot_cross(graph_xb,graph_yb,'--g')
        self.plot_cross(graph_xc,graph_yc,'--b')
        mpl.legend()

    def Addition(self,graph_xa,graph_ya,graph_xb,graph_yb):
        graph_xc=[float(format(graph_xa[i]+graph_xb[i],'.5f'))for i in range(0,len(graph_xa))]
        graph_yc=self.get_graph_y()
        angle = self.get_angel()
        if(angle==1):
            self.on_complete(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A+B")
        elif(angle==2):
            self.to_reverse(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A+B")

    def Subtraction(self,graph_xa,graph_ya,graph_xb,graph_yb):
        graph_xb=graph_xb[::-1]
        graph_xc=[float(format(graph_xa[i]-graph_xb[i],'.5f'))for i in range(0,len(graph_xa))]
        graph_yc=self.get_graph_y()
        angle=self.get_angel()
        if(angle==1):
            self.on_complete(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A-B")
        elif(angle==2):
            self.to_reverse(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A-B")

    def Multiplication(self,graph_xa,graph_ya,graph_xb,graph_yb):
        midpoint=self.get_mid_point()
        if(self.graph_type==1):
            graph_xc=[graph_xa[midpoint]*graph_xb[midpoint]]
            for i in range(1,midpoint+1):
                temp=[(graph_xa[midpoint-i]*graph_xb[midpoint-i]),(graph_xa[midpoint-i]*graph_xb[midpoint+i]),(graph_xa[midpoint+i]*graph_xb[midpoint-i]),(graph_xa[midpoint+i]*graph_xb[midpoint+i])]
                graph_xc.append(float(format(max(temp),'.5f')))
                graph_xc.append(float(format(min(temp),'.5f')))
                temp=[]
            graph_xc.sort()
            graph_yc=self.get_graph_y()
            print("\nThe multiplication  of A and B is ",graph_xc)
            angle=self.get_angel()
            if(angle==1):
                self.on_complete(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A*B")
            elif(angle==2):
                self.to_reverse(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A*B")
        elif(self.graph_type==2):
            graph_xc=[]
            for i in range(0,midpoint[1]):
                temp=[(graph_xa[(midpoint[0])-i]*graph_xb[(midpoint[0])-i]),(graph_xa[(midpoint[0])-i]*graph_xb[(midpoint[1])+i]),(graph_xa[(midpoint[1])+i]*graph_xb[(midpoint[0])-i]),(graph_xa[(midpoint[1])+i]*graph_xb[(midpoint[1])+i])]
                graph_xc.append(float(format(max(temp),'.5f')))
                graph_xc.append(float(format(min(temp),'.5f')))
                temp=[]
            graph_xc.sort()
            graph_yc=self.get_graph_y()
            print("\nThe multiplication  of A and B is ",graph_xc)
            angle=self.get_angel()
            if(angle==1):
                self.on_complete(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A*B")
            elif(angle==2):
                self.on_complete(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A*B")

    def Division(self,graph_xa,graph_ya,graph_xb,graph_yb):
        graph_xb=graph_xb[::-1]
        graph_xc=[float(format(graph_xa[i]/graph_xb[i],'.5f'))for i in range(0,len(graph_xa))]
        graph_yc=self.get_graph_y()
        angle=self.get_angel()
        if(angle==1):
            self.on_complete(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A/B")
        elif(angle==2):
            self.to(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A/B")

    def minimum(self,graph_xa,graph_ya,graph_xb,graph_yb):
        graph_xc=[float(format(min(graph_xa[i],graph_xb[i]),'.5f')) for i in range(len(graph_xa))]
        graph_yc=self.get_graph_y()
        angle=self.get_angel()
        if(angle==1):
            self.on_complete(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"min AB")
        elif(angle==2):
            self.on_complete(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"min AB")


    def maximum(self,graph_xa,graph_ya,graph_xb,graph_yb):
        graph_xc=[float(format(max(graph_xa[i],graph_xb[i]),'.5f')) for i in range(len(graph_xa))]
        graph_yc=self.get_graph_y()
        angle=self.get_angel()
        if(angle==1):
            self.on_complete(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"max AB")
        elif(angle==2):
            self.to_reverse(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"max AB")

    def scalar_mul(self,graph_x,graph_y):
        print("\n enter the multiplicand")
        multiplicand=int(input())
        graph_xc=[float(format(multiplicand*graph_x[i],'.5f')) for i in range(len(graph_x))]
        graph_xc.sort()
        print(multiplicand," * A = ",graph_xc,'\nAlpha cut value is ', graph_y)
        angle=self.get_angel()
        if(angle==1):
            mpl.plot(graph_xc,graph_y,color="blue",label="Scalar A")
            mpl.plot(graph_x,graph_y,color="red",label="graph A")
            mpl.legend()
            self.plot_cross(graph_x,graph_y,'--r')
            self.plot_cross(graph_xc,graph_y,'--b')
        elif(angle==2):
            self.reverse(graph_x,graph_y,color="red",label="A",crossColor='--r')
            self.reverse(graph_xc,graph_y,color="blue",label="Scalar A",crossColor='--b')

    def inverse(self,graph_x,graph_y):
        j=len(graph_x)-1
        graph_xc=[float(format(1/graph_x[j-i],'.5f'))for i in range(len(graph_x))]
        graph_xc.sort()
        print("Inverse of A is",graph_xc,"\nAlpha cut value is ", graph_y)
        angle=self.get_angel()
        if(angle==1):
            self.plot_cross(graph_x,graph_y,'--r')
            self.plot_cross(graph_xc,graph_y,'--b')
            mpl.plot(graph_xc,graph_y,color="blue",label="Inverse A")
            mpl.plot(graph_x,graph_y,color="red",label="Graph A")
            mpl.legend()
        elif(angle==2):
            self.reverse(graph_x,graph_y,color="red",label="A",crossColor='--r')
            self.reverse(graph_xc,graph_y,color="blue",label="Inverse A",crossColor='--b')

    def reverse(self,graph_x,graph_y,color,label,crossColor):
        initial_length=len(graph_y)
        if((initial_length % 2)==0):
            graph_y = graph_y[(round((len(graph_y))/2)):len(graph_y)]
            graph_y.extend(graph_y[::-1])
            self.plot_cross(graph_x,graph_y,crossColor)
            mpl.plot(graph_x,graph_y,color=color,label=label)
            self.print_result(graph_x,graph_y,name=label)
            mpl.legend()
        else:
            if(initial_length==3):
                graph_y = graph_y[1:len(graph_y)]
                graph_y.append(graph_y[0])
                mpl.plot(graph_x,graph_y,color=color,label=label)
                self.plot_cross(graph_x,graph_y,crossColor)
                self.print_result(graph_x,graph_y,name=label)
                mpl.legend()
            else:
                graph_y = graph_y[(round((len(graph_y)-1)/2)):len(graph_y)]
                graph_y.extend(graph_y[-2::-1])
                mpl.plot(graph_x,graph_y,color=color,label=label)
                self.plot_cross(graph_x,graph_y,crossColor)
                self.print_result(graph_x,graph_y,name=label)
                mpl.legend()

    def get_val(self,operation):
        print("Enter the n-gonal fuzzy number, where n= 2,3,4...\n")
        self.n_gonal=int(input())
        if(self.n_gonal==1):
            print("invalid input\n")
            get_val() #1 is invalid input so it will promt to inter again
        else:
            print("press \n 1 GRAPHICAL REPRESENTATION OF n-TRIANGULAR SHAPE FUZZY NUMBER \n 2 GRAPHICAL REPRESENTATION OF n-TRAPEZOIDAL SHAPE FUZZY NUMBER \n")
            self.graph_type=int(input())
        if(self.graph_type==1):
            self.fuzzy_no=(2*self.n_gonal)-1 #formula
        elif(self.graph_type==2):
            self.fuzzy_no=2*self.n_gonal
        if((operation>=1) and(operation<=6)):
            print("\n ENTER ",self.fuzzy_no,"PARAMETERS FOR GRAPH A")
            graph_xa=[float(input()) for i in range(0,self.fuzzy_no)] #Taking points from the user
            graph_ya=self.get_graph_y()#Y axis value calculated and stoblue to the list
            print("\n ENTER ",self.fuzzy_no," PARAMETERS FOR GRAPH B")
            graph_xb=[float(input()) for i in range(0,self.fuzzy_no)] #Taking points from the user
            #Y axis value and midpoint calculation
            graph_yb=self.get_graph_y()
        elif(operation>=7):
            print("\n ENTER ",self.fuzzy_no," PARAMETERS FOR GRAPH A")
            graph_xa=[float(input()) for i in range(0,self.fuzzy_no)] #Taking points from the user
            graph_ya=self.get_graph_y()
        if(operation==1):
           self.Addition(graph_xa,graph_ya,graph_xb,graph_yb)
        if(operation==2):
           self.Subtraction(graph_xa,graph_ya,graph_xb,graph_yb)
        if(operation==3):
           self.Multiplication(graph_xa,graph_ya,graph_xb,graph_yb)
        if(operation==4):
           self.Division(graph_xa,graph_ya,graph_xb,graph_yb)
        if(operation==5):
           self.minimum(graph_xa,graph_ya,graph_xb,graph_yb)
        if(operation==6):
           self.maximum(graph_xa,graph_ya,graph_xb,graph_yb)
        if(operation==7):
            self.scalar_mul(graph_xa,graph_ya)
        if(operation==8):
            self.inverse(graph_xa,graph_ya)

    def print_result(self,graph_x,graph_y,name):
        compare=graph_x[1]-graph_x[0]
        midpoint=self.get_mid_point()
        isSymmetric = True
        if(self.graph_type==1):
            classic_no = graph_x[midpoint]
            l_limit=[float(format(graph_x[i+1]-graph_x[i],'.5f'))for i in range(0,(int(self.fuzzy_no/2)))]
            u_limit=[float(format(graph_x[i+1]-graph_x[i],'.5f'))for i in range((int((self.fuzzy_no)/2)),self.fuzzy_no-1)]
        elif(self.graph_type==2):
            classic_no = [graph_x[midpoint[0]],graph_x[midpoint[0]]]
            l_limit=[float(format(graph_x[i+1]-graph_x[i],'.5f'))for i in range(0,(int(self.fuzzy_no/2))-1)]
            u_limit=[float(format(graph_x[i+1]-graph_x[i],'.5f'))for i in range((int((self.fuzzy_no)/2)),self.fuzzy_no-1)]
        for i in range(0,self.fuzzy_no-1):
            if((graph_x[i+1]-graph_x[i])!=compare):
                isSymmetric= False
        print("The classic number of ",name," is ",classic_no,)
        print("\n Here, the fuzzy number: ",name,": (",graph_x[(int((self.fuzzy_no)/2))]," : ",l_limit[::-1],": ",u_limit,")")
        print("\n That is fuzzy number",name,': ',graph_x)
        print("\n Also, fuzzy number",name,"is",isSymmetric and 'SYMMETRIC' or 'NON-SYMMETRIC')
        print("\n Alpha cut value of graph ",name,"is :",graph_y)

    def get_graph_y(self):
        graph_y=[float(format(i/(self.n_gonal - 1),'.5f')) for i in range (0,self.n_gonal)]
        if(self.graph_type==1):#triangle
            graph_y=graph_y+graph_y[-2::-1]
            return(graph_y)
        elif(self.graph_type==2):#Trapisoid
            graph_y=graph_y+graph_y[-1::-1]
            return(graph_y)

    def get_mid_point(self):
        if(self.graph_type==1):
            return(int((self.fuzzy_no)/2))
        elif(self.graph_type==2):
            return([(int((self.fuzzy_no/2)-1)),(int(self.fuzzy_no/2))])

    def get_angel(self):
        return(int(input("Press 1 Graphicly Normal order fuzzy number\nPress 2 Graphicly Reverse order fuzzy number\n")))

    def to_reverse(self,graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,label):
        self.reverse(graph_xa,graph_ya,color="red",label="A",crossColor='--r')
        self.reverse(graph_xb,graph_yb,color="green",label="B",crossColor='--g')
        self.reverse(graph_xc,graph_yc,color="blue",label=label,crossColor='--b')

    def main(self):
        print("GRAPHICAL REPRESENTATION OF NEW ARITHMETICS OPERATIONS OF")
        print("FUZZY NUMBERS FOR TRAPEZOIDAL AND TRIANGULAR SHAPES")
        print("Press \n 1 ADDITION  2 SUBTRACTION   3 MULTIPLICATION  4 DIVISION \n 5 MINIMUM  6 MAXIMUM   7 SCALAR MULTIPLICATION   8 INVERSE \n FUZZY NUMBERS\n")
        operation=int(input())
        self.get_val(operation)
        mpl.title('Graphcal representation of  fuzzy numbers')
        mpl.show()

fuzzy_processor = FuzzyLogic()
if __name__ == '__main__':
    fuzzy_processor.main()
