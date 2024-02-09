"""
Calculates summary statistics, stratifying them by diagnosis

Written by sirismcgee 2024-02-09

"""
import pandas as pd
from tableone import TableOne

filename = 'BreastCancerData.csv'
df = pd.read_csv(filename)
columns = ["diagnosis","radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]
categorical=['diagnosis']
groupby='diagnosis'
mytable=TableOne(df, columns,categorical, groupby, pval=True)
print(mytable.tabulate(tablefmt='github'))

