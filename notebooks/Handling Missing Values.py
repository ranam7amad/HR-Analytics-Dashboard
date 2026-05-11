# Handling Missing Values

"""**Handling Strategy**

| Column | Action Taken | Reason |
|--------|--------------|--------|
| Unit Manager | Filled with "No Manager" | Missing values are acceptable for direct reporting employees |
| Top Level  | Left as it is   |  Missing values are logically expected |
| Email | Investigated manually | Email is considered critical employee information |
"""
missing_cols = df.isnull().sum()
missing_cols = missing_cols[missing_cols > 0]

#Getting The sum of missingn values in columns and sorting them.

missing_cols.sort_values(ascending=False)

df[df['unit manager'].isnull()]

df[df['top level'].isnull()]

(df.isnull().sum() / len(df)) * 100

df = df.drop(columns=['unit manager'])

df.columns

"""Missing values in the 'top level' column were replaced with "no manager" to represent employees without top level management."""

df['top level'] = df['top level'].fillna('no manager')

df['top level']

df['email'] = df['email'].str.lower()

df['email'] = df['email'].fillna('no email')

df['email']
