import matplotlib.pyplot as plt

def main():
    
    language =["C","C++","JAVA","PYTHON"]
    Students =[30,40,35,55]
    
    plt.bar(
        language,
        Students,
        width=0.6,                    #width of bar
        edgecolor="black",              #boarder colour of bar
        linewidth=1,                  #width of bar boarder
        alpha=0.8,                    #transperace  0.0 to 1
        label="Students"              #legend text
    )
    
    plt.title("Bar plot of Data")
    plt.xlabel("language")
    plt.ylabel("no of students")
    
    plt.legend()
    plt.show()
if __name__=="__main__":
    main()