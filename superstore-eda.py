## Import Libraries 
import numpy as np                            ## adds powerful data structures to python to perform mathematical operations on arrays.
import pandas as pd                           ## library perform general eda.
import seaborn as sns                         ## data visualization library based on matplotlib to provide statistical graphs. 
from matplotlib import pyplot as plt          ## creates quality static, animated, and visualizations in python.
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")             ## controls whether warnigns are ignored, displayed, or turned into errors.

## Load the dataset
df = pd.read_csv("/Users/kevineddy/Desktop/Data Projects/Superstore-timeseries/train.csv")
df.head()