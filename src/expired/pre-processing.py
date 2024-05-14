
import pandas as pd
import numpy as np 

hosts_path = '/data/raw/olympic_hosts.csv'
medals_path = '/data/raw/olympic_medals.csv'
results_path = '/data/raw/olympic_results.csv'
athletes_path = '/data/raw/olympic_athletes.csv'

hosts = pd.read_csv(hosts_path)
medals = pd.read_csv(medals_path)
results = pd.read_csv(results_path)
athletes = pd.read_csv(athletes_path)


