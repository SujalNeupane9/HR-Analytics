import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the data
data = pd.read_csv('data/HR_Analytics.csv')

# Define functions for each analysis
def attrition_analysis(data):
    fig, ax = plt.subplots()
    sns.countplot(x='Attrition', data=data,palette='dark')
    plt.title('Attrition Count')
    plt.show()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    group = data.groupby(['AgeGroup','BusinessTravel','Department'])['Attrition'].count().reset_index()
    sns.barplot(x='AgeGroup', y='Attrition', hue='Department', data=group)
    plt.title('Attrition by AgeGroup, BusinessTravel, and Department')
    plt.show()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    attrition_counts = data['Attrition'].value_counts(normalize=True) * 100
    sns.countplot(x='Attrition', data=data)
    plt.title('Attrition Distribution')
    for i in range(len(attrition_counts)):
        count = attrition_counts[i]
        plt.text(i, count, f'{count:.1f}%', ha='center', va='bottom')
    plt.show()
    st.pyplot(fig)

def demographics_analysis(data):
    st.subheader('Employee Demographics Analysis')
    fig, ax = plt.subplots()
    sns.histplot(data=data,x='Age')
    plt.title('Age Distribution of Employees')
    plt.show()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    fig, axes = plt.subplots(3, 1, figsize=(8, 12))
    sns.countplot(ax=axes[0], x='Education', data=data)
    axes[0].set_title('Education Distribution')
    
    sns.countplot(ax=axes[1], x='Gender', data=data)
    axes[1].set_title('Gender Distribution')
    
    sns.countplot(ax=axes[2], x='MaritalStatus', data=data)
    axes[2].set_title('Marital Status Distribution')
    fig.tight_layout()
    plt.show()
    st.pyplot(fig)
    

def salary_analysis(data):
    st.subheader('Salary and Compensation Analysis')
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    sns.boxplot(ax=axes[0], y='DailyRate', data=data)
    axes[0].set_title('Distribution of Daily Rates')
    
    sns.boxplot(ax=axes[1], y='MonthlyIncome', data=data)
    axes[1].set_title('Distribution of Monthly Income')
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    avg_daily_rates = data.groupby('Department')['DailyRate'].mean().reset_index()

    sns.barplot(x='Department', y='DailyRate', data=avg_daily_rates)
    plt.title('Average Daily Rates by Department')
    plt.xlabel('Department')
    plt.ylabel('Average Daily Rate')
    plt.show()
    st.pyplot(fig)

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    sns.scatterplot(ax=axes[0], x='DistanceFromHome', y='DailyRate', data=data)
    axes[0].set_title('Distance from Home vs Daily Rate')
    
    sns.scatterplot(ax=axes[1], x='DistanceFromHome', y='MonthlyIncome', data=data)
    axes[1].set_title('Distance from Home vs Monthly Income')
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)

def job_satisfaction_analysis(data):
    st.subheader('Job Satisfaction and Work-Life Balance Analysis')
    fig, ax = plt.subplots()
    sns.countplot(x='JobSatisfaction', data=data)

    plt.title('Job Satisfaction Levels')
    plt.xlabel('Job Satisfaction')
    plt.ylabel('Count')
    
    plt.show()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    worklife_counts = data['WorkLifeBalance'].value_counts()

    plt.pie(worklife_counts, labels=worklife_counts.index, autopct='%1.1f%%')
    plt.title('Work-Life Balance Ratings')
    plt.show()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.countplot(x='JobSatisfaction', hue='WorkLifeBalance', data=data)
    plt.title('Attrition by Job Satisfaction and Work-Life Balance')
    plt.xlabel('Job Satisfaction')
    plt.ylabel('Count')
    plt.legend(title='Work-Life Balance')
    plt.show()
    st.pyplot(fig)

def tenure_analysis(data):
    st.subheader('Employee Tenure Analysis')
    fig, ax = plt.subplots()
    sns.histplot(data=data, x='YearsAtCompany')
    plt.title('Years at Company Distribution')
    plt.xlabel('Years at Company')
    plt.ylabel('Count')
    plt.show()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.scatterplot(x='YearsAtCompany', y='Attrition', data=data)
    plt.title('Attrition vs Years at Company')
    plt.xlabel('Years at Company')
    plt.ylabel('Attrition')
    plt.show()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.countplot(x='Department', hue='Attrition', data=data)
    plt.title('Attrition by Job Role')
    plt.xlabel('Job Role')
    plt.ylabel('Count')
    plt.legend(title='Attrition')
    plt.show()
    st.pyplot(fig)

def performance_analysis(data):
    st.subheader('Employee Performance and Training Analysis')
    fig, ax = plt.subplots()
    sns.countplot(x='PerformanceRating', data=data)
    plt.title('Performance Ratings')
    plt.xlabel('Performance Rating')
    plt.ylabel('Count')
    plt.show()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.boxplot(data=data, y='TrainingTimesLastYear')
    plt.title('Training Times Last Year Distribution')
    plt.ylabel('Training Times Last Year')
    plt.show()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.catplot(x='TrainingTimesLastYear', y='Attrition', hue='PerformanceRating', kind='bar', data=data)
    plt.title('Impact of Training on Performance and Attrition')
    plt.xlabel('Training Times Last Year')
    plt.ylabel('Attrition')
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)

def stock_option_analysis(data):
    st.subheader('Stock Option Analysis')
    fig, ax = plt.subplots()
    sns.countplot(x='StockOptionLevel', data=data)
    plt.title('Stock Option Levels')
    plt.xlabel('Stock Option Level')
    plt.ylabel('Count')
    plt.show()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.countplot(x='StockOptionLevel', hue='Attrition', data=data)
    plt.title('Attrition by Stock Option Level')
    plt.xlabel('Stock Option Level')
    plt.ylabel('Count')
    plt.legend(title='Attrition')
    plt.show()
    st.pyplot(fig)

def relationship_satisfaction_analysis(data):
    st.subheader('Relationship Satisfaction Analysis')
    fig, ax = plt.subplots()
    sns.countplot(x='RelationshipSatisfaction', data=data)
    plt.title('Relationship Satisfaction Levels')
    plt.xlabel('Relationship Satisfaction')
    plt.ylabel('Count')
    plt.show()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.countplot(x='RelationshipSatisfaction', hue='Attrition', data=data)
    plt.title('Attrition by Relationship Satisfaction')
    plt.xlabel('Relationship Satisfaction')
    plt.ylabel('Count')
    plt.legend(title='Attrition')
    plt.show()
    st.pyplot(fig)
    
# Set page title and layout
st.set_page_config(page_title='HR Analytics Dashboard', layout='wide')

# Create sidebar with buttons for each analysis
analysis = st.sidebar.radio('Select an analysis', ('Attrition Analysis', 'Employee Demographics Analysis', 'Salary and Compensation Analysis', 'Job Satisfaction and Work-Life Balance Analysis', 'Employee Tenure Analysis', 'Employee Performance and Training Analysis', 'Stock Option Analysis', 'Relationship Satisfaction Analysis'))

# Call the corresponding function based on the user's selection
if analysis == 'Attrition Analysis':
    attrition_analysis(data)
elif analysis == 'Employee Demographics Analysis':
    demographics_analysis(data)
elif analysis == 'Salary and Compensation Analysis':
    salary_analysis(data)
elif analysis == 'Job Satisfaction and Work-Life Balance Analysis':
    job_satisfaction_analysis(data)
elif analysis == 'Employee Tenure Analysis':
    tenure_analysis(data)
elif analysis == 'Employee Performance and Training Analysis':
    performance_analysis(data)
elif analysis == 'Stock Option Analysis':
    stock_option_analysis(data)
elif analysis == 'Relationship Satisfaction Analysis':
    relationship_satisfaction_analysis(data)
