import matplotlib.pyplot as plt

def main():
    
    marks=[45,55,60,62,65,67,70,72,75,78,80,82,85,90,92]
    
    plt.hist(
        marks,                           #countinuous data 
        bins=5,                          #num of grps
        edgecolor="black",               #boarder colour
        alpha=0.8,                       #transperancy
        rwidth=0.9                       #relative width of bars
    )
    
    plt.title("Histogram plot of Data")          
    plt.xlabel("marks")
    plt.ylabel("frequency")
    
    plt.show()

if __name__=="__main__":
    main()