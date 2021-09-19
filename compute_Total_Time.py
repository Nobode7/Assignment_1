#!/usr/bin/env python
# coding: utf-8

# In[21]:


def compute_Total_Hrs(Hours,Total_Hrs):
    Total_Hrs = Total_Hrs + float(Hours)
    return Total_Hrs

def compute_Avg_Hrs(Total_Hrs):
    Avg_Hrs = round(Total_Hrs/3,2)
    return Avg_Hrs

def get_Weekly_Hrs():
    Week = ["Week1","Week2","Week3","Week4"]
    Tasks = ["Task1","Task2","Task3"]
    Task_name = []
    Total_Time = []
    for i in Week:
        Total_Hrs_Spent_Per_Week = {}
        Total_Hrs = 0
        for ii in Tasks:
            Task_name = input("Enter 3 tasks that you have done in " + i + " , " + ii + ": ")
            Hours = int(input("Enter the total hours you spent on " + ii + " in " + i + " : "))
            Total_Hrs_Spent_Per_Week ["Week"] = i
            Total_Hrs_Spent_Per_Week [Task_name] = Hours
            Total_Hrs = compute_Total_Hrs(Hours,Total_Hrs)
            Avg_Hrs = compute_Avg_Hrs(Total_Hrs)
        print(Avg_Hrs)
        Total_Hrs_Spent_Per_Week ["Avg_Hrs"] = Avg_Hrs
        print(Total_Hrs_Spent_Per_Week)
        Total_Time.append(Total_Hrs_Spent_Per_Week)
    print(Total_Time)
    return Total_Time

