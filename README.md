# HR-Analytics-Dashboard
Project Overview
This project is an end-to-end HR Data Analytics Dashboard built using Python. It performs data cleaning, exploratory data analysis (EDA), and interactive visualizations to extract meaningful insights about employees, departments, and organizational structure.
The goal is to transform raw HR data into actionable insights that support better decision-making in workforce management.
________________________________________
 ##Features
##Data Cleaning
•	Standardized column names (lowercase & trimmed)
•	Handled missing values
•	Removed duplicate employee records
•	Converted date columns to proper datetime format
•	Normalized text columns (departments, levels, job titles, etc.)
Exploratory Data Analysis (EDA)
•	Department-wise employee distribution
•	Level distribution (Junior, Mid, Senior)
•	Managerial hierarchy analysis
•	Missing values analysis
•	Employee hiring trends over time
 ##Visualizations
Built using Matplotlib & Plotly:
•	Bar charts (Departments, Managers)
•	Pie charts (Level distribution)
•	Stacked bar charts (Department vs Level)
•	Line charts (Hiring trends)
•	Missing values analysis charts
 ##Key KPIs
•	Total number of employees
•	Number of departments
•	Number of managers
•	Missing email records
________________________________________
Dataset
The dataset contains HR-related employee information such as:
•	Employee ID
•	Full Name
•	Department
•	Job Title
•	Level
•	Manager hierarchy
•	Start Date
•	Email
________________________________________
 ##Technologies Used
•	Python 
•	Pandas 
•	Matplotlib 
•	Plotly 
•	Google Colab 
________________________________________
##Key Insights
•	Departments vary significantly in employee distribution
•	Certain departments have higher managerial concentration
•	Missing values exist mainly in hierarchy-related fields
•	Hiring trends show variation across years
________________________________________

##How to Run the Project
1.	Open Google Colab or Jupyter Notebook
2.	Upload the dataset:
from google.colab import files
uploaded = files.upload()
3.	Install required libraries:
pip install pandas matplotlib plotly
4.	Run the notebook step by step
________________________________________
##Output Export
Final cleaned dataset can be exported using:
df.to_csv('final_hr_data.csv', index=False)
________________________________________
##Author
Rana Mohamed
________________________________________

 If you like this project
Give it a ⭐ on GitHub and feel free to contribute or improve it

