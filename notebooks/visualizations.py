"""##Visualizations"""

import matplotlib.pyplot as plt

##Separate Numerical columns from Object columns.
num_cols = df.select_dtypes(include='number').columns
cat_cols = df.select_dtypes(include='object').columns

num_cols

cat_cols

df['department'].value_counts().plot(kind='bar')
plt.title("Department Count")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

df['level'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.ylabel("")
plt.title("levels")
plt.show()

cross = pd.crosstab(df['department'], df['level'])

cross.plot(kind='bar', stacked=True)

plt.title("Department vs Level Distribution")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

mgr_counts = df.groupby(['department', 'department manager']).size()
mgr_counts

mgr_counts.head(10).plot(kind='barh')

plt.title("Top Department Managers by Number of Employees")
plt.xlabel("Number of Employees")
plt.ylabel("Manager")
plt.show()

df.groupby(['department', 'department manager']).size()

!pip install plotly

import plotly.express as px
import plotly.graph_objects as go

fig = px.bar(
    df['department manager'].value_counts().reset_index(),
    x='department manager',
    y='count',
    title='Employees per Department'
)

fig.show()

missing = df.isnull().sum().reset_index()

missing.columns = ['column', 'missing_count']

fig = px.bar(
    missing,
    x='column',
    y='missing_count',
    title='Missing Values'
)

fig.show()
