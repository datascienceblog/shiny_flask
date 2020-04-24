# imports
from pandas import read_csv
import plotly.express as px
import numpy as np

# read data from disk
# Rscript -e "readr::write_csv(faithful, 'data/faithful.csv')"
faithful = read_csv('./data/faithful.csv')
def hist(bins = 30):
  # calculate the bins
  x = faithful['waiting']
  counts, bins = np.histogram(x, bins=np.linspace(np.min(x), np.max(x), bins+1))
  bins = 0.5* (bins[:-1] + bins[1:])
  p = px.bar(
    x=bins, y=counts,
    title='Histogram of waiting times',
    labels={
      'x': 'Waiting time to next eruption (in mins)',
      'y': 'Frequency'
    },
    template='simple_white'
  )
  return p

plot = hist()
plot.show()
