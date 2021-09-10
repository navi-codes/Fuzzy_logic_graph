"""
Title:     fuzzy logic Program
Author:    A Navaneethraj
Version:   5.2.0 (Arithmetic operations)
python Version: 3.5.2
"""
import matplotlib.pyplot as mpl
import matplotlib.patches as mpatches

class FuzzyLogic():

    def __init__(self):
        self.graph_type = 0
        self.fuzzy_no = 0
        self.n_gonal = 0
        self.begin_again = True
        self.is_first = True
        self.graph_xa = []
        self.graph_ya = []
        self.graph_xb = []
        self.graph_yb = []

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

    def on_complete(self,graph_xc,graph_yc,label):
    #plotting the graph
        mpl.plot(graph_xc,graph_yc,color="blue",label=label)
        mpl.plot(self.graph_xa,self.graph_ya,color="red",label="A")
        mpl.plot(self.graph_xb,self.graph_yb,color="green",label="B")
    #printing the result
        self.print_result(self.graph_xa,self.graph_ya,name="A")
        self.print_result(self.graph_xb,self.graph_yb,name="B")
        self.print_result(graph_xc,graph_yc,name=label)
    #plotting the cross cutting line
        self.plot_cross(self.graph_xa,self.graph_ya,'--r')
        self.plot_cross(self.graph_xb,self.graph_yb,'--g')
        self.plot_cross(graph_xc,graph_yc,'--b')
        mpl.legend()

    def Addition(self):
        graph_xc=[float(format(self.graph_xa[i]+self.graph_xb[i],'.5f'))for i in range(0,len(self.graph_xa))]
        graph_yc=self.get_graph_y()
        angle = self.get_angel()
        if(angle==1):
            self.on_complete(graph_xc,graph_yc,"A+B")
        elif(angle==2):
            self.to_reverse(graph_xc,graph_yc,"A+B")

    def Subtraction(self):
        self.sub_graph_xb=self.graph_xb[::-1]
        graph_xc=[float(format(self.graph_xa[i]-self.sub_graph_xb[i],'.5f'))for i in range(0,len(self.graph_xa))]
        graph_yc=self.get_graph_y()
        angle=self.get_angel()
        if(angle==1):
            self.on_complete(graph_xc,graph_yc,"A-B")
        elif(angle==2):
            self.to_reverse(graph_xc,graph_yc,"A-B")
        else:
            print("Invalid input")
            self.Subtraction()

    def Multiplication(self):
        midpoint=self.get_mid_point()
        graph_yc=self.get_graph_y()
        if(self.graph_type==1):
            graph_xc=[self.graph_xa[midpoint]*self.graph_xb[midpoint]]
            for i in range(1,midpoint+1):
                temp=[(self.graph_xa[midpoint-i]*self.graph_xb[midpoint-i]),(self.graph_xa[midpoint-i]*self.graph_xb[midpoint+i]),(self.graph_xa[midpoint+i]*self.graph_xb[midpoint-i]),(self.graph_xa[midpoint+i]*self.graph_xb[midpoint+i])]
                graph_xc.append(float(format(max(temp),'.5f')))
                graph_xc.append(float(format(min(temp),'.5f')))
                temp=[]
            graph_xc.sort()
            angle=self.get_angel()
            if(angle==1):
                self.on_complete(graph_xc,graph_yc,"A*B")
            elif(angle==2):
                self.to_reverse(graph_xc,graph_yc,"A*B")
        elif(self.graph_type==2):
            graph_xc=[]
            for i in range(0,midpoint[1]):
                temp=[(self.graph_xa[(midpoint[0])-i]*self.graph_xb[(midpoint[0])-i]),(self.graph_xa[(midpoint[0])-i]*self.graph_xb[(midpoint[1])+i]),(self.graph_xa[(midpoint[1])+i]*self.graph_xb[(midpoint[0])-i]),(self.graph_xa[(midpoint[1])+i]*self.graph_xb[(midpoint[1])+i])]
                graph_xc.append(float(format(max(temp),'.5f')))
                graph_xc.append(float(format(min(temp),'.5f')))
                temp=[]
            graph_xc.sort()
            angle=self.get_angel()
            if(angle==1):
                self.on_complete(graph_xc,graph_yc,"A*B")
            elif(angle==2):
                self.to_reverse(graph_xc,graph_yc,"A*B")

    def Division(self):
        self.div_graph_xb=self.graph_xb[::-1]
        graph_yc=self.get_graph_y()
        angle=self.get_angel()
        graph_xc = []
        midpoint = self.get_mid_point()
        if(self.graph_type==1):
            graph_xc=[self.graph_xa[midpoint]*(1/(self.div_graph_xb[midpoint]))]
            for i in range(1,midpoint+1):
                temp=[(self.graph_xa[midpoint-i]*(1/(self.div_graph_xb[midpoint-i]))),(self.graph_xa[midpoint-i]*(1/(self.div_graph_xb[midpoint+i]))),(self.graph_xa[midpoint+i]*(1/(self.div_graph_xb[midpoint-i]))),(self.graph_xa[midpoint+i]*(1/(self.div_graph_xb[midpoint+i])))]
                graph_xc.append(float(format(max(temp),'.5f')))
                graph_xc.append(float(format(min(temp),'.5f')))
                temp=[]
        elif(self.graph_type==2):
            for i in range(0,midpoint[1]):
                    temp=[(self.graph_xa[(midpoint[0])-i]*(1/(self.div_graph_xb[(midpoint[0])-i]))),(self.graph_xa[(midpoint[0])-i]*(1/(self.div_graph_xb[(midpoint[1])+i]))),(self.graph_xa[(midpoint[1])+i]*(1/(self.div_graph_xb[(midpoint[0])-i]))),(self.graph_xa[(midpoint[1])+i]*(1/(self.div_graph_xb[(midpoint[1])+i])))]
                    graph_xc.append(float(format(max(temp),'.5f')))
                    graph_xc.append(float(format(min(temp),'.5f')))
                    temp=[]
        graph_xc.sort()
        if(angle==1):
            self.on_complete(graph_xc,graph_yc,"A/B")
        elif(angle==2):
            self.to_reverse(graph_xc,graph_yc,"A/B")

    def minimum(self):
        graph_xc=[float(format(min(self.graph_xa[i],self.graph_xb[i]),'.5f')) for i in range(len(self.graph_xa))]
        graph_yc=self.get_graph_y()
        angle=self.get_angel()
        if(angle==1):
            self.on_complete(graph_xc,graph_yc,"Min(A,B)")
        elif(angle==2):
            self.to_reverse(graph_xc,graph_yc,"Min(A,B)")

    def maximum(self):
        graph_xc=[float(format(max(self.graph_xa[i],self.graph_xb[i]),'.5f')) for i in range(len(self.graph_xa))]
        graph_yc=self.get_graph_y()
        angle=self.get_angel()
        if(angle==1):
            self.on_complete(graph_xc,graph_yc,"Max(A,B)")
        elif(angle==2):
            self.to_reverse(graph_xc,graph_yc,"Max(A,B)")

    def scalar_mul(self):
        print("\n Enter the SCALAR VALUE:")
        multiplicand=int(input())
        graph_xc=[float(format(multiplicand*self.graph_xa[i],'.5f')) for i in range(len(self.graph_xa))]
        graph_xc.sort()
        print(multiplicand," * A = ",graph_xc,'\nAlpha cut value is ', self.graph_ya)
        angle=self.get_angel()
        if(angle==1):
            mpl.plot(graph_xc,self.graph_ya,color="blue",label="Scalar A")
            mpl.plot(self.graph_xa,self.graph_ya,color="red",label="Graph A")
            mpl.legend()
            self.plot_cross(self.graph_xa,self.graph_ya,'--r')
            self.plot_cross(graph_xc,self.graph_ya,'--b')
        elif(angle==2):
            self.reverse(self.graph_xa,self.graph_ya,color="red",label="A",crossColor='--r')
            self.reverse(graph_xc,self.graph_ya,color="blue",label="Scalar*A",crossColor='--b')

    def inverse(self):
        length_xa=len(self.graph_xa)-1
        graph_xc=[float(format(1/self.graph_xa[length_xa-i],'.5f'))for i in range(len(self.graph_xa))]
        graph_xc.sort()
        print("Inverse of A is",graph_xc,"\nAlpha cut value is ", self.graph_ya)
        angle=self.get_angel()
        if(angle==1):
            self.plot_cross(self.graph_xa,self.graph_ya,'--r')
            self.plot_cross(graph_xc,self.graph_ya,'--b')
            mpl.plot(graph_xc,self.graph_ya,color="blue",label="Inverse A")
            mpl.plot(self.graph_xa,self.graph_ya,color="red",label="Graph A")
            mpl.legend()
        elif(angle==2):
            self.reverse(self.graph_xa,self.graph_ya,color="red",label="A",crossColor='--r')
            self.reverse(graph_xc,self.graph_ya,color="blue",label="Inverse A",crossColor='--b')

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
        if (self.is_first and self.begin_again):
            print("Enter the n-gonal fuzzy number, where n= 2,3,4...\n")
            self.n_gonal=int(input())
            if(self.n_gonal<=1):
                print("invalid input\n")
                self.get_val(operation) #1 is invalid input so it will promt to inter again
            else:
                print("press \n 1 GRAPHICAL REPRESENTATION OF n-TRIANGULAR SHAPE FUZZY NUMBER \n 2 GRAPHICAL REPRESENTATION OF n-TRAPEZOIDAL SHAPE FUZZY NUMBER \n")
                self.graph_type=int(input())
                if 1<= self.graph_type <=2:
                    if(self.graph_type==1):
                        self.fuzzy_no=(2*self.n_gonal)-1 #formula
                    elif(self.graph_type==2):
                        self.fuzzy_no=2*self.n_gonal
                    if((operation>=1) and(operation<=6)):
                        print("\n ENTER ",self.fuzzy_no,"PARAMETERS FOR GRAPH A")
                        self.graph_xa=[float(input()) for i in range(0,self.fuzzy_no)] #Taking points from the user
                        self.graph_ya=self.get_graph_y()#Y axis value calculated and stoblue to the list
                        print("\n ENTER ",self.fuzzy_no," PARAMETERS FOR GRAPH B")
                        self.graph_xb=[float(input()) for i in range(0,self.fuzzy_no)] #Taking points from the user
                        #Y axis value and midpoint calculation
                        self.graph_yb=self.get_graph_y()
                    elif(operation>=7):
                        print("\n ENTER ",self.fuzzy_no," PARAMETERS FOR GRAPH A")
                        self.graph_xa=[float(input()) for i in range(0,self.fuzzy_no)] #Taking points from the user
                        self.graph_ya=self.get_graph_y()
                    self.is_first = False
                else:
                    print("\nInvalid input")
                self.get_val(operation)

    def menu(self,operation):
        if 1 <= operation <= 9:
            self.get_val(operation)
            if(operation==1):
               self.Addition()
            if(operation==2):
               self.Subtraction()
            if(operation==3):
               self.Multiplication()
            if(operation==4):
               self.Division()
            if(operation==5):
               self.minimum()
            if(operation==6):
               self.maximum()
            if(operation==7):
                self.scalar_mul()
            if(operation==8):
                self.inverse()
            if(operation==9):
                self.begin_again = False
        else:
            print("Invalid input try again")
            self.main()

    def print_result(self,graph_x,graph_y,name):
        compare=graph_x[1]-graph_x[0]
        midpoint=self.get_mid_point()
        isSymmetric = True
        if(self.graph_type==1):
            classic_no = graph_x[midpoint]
            l_limit=[float(format(graph_x[i+1]-graph_x[i],'.5f'))for i in range(0,(int(self.fuzzy_no/2)))]
            u_limit=[float(format(graph_x[i+1]-graph_x[i],'.5f'))for i in range((int((self.fuzzy_no)/2)),self.fuzzy_no-1)]
        elif(self.graph_type==2):
            classic_no = [graph_x[midpoint[0]],graph_x[midpoint[1]]]
            l_limit=[float(format(graph_x[i+1]-graph_x[i],'.5f'))for i in range(0,(int(self.fuzzy_no/2))-1)]
            u_limit=[float(format(graph_x[i+1]-graph_x[i],'.5f'))for i in range((int((self.fuzzy_no)/2)),self.fuzzy_no-1)]
        else:
            print("\n Invalid Input... Try again")
            self.main()
        for i in range(0,self.fuzzy_no-1):
            if((graph_x[i+1]-graph_x[i])!=compare):
                isSymmetric= False
        print("The classical number of ",name," is ",classic_no,)
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
        return(int(input("Press 1 Graphically Normal fuzzy number\nPress 2 Graphically Reverse order fuzzy number\n")))

    def to_reverse(self,graph_xc,graph_yc,label):
        self.reverse(self.graph_xa,self.graph_ya,color="red",label="A",crossColor='--r')
        self.reverse(self.graph_xb,self.graph_yb,color="green",label="B",crossColor='--g')
        self.reverse(graph_xc,graph_yc,color="blue",label=label,crossColor='--b')

    def main(self):
        while (self.begin_again==True):
            print("GRAPHICAL REPRESENTATION OF NEW ARITHMETICS OPERATIONS OF")
            print("FUZZY NUMBERS FOR TRAPEZOIDAL AND TRIANGULAR SHAPES")
            print("Press \n 1 ADDITION  2 SUBTRACTION   3 MULTIPLICATION  4 DIVISION \n 5 MINIMUM  6 MAXIMUM   7 SCALAR MULTIPLICATION   8 INVERSE  9 EXIT \n FUZZY NUMBERS\n")
            operation=int(input())
            self.menu(operation)
            if self.begin_again:
                mpl.title('GRAPHICAL REPRESENTATION OF FUZZY NUMBERS OPERATION')
                mpl.show()

fuzzy_processor = FuzzyLogic()
if __name__ == '__main__':
    fuzzy_processor.main()
