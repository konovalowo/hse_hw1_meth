import pandas as pd
import matplotlib.pyplot as plt

def plot_meth_hist(bg, name):
  cols = ['chr', 'start', 'end', 'value']
  df = pd.read_csv(bg, sep='	', names=cols)[1:]
  df['value'] = df['value'].round()
  gb = df.groupby('value').count()['chr']
  x = list(gb.keys())
  y = list(gb)

  plt.title(name)
  plt.bar(x, y)