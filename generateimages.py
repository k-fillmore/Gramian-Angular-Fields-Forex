import ray
import pandas as pd
import psutil
from utils import select_df
from ImageGenerator import GrammianImage

num_cpus = psutil.cpu_count(logical=False)
ray.init()

df = pd.read_csv('eurusd_hour.csv')
df.drop(labels=['BCh', 'AO', 'AH', 'AL', 'AC', 'ACh'], inplace=True, axis=1)
df.rename(columns={"BO": "open", "BH": "high", "BL": "low", "BC": "close"}, inplace=True)
print(df.head())
dfs = select_df(df, 10)

@ray.remote
def execute_image_generator(df):
    GrammianImage(df, 10, "./test/", "gasf", 20).generateGasf()

for df in dfs:
    execute_image_generator.remote(df)
ray.shutdown()
