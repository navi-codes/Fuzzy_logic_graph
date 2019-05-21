"""
Title:     fuzzy logic Program
Author:    A Navaneethraj, RV Parthasarathi
Version:   4.2.0 (Arithmetic operations)
python Version: 3.5.2
"""
import matplotlib.pyplot as mpl
import matplotlib.patches as mpatches


def plot_cross(graph_x,graph_y,crossColor):
    for i in range (0,len(graph_x)):      #To plot the multiple cutting line
        temp_x=[graph_x[i],graph_x[i]]          #for sending the y value it plot for each cutting line it will move to the next y value
        y=[0,graph_y[i]]
        mpl.plot(temp_x,y,crossColor)
        temp_x=[graph_y[i],graph_y[i]]          #for sending the y value it plot for each cutting line it will move to the next y value
        y=[0,graph_x[i]]
        clr="red"
        mpl.plot(y,temp_x,'--c')

def plot_graph(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,label):
    mpl.plot(graph_xc,graph_yc,color="blue",label=label)
    mpl.plot(graph_xa,graph_ya,color="red",label="A")
    mpl.plot(graph_xb,graph_yb,color="green",label="B")
    mpl.legend()

def Addition(graph_xa,graph_ya,graph_xb,graph_yb,fuzzy_no,n,option):
    graph_xc=[(graph_xa[i]+graph_xb[i])for i in range(0,len(graph_xa))]
    graph_yc,midpoint=basic_opp(option,graph_xc,n,fuzzy_no,"Addition of A and B")
    angle=int(input("Press 1 Graphicly Normal order fuzzy number\nPress 2 Graphicly Reverse order fuzzy number \n"))
    if(angle==1):
        plot_cross(graph_xa,graph_ya,'--r')
        plot_cross(graph_xb,graph_yb,'--g')
        plot_cross(graph_xc,graph_yc,'--b')
        plot_graph(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A+B")
    elif(angle==2):
        reverse(graph_xa,graph_ya,color="red",label="A",crossColor='--r')
        reverse(graph_xb,graph_yb,color="green",label="B",crossColor='--g')
        reverse(graph_xc,graph_yc,color="blue",label="A+B",crossColor='--b')

def Subtraction(graph_xa,graph_ya,graph_xb,graph_yb,fuzzy_no,n,option):
    graph_xb=graph_xb[::-1]
    graph_xc=[(graph_xa[i]-graph_xb[i])for i in range(0,len(graph_xa))]
    graph_yc,midpoint=basic_opp(option,graph_xc,n,fuzzy_no,"Subtraction of A and B")
    angle=int(input("Press 1 Graphicly Normal order fuzzy number\nPress 2 Graphicly Reverse order fuzzy number \n"))
    if(angle==1):
        plot_cross(graph_xa,graph_ya,'--r')
        plot_cross(graph_xb,graph_yb,'--g')
        plot_cross(graph_xc,graph_yc,'--b')
        plot_graph(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A-B")
    elif(angle==2):
        reverse(graph_xa,graph_ya,color="red",label="A",crossColor='--r')
        reverse(graph_xb,graph_yb,color="green",label="B",crossColor='--g')
        reverse(graph_xc,graph_yc,color="blue",label="A-B",crossColor='--b')

def Multiplication(graph_xa,graph_ya,graph_xb,graph_yb,fuzzy_no,n,option,midpoint):
    if(option==1):
        graph_xc=[graph_xa[midpoint]*graph_xb[midpoint]]
        for i in range(1,midpoint+1):
            temp=[(graph_xa[midpoint-i]*graph_xb[midpoint-i]),(graph_xa[midpoint-i]*graph_xb[midpoint+i]),(graph_xa[midpoint+i]*graph_xb[midpoint-i]),(graph_xa[midpoint+i]*graph_xb[midpoint+i])]
            graph_xc.append(max(temp))
            graph_xc.append(min(temp))
            temp=[]
        graph_xc.sort()
        graph_yc,midpoint=basic_opp(option,graph_xc,n,fuzzy_no,"Multiplication of A and  B")
        print("\nThe multiplication  of A and B is ",graph_xc)
        angle=int(input("Press 1 Graphicly Normal order fuzzy number\nPress 2 Graphicly Reverse order fuzzy number \n"))
        if(angle==1):
            plot_cross(graph_xa,graph_ya,'--r')
            plot_cross(graph_xb,graph_yb,'--g')
            plot_cross(graph_xc,graph_yc,'--b')
            plot_graph(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A*B")
        elif(angle==2):
            reverse(graph_xa,graph_ya,color="red",label="A",crossColor='--r')
            reverse(graph_xb,graph_yb,color="green",label="B",crossColor='--g')
            reverse(graph_xc,graph_yc,color="blue",label="A*B",crossColor='--b')

    elif(option==2):
        graph_xc=[]
        for i in range(0,midpoint[1]):
            temp=[(graph_xa[(midpoint[0])-i]*graph_xb[(midpoint[0])-i]),(graph_xa[(midpoint[0])-i]*graph_xb[(midpoint[1])+i]),(graph_xa[(midpoint[1])+i]*graph_xb[(midpoint[0])-i]),(graph_xa[(midpoint[1])+i]*graph_xb[(midpoint[1])+i])]
            graph_xc.append(max(temp))
            graph_xc.append(min(temp))
            temp=[]
        graph_xc.sort()
        graph_yc,midpoint=basic_opp(option,graph_xc,n,fuzzy_no,"C")
        print("\nThe multiplication  of A and B is ",graph_xc)
        angle=int(input("Press 1 Graphicly Normal order fuzzy number\nPress 2 Graphicly Reverse order fuzzy number \n"))
        if(angle==1):
            plot_cross(graph_xa,graph_ya,'--r')
            plot_cross(graph_xb,graph_yb,'--g')
            plot_cross(graph_xc,graph_yc,'--b')
            plot_graph(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A*B")
        elif(angle==2):
            reverse(graph_xa,graph_ya,color="red",label="A",crossColor='--r')
            reverse(graph_xb,graph_yb,color="green",label="B",crossColor='--g')
            reverse(graph_xc,graph_yc,color="blue",label="A*B",crossColor='--b')


def Division(graph_xa,graph_ya,graph_xb,graph_yb,fuzzy_no,n,option):
    graph_xb=graph_xb[::-1]
    graph_xc=[float(format(graph_xa[i]/graph_xb[i],'.5f'))for i in range(0,len(graph_xa))]
    graph_yc,midpoint=basic_opp(option,graph_xc,n,fuzzy_no,"Division of A by B")
    angle=int(input("press 1 Graphicly Normal order fuzzy number\npress 2 Graphicly Reverse order fuzzy number\n"))
    if(angle==1):
        plot_graph(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"A/B")
        plot_cross(graph_xa,graph_ya,'--r')
        plot_cross(graph_xb,graph_yb,'--g')
        plot_cross(graph_xc,graph_yc,'--b')
    elif(angle==2):
        reverse(graph_xa,graph_ya,color="red",label="A",crossColor='--r')
        reverse(graph_xb,graph_yb,color="green",label="B",crossColor='--g')
        reverse(graph_xc,graph_yc,color="blue",label="A/B",crossColor='--b')

def minimum(graph_xa,graph_ya,graph_xb,graph_yb,fuzzy_no,n,option):
    graph_xc=[min(graph_xa[i],graph_xb[i]) for i in range(len(graph_xa))]
    graph_yc,midpoint=basic_opp(option,graph_xc,n,fuzzy_no,"Minimum of A and B")
    angle=int(input("press 1 Graphicly Normal order fuzzy number\npress 2 Graphicly Reverse order fuzzy number\n"))
    if(angle==1):
        plot_graph(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"min")
        plot_cross(graph_xa,graph_ya,'--r')
        plot_cross(graph_xb,graph_yb,'--g')
        plot_cross(graph_xc,graph_yc,'--b')
    elif(angle==2):
        reverse(graph_xa,graph_ya,color="red",label="A",crossColor='--r')
        reverse(graph_xb,graph_yb,color="green",label="B",crossColor='--g')
        reverse(graph_xc,graph_yc,color="blue",label="min A/B",crossColor='--b')

def maximum(graph_xa,graph_ya,graph_xb,graph_yb,fuzzy_no,n,option):
    graph_xc=[max(graph_xa[i],graph_xb[i]) for i in range(len(graph_xa))]
    graph_yc,midpoint=basic_opp(option,graph_xc,n,fuzzy_no,"Maximum of A and B")
    angle=int(input("Press 1 Graphicly Normal order fuzzy number\nPress 2 Graphicly Reverse order fuzzy number\n"))
    if(angle==1):
        plot_graph(graph_xa,graph_ya,graph_xb,graph_yb,graph_xc,graph_yc,"max")
        plot_cross(graph_xa,graph_ya,'--r')
        plot_cross(graph_xb,graph_yb,'--g')
        plot_cross(graph_xc,graph_yc,'--b')
    elif(angle==2):
        reverse(graph_xa,graph_ya,color="red",label="A",crossColor='--r')
        reverse(graph_xb,graph_yb,color="green",label="B",crossColor='--g')
        reverse(graph_xc,graph_yc,color="blue",label="max A/B",crossColor='--b')

def scalar_mul(graph_x,graph_y):
    print("\n enter the multiplicand")
    multiplicand=int(input())
    graph_xc=[(multiplicand*graph_x[i]) for i in range(len(graph_x))]
    graph_xc.sort()
    print(multiplicand," * A = ",graph_xc,'\nAlpha cut value is ', graph_y)
    print()
    angle=int(input("Press 1 Graphicly Normal order fuzzy number\nPress 2 Graphicly Reverse order fuzzy number\n"))
    if(angle==1):
        mpl.plot(graph_xc,graph_y,color="blue",label="Scalar A")
        mpl.plot(graph_x,graph_y,color="red",label="graph A")
        mpl.legend()
        plot_cross(graph_x,graph_y,'--r')
        plot_cross(graph_xc,graph_y,'--b')
    elif(angle==2):
        reverse(graph_x,graph_y,color="red",label="A",crossColor='--r')
        reverse(graph_xc,graph_y,color="blue",label="Scalar A",crossColor='--b')

def inverse(graph_x,graph_y):
    j=len(graph_x)-1
    graph_xc=[float(format(1/graph_x[j-i],'.5f'))for i in range(len(graph_x))]
    graph_xc.sort()
    print("Inverse of A is",graph_xc,"\nAlpha cut value is ", graph_y)
    angle=int(input("Press 1 Graphicly Normal order fuzzy number\nPress 2 Graphicly Reverse order fuzzy number\n"))
    if(angle==1):
        plot_cross(graph_x,graph_y,'--r')
        plot_cross(graph_xc,graph_y,'--b')
        mpl.plot(graph_xc,graph_y,color="blue",label="Inverse A")
        mpl.plot(graph_x,graph_y,color="red",label="Graph A")
        mpl.legend()
    elif(angle==2):
        reverse(graph_x,graph_y,color="red",label="A",crossColor='--r')
        reverse(graph_xc,graph_y,color="blue",label="Inverse A",crossColor='--b')

def reverse(graph_x,graph_y,color,label,crossColor):
    initial_length=len(graph_y)
    if((initial_length % 2)==0):
        graph_y = graph_y[(round((len(graph_y))/2)):len(graph_y)]
        graph_y.extend(graph_y[::-1])
        plot_cross(graph_x,graph_y,crossColor)
        mpl.plot(graph_x,graph_y,color=color,label=label)
        mpl.legend()
    else:
        if(initial_length==3):
            graph_y = graph_y[1:len(graph_y)]
            graph_y.append(graph_y[0])
            mpl.plot(graph_x,graph_y,color=color,label=label)
            plot_cross(graph_x,graph_y,crossColor)
            mpl.legend()
        else:
            graph_y = graph_y[(round((len(graph_y)-1)/2)):len(graph_y)]
            graph_y.extend(graph_y[-2::-1])
            mpl.plot(graph_x,graph_y,color=color,label=label)
            plot_cross(graph_x,graph_y,crossColor)
            mpl.legend()

def get_val(operation):
    print("Enter the n-gonal fuzzy number, where n= 2,3,4...\n")
    n=int(input())
    if(n==1):
        print("invalid input\n")
        get_val() #1 is invalid input so it will promt to inter again
    else:
        print("press \n 1 GRAPHICAL REPRESENTATION OF n-TRIANGULAR SHAPE FUZZY NUMBER \n 2 GRAPHICAL REPRESENTATION OF n-TRAPEZOIDAL SHAPE FUZZY NUMBER \n")
        option=int(input())

    if(option==1):
        fuzzy_no=(2*n)-1 #formula
    elif(option==2):
        fuzzy_no=2*n

    if((operation>=1) and(operation<=6)):
        print("\n ENTER ",fuzzy_no,"PARAMETERS FOR GRAPH A")
        graph_xa=[float(input()) for i in range(0,fuzzy_no)] #Taking points from the user
        graph_ya,midpoint=basic_opp(option,graph_xa,n,fuzzy_no,"A")#Y axis value calculated and stoblue to the list

        print("\n ENTER ",fuzzy_no," PARAMETERS FOR GRAPH B")
        graph_xb=[float(input()) for i in range(0,fuzzy_no)] #Taking points from the user
        #Y axis value and midpoint calculation
        graph_yb,midpoint=basic_opp(option,graph_xb,n,fuzzy_no,"B")

    elif(operation>=7):
        print("\n ENTER ",fuzzy_no," PARAMETERS FOR GRAPH A")
        graph_xa=[float(input()) for i in range(0,fuzzy_no)] #Taking points from the user
        graph_ya,midpoint=basic_opp(option,graph_xa,n,fuzzy_no,"A")


    if(operation==1):
       Addition(graph_xa,graph_ya,graph_xb,graph_yb,fuzzy_no,n,option)
    if(operation==2):
       Subtraction(graph_xa,graph_ya,graph_xb,graph_yb,fuzzy_no,n,option)
    if(operation==3):
       Multiplication(graph_xa,graph_ya,graph_xb,graph_yb,fuzzy_no,n,option,midpoint)
    if(operation==4):
       Division(graph_xa,graph_ya,graph_xb,graph_yb,fuzzy_no,n,option)
    if(operation==5):
       minimum(graph_xa,graph_ya,graph_xb,graph_yb,fuzzy_no,n,option)
    if(operation==6):
       maximum(graph_xa,graph_ya,graph_xb,graph_yb,fuzzy_no,n,option)
    if(operation==7):
        scalar_mul(graph_xa,graph_ya)
    if(operation==8):
        inverse(graph_xa,graph_ya)

def basic_opp(option,graph_x,n,fuzzy_no,name):
    compare=graph_x[1]-graph_x[0]
    isSymmetric= True
    graph_y=[float(format(i/(n-1),'.5f')) for i in range (0,n)]

    if(option==1):#triangle
        graph_y=graph_y+graph_y[-2::-1]
        midpoint=(int((fuzzy_no)/2))
        print("The classic number of ",name," is [",graph_x[midpoint],"]")
        l_limit=[float(format(graph_x[i+1]-graph_x[i],'.5f'))for i in range(0,(int(fuzzy_no/2)))]
        u_limit=[float(format(graph_x[i+1]-graph_x[i],'.5f'))for i in range((int((fuzzy_no)/2)),fuzzy_no-1)]
        for i in range(0,fuzzy_no-1):
            if((graph_x[i+1]-graph_x[i])!=compare):
                isSymmetric= False
        if(isSymmetric):
            print("\n Here, the fuzzy number: ",name,": (",graph_x[(int((fuzzy_no)/2))]," : ",l_limit[::-1],": ",u_limit,")")
            print("\n That is fuzzy number",name,': ',graph_x)
            print("\n Also, fuzzy number",name,"is SYMMETRIC")
            print("\n Alpha cut value of graph ",name,"is :",graph_y)
        else:
            print("\n Here, the fuzzy number: ",name,": (",graph_x[(int((fuzzy_no)/2))]," : ",l_limit[::-1],": ",u_limit,")")
            print("That is fuzzy number",name,': ',graph_x)
            print("\n Also, fuzzy number ",name,"is NON-SYMMETRIC")
            print("\n Alpha cut value of graph ",name,"is :",graph_y)
        return(graph_y,midpoint)

    elif(option==2):#Trapisoid
        graph_y=graph_y+graph_y[-1::-1]
        l_limit=[float(format(graph_x[i+1]-graph_x[i],'.5f'))for i in range(0,(int(fuzzy_no/2))-1)]
        u_limit=[float(format(graph_x[i+1]-graph_x[i],'.5f'))for i in range((int((fuzzy_no)/2)),fuzzy_no-1)]
        midpoint=[(int((fuzzy_no/2)-1)),(int(fuzzy_no/2))]
        print("\n The classic number of",name,"is [",graph_x[midpoint[0]]," , ",graph_x[midpoint[1]],"]")
        for i in range(0,int(fuzzy_no/2)-2):
            if((graph_x[i+1]-graph_x[i])!=compare):
                isSymmetric=False
        for i in range((int(fuzzy_no/2)-1),fuzzy_no-1):
            if((graph_x[i+1]-graph_x[i])!=compare):
                isSymmetric=False;
        if(isSymmetric):
            print("\n Here, the fuzzy number: ",name, ": (",graph_x[(int(fuzzy_no/2)-1):(int(fuzzy_no/2)+1)]," : ",l_limit[::-1],": ",u_limit,")")
            print("\n That is fuzzy number",name,': ',graph_x)
            print("\n Also, fuzzy number",name,"is SYMMETRIC")
            print("\n Alpha cut value of graph ",name,"is :",graph_y)
        else:
            print("\n Here, the fuzzy number: ",name,": (",graph_x[(int(fuzzy_no/2)-1):(int(fuzzy_no/2)+1)]," : ",l_limit[::-1],": ",u_limit,")")
            print("\n That is fuzzy number",name,': ',graph_x)
            print("\n Also, fuzzy number ",name,"is NON-SYMMETRIC")
            print("\n Alpha cut value of graph ",name,"is :",graph_y)
        return(graph_y,midpoint)

print("GRAPHICAL REPRESENTATION OF NEW ARITHMETICS OPERATIONS OF")
print("FUZZY NUMBERS FOR TRAPEZOIDAL AND TRIANGULAR SHAPES")
print("Press \n 1 ADDITION  2 SUBTRACTION   3 MULTIPLICATION  4 DIVISION \n 5 MINIMUM  6 MAXIMUM   7 SCALAR MULTIPLICATION   8 INVERSE \n FUZZY NUMBERS\n")

operation=int(input())
get_val(operation)
mpl.title('Graphcal representation of  fuzzy numbers')
mpl.show()
