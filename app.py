import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the data
data = pd.read_csv('data/HR_Analytics.csv')

# Define functions for each analysis
def attrition_analysis(data):
    # Add sliders for the analysis
    attrition_slider = st.slider('Attrition', min_value=0, max_value=1, step=1)
    age_slider = st.slider('Age', min_value=data['Age'].min(), max_value=data['Age'].max(), step=1)
    education_slider = st.slider('Education', min_value=data['Education'].min(), max_value=data['Education'].max(), step=1)

    # Plotting the visualizations
    st.subheader('Attrition Count')
    fig, ax = plt.subplots()
    sns.countplot(x='Attrition', data=data[data['Attrition'] == attrition_slider], palette='dark')
    plt.title('Attrition Count')
    st.pyplot(fig)

    st.subheader('Attrition by AgeGroup, BusinessTravel, and Department')
    fig, ax = plt.subplots()
    group = data.groupby(['AgeGroup','BusinessTravel','Department'])['Attrition'].count().reset_index()
    sns.barplot(x='AgeGroup', y='Attrition', hue='Department', data=group)
    plt.title('Attrition by AgeGroup, BusinessTravel, and Department')
    st.pyplot(fig)

    st.subheader('Attrition Distribution')
    fig, ax = plt.subplots()
    attrition_counts = data['Attrition'].value_counts(normalize=True) * 100
    sns.countplot(x='Attrition', data=data)
    plt.title('Attrition Distribution')
    for i in range(len(attrition_counts)):
        count = attrition_counts[i]
        plt.text(i, count, f'{count:.1f}%', ha='center', va='bottom')
    st.pyplot(fig)

    st.subheader('Age Distribution of Employees')
    fig, ax = plt.subplots()
    sns.histplot(data=data[data['Age'] == age_slider], x='Age')
    plt.title('Age Distribution of Employees')
    st.pyplot(fig)

    fig, axes = plt.subplots(3, 1, figsize=(8, 12))
    fig, ax = plt.subplots()
    sns.countplot(ax=axes, x='Education', data=data[data['Education'] == education_slider])
    axes.set_title('Education Distribution')
    sns.countplot(ax=axes, x='Gender', data=data)
    axes.set_title('Gender Distribution')
    sns.countplot(ax=axes, x='MaritalStatus', data=data)
    axes.set_title('Marital Status Distribution')
    fig.tight_layout()
    st.pyplot(fig)

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    sns.boxplot(ax=axes, y='DailyRate', data=data)
    axes.set_title('Distribution of Daily Rates')
    sns.boxplot(ax=axes, y='MonthlyIncome', data=data)
    axes.set_title('Distribution of Monthly Income')
    plt.tight_layout()
    st.pyplot(fig)

    avg_daily_rates = data.groupby('Department')['DailyRate'].mean().reset_index()
    fig, ax = plt.subplots()
    sns.barplot(x='Department', y='DailyRate', data=avg_daily_rates)
    plt.title('Average Daily Rates by Department')
    plt.xlabel('Department')
    plt.ylabel('Average Daily Rate')
    st.pyplot(fig)

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    sns.scatterplot(ax=axes, x='DistanceFromHome', y='DailyRate', data=data)
    axes.set_title('Distance from Home vs Daily Rate')
    sns.scatterplot(ax=axes, x='DistanceFromHome', y='MonthlyIncome', data=data)
    axes.set_title('Distance from Home vs Monthly Income')
    plt.tight_layout()
    st.pyplot(fig)

def demographics_analysis(data):
    st.subheader('Employee Demographics Analysis')
    # Add code for the visualizations

def salary_analysis(data):
    st.subheader('Salary and Compensation Analysis')
    # Add code for the visualizations

def job_satisfaction_analysis(data):
    st.subheader('Job Satisfaction and Work-Life Balance Analysis')
    # Add code for the visualizations

def tenure_analysis(data):
    st.subheader('Employee Tenure Analysis')
    # Add code for the visualizations

def performance_analysis(data):
    st.subheader('Employee Performance and Training Analysis')
    # Add code for the visualizations

def stock_option_analysis(data):
    st.subheader('Stock Option Analysis')
    # Add code for the visualizations

def relationship_satisfaction_analysis(data):
    st.subheader('Relationship Satisfaction Analysis')
    # Add code for the visualizations

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
