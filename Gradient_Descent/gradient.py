import numpy as np 


def gradient_descent(x,y):
    m_curr=b_curr=0
    iterations=10 #can be modified until cost is reduced.
    n=len(x) #Assuming length of x and y datapoints are the same
    learning_rate=0.00001 #can be modified until the cost is reduced 
    
    for i in range (iterations):
        y_predicted=m_curr*x + b_curr
        cost=(1/n)*sum([val**2 for val in (y-y_predicted)])
        md=-(2/n)*sum(x*(y-y_predicted))
        bd=-(2/n)*sum(y-y_predicted)
        m_curr=m_curr-learning_rate*md
        b_curr=b_curr-learning_rate*bd 
        print("m{}, b{}, iteration{}, cost{}".format(m_curr, b_curr, cost, i))
        
x=np.array([1,2,3,4,5])
y=np.array([15,7,9,11,13])

gradient_descent(x,y)