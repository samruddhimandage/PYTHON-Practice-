import matplotlib.pyplot as plt

def main():
    
    X=[1,2,3,4,5]
    Y=[10,25,18,35,20]
    
    plt.plot(
        X,                             #possitional argument
        Y,                             #possitional argument
        
        marker ="o",                    #keyword arguments 
        linestyle ="--",
        linewidth=2,
        markersize =7,
        label="Marks"
    )
    
    plt.title("Line plot of Data")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")
    
    plt.grid(True)      # the squares on the background
    plt.legend()        
    plt.show()
    
if __name__=="__main__":
    main()