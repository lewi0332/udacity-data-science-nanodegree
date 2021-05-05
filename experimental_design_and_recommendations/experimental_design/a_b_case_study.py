import pandas as pd
import numpy as np

df = pd.read_csv('homepage-experiment-data.csv')

df[['Control Cookies', 'Experiment Cookies']].sum()

u_pop = df['Control Cookies'].mean()
u_samp = df['Experiment Cookies'].mean()
std_samp = df['Experiment Cookies'].std()
n = len(df['Experiment Cookies'])

(u_pop - u_samp) / np.sqrt( (u_samp * (1-u_samp)) / n)