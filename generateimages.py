import pandas as pd
import ray

from ImageGenerator import GrammianImage
from utils import select_df

output_directory = "./test/"
csv_file = 'eurusd_hour.csv'
window_size = 10
quality_pct = 20

ray.init()
df = pd.read_csv(csv_file)
df.drop(labels=['BCh', 'AO', 'AH', 'AL', 'AC', 'ACh'], inplace=True, axis=1)
df.rename(columns={"BO": "open", "BH": "high", "BL": "low", "BC": "close"}, inplace=True)
dfs = select_df(df, window_size)

@ray.remote
def execute_image_generator(df):
    GrammianImage(df, window_size, output_directory, "gasf", quality_pct).generateGaf()

for df in dfs:
    execute_image_generator.remote(df)
ray.shutdown()
