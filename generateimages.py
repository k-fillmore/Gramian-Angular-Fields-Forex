import ray
import pandas as pd
import psutil

num_cpus = psutil.cpu_count(logical=False)
ray.init(num_cpus)



