import matplotlib.pyplot as plt

def main():
    study_hours=[1,2,3,4,5,6]
    marks=[35,50,60,72,85,95]
    
    plt.scatter(
        study_hours,
        marks,
        s = 100,
        marker="o",
        alpha =0.7,
        edgecolors="pink",
        linewidths=1,
        label ="students"
    )
    
    plt.title("Scatter plot of Data")
    plt.xlabel("Study Hours")
    plt.ylabel("Obtained Marks")
    
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()