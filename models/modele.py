import pandas as pd
import os

def get_echantillon():
    # Chargement du DataFrame
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(current_dir, 'data', 'echantillon.csv')
    df = pd.read_csv(csv_path, sep=',')
    
    return df

def get_atomes():
    # Chargement du DataFrame
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(current_dir, 'data', 'atomes.csv')
    df = pd.read_csv(csv_path, sep=',')
    
    return df