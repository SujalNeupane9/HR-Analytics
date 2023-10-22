
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the data
data = pd.read_csv('data/HR_Analytics.csv')

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
sns.countplot(ax=axes[0], x='Education', data=data[data['Education'] == education_slider])
axes[0].set_title('Education Distribution')

sns.countplot(ax=axes[1], x='Gender', data=data)
axes[1].set_title('Gender Distribution')

sns.countplot(ax=axes[2], x='MaritalStatus', data=data)
axes[2].set_title('Marital Status Distribution')
fig.tight_layout()
st.pyplot(fig)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

sns.boxplot(ax=axes[0], y='DailyRate', data=data)
axes[0].set_title('Distribution of Daily Rates')

sns.boxplot(ax=axes[1], y='MonthlyIncome', data=data)
axes[1].set_title('Distribution of Monthly Income')
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

sns.scatterplot(ax=axes[0], x='DistanceFromHome', y='DailyRate', data=data)
axes[0].set_title('Distance from Home vs Daily Rate')

sns.scatterplot(ax=axes[1], x='DistanceFromHome', y='MonthlyIncome', data=data)
axes[1].set_title('Distance from Home vs Monthly Income')
plt.tight_layout()
st.pyplot(fig)

fig, ax = plt.subplots()
sns.countplot(x='JobSatisfaction', data=data)
plt.title('Job Satisfaction Levels')
plt.xlabel('Job Satisfaction')
plt.ylabel('Count')
st.pyplot(fig)

worklife_counts = data['WorkLifeBalance'].value_counts()

fig, ax = plt.subplots()
plt.pie(worklife_counts, labels=worklife_counts.index, autopct='%1.1f%%')
plt.title('Work-Life Balance Ratings')
st.pyplot(fig)

fig, ax = plt.subplots()
sns.countplot(x='JobSatisfaction', hue='WorkLifeBalance', data=data)
plt.title('Attrition by Job Satisfaction and Work-Life Balance')
plt.xlabel('Job Satisfaction')
plt.ylabel('Count')
plt.legend(title='Work-Life Balance')
st.pyplot(fig)

fig, ax = plt.subplots()
sns.histplot(data=data, x='YearsAtCompany')
plt.title('Years at Company Distribution')
plt.xlabel('Years at Company')
plt.ylabel('Count')
st.pyplot(fig)

fig, ax = plt.subplots()
sns.scatterplot(x='YearsAtCompany', y='Attrition', data=data)
plt.title('Attrition vs Years at Company')
plt.xlabel('Years at Company')
plt.ylabel('Attrition')
st.pyplot(fig)

fig, ax = plt.subplots()
sns.countplot(x='Department', hue='Attrition', data=data)
plt.title('Attrition by Job Role')
plt.xlabel('Job Role')
plt.ylabel('Count')
plt.legend(title='Attrition')
st.pyplot(fig)

fig, ax = plt.subplots()
sns.countplot(x='PerformanceRating', data=data)
plt.title('Performance Ratings')
plt.xlabel('Performance Rating')
plt.ylabel('Count')
st.pyplot(fig)

fig, ax = plt.subplots()
sns.boxplot(data=data, y='TrainingTimesLastYear')
plt.title('Training Times Last Year Distribution')
plt.ylabel('Training Times Last Year')
st.pyplot(fig)

fig, ax = plt.subplots()
sns.catplot(x='TrainingTimesLastYear', y='Attrition', hue='PerformanceRating', kind='bar', data=data)
plt.title('Impact of Training on Performance and Attrition')
plt.xlabel('Training Times Last Year')
plt.ylabel('Attrition')
plt.tight_layout()
st.pyplot(fig)

fig, ax = plt.subplots()
sns.countplot(x='StockOptionLevel', data=data)
plt.title('Stock Option Levels')
plt.xlabel('Stock Option Level')
plt.ylabel('Count')
st.pyplot(fig)

fig, ax = plt.subplots()
sns.countplot(x='StockOptionLevel', hue='Attrition', data=data)
plt.title('Attrition by Stock Option Level')
plt.xlabel('Stock Option Level')
plt.ylabel('Count')
plt.legend(title='Attrition')
st.pyplot(fig)

fig, ax = plt.subplots()
sns.countplot(x='RelationshipSatisfaction', data=data)
plt.title('Relationship Satisfaction Levels')
plt.xlabel('Relationship Satisfaction')
plt.ylabel('Count')
st.pyplot(fig)

fig, ax = plt.subplots()
sns.countplot(x='RelationshipSatisfaction', hue='Attrition', data=data)
plt.title('Attrition by Relationship Satisfaction')
plt.xlabel('Relationship Satisfaction')
plt.ylabel('Count')
plt.legend(title='Attrition')
st.pyplot(fig)
