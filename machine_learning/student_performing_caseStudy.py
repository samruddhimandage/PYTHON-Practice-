import pandas as pd
def student_data(Datapath):
    
    df =  pd.read_csv(Datapath)
    
    print("first 5 rows of the data frame")
    print(df.head())
    
    print("last 5 rows of the data frame")
    print(df.tail())
    
    print("shape of the data frame")
    print(df.shape)
    
    print("columns in the data frame")
    print(df.columns.tolist())
    
    print("data types of the columns in the data frame")
    print(df.dtypes)
     
    print("number of rows in the data frame ie number of students") 
    total_students=len(df)
    print(len(df))
    
    passed_students = (df["FinalResult"] == 1).sum()
    print("Number of passed students:", passed_students)
    
    failed_students = (df["FinalResult"]==0).sum()
    print("Number of failed students :",failed_students)

    avg_hr = (df["StudyHours"]).mean()
    avg_attendence = (df["Attendance"]).mean()
    max_previousScore = (df["PreviousScore"]).max()
    avg_SleepHr = (df["SleepHours"]).min()
    
    print("average study hours :",avg_hr)
    print("average attendence :",avg_attendence)
    print("Max PreviousScore :",max_previousScore)
    print("Min SleepHours :",avg_SleepHr)
    
    print("Distribution of final result :")
    result_count=(df["FinalResult"]).value_counts()
    print(result_count)
    
    percentage_count = (df["FinalResult"]).value_counts(normalize=True)*100
    print("percentage_count is ",percentage_count)
    
    pass_percentage = (passed_students/total_students)*100
    failed_percentage=(failed_students/total_students)*100
    
    print("Percentage of passed students:",pass_percentage)
    print("percentage of failed students:",failed_percentage)
    
    if abs(pass_percentage-failed_percentage) <= 10:
        print("Sheet is approx Balanced")
    else:
        print("Sheet is Not Balanced")
        
    
def main():
    student_data("student_performance_ml.csv")
    
if __name__=="__main__":
    main()