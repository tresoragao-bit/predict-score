import pandas as pd

def load_matches(file_path="data/matches.csv"):
    """
    Charge le fichier CSV contenant les matchs.
    Retourne un DataFrame pandas.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("❌ Fichier introuvable :", file_path)
        return pd.DataFrame()

def get_team_matches(df, team_name):
    """
    Retourne les matchs récents d'une équipe.
    """
    return df[(df["team_home"] == team_name) | (df["team_away"] == team_name)]

def get_head_to_head(df, team1, team2):
    """
    Retourne les confrontations directes entre deux équipes.
    """
    return df[
        ((df["team_home"] == team1) & (df["team_away"] == team2))
        | ((df["team_home"] == team2) & (df["team_away"] == team1))
  ]
