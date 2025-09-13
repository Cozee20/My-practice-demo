import pandas as pd
df = pd.read_csv('student_scores.csv')
df['Class_av'] = df.iloc[:,2:5].mean(axis=1)#class_av is the class average
score = df.iloc[:,2:5]
Subjects = score.idxmax(axis=1)
highest_score = score.max(axis=1)
df['Subject'] = Subjects
df['high score']= highest_score
print(df[['Student','Subject','high score']])
Mean_english = df.iloc[:,2].mean()
Mean_math = df.iloc[:,3].mean()
Mean_Science = df.iloc[:,4].mean()
print(Mean_english)
print(Mean_math)
print(Mean_Science)
top_boy =df.iloc[:,2].max()
Name = df.iloc[:,2].idxmax()
print(Name)
print(top_boy)
