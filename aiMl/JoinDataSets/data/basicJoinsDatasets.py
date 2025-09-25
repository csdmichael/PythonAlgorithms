import pandas as pd
site = pd.read_csv('aiML/JoinDatasets/data/site.csv')
print(site.head(2))
print(site.info())

visited = pd.read_csv('aiML/JoinDatasets/data/visited.csv')
print(visited.head(2))
print(visited.info())

person = pd.read_csv('aiML/JoinDatasets/data/person.csv')
print(person.head(2))
print(person.info())

survey = pd.read_csv('aiML/JoinDatasets/data/survey.csv')
print(survey.head(2))
print(survey.info())

site_visits_df = pd.merge(left=site, right=visited, left_on="name", right_on="site", how="inner")


# Answer check
print(type(site_visits_df), site_visits_df.shape)
print(site_visits_df.head())

visited_renamed = visited.rename(columns={"site": "name"})
site_visits_df = pd.merge(left=site, right=visited_renamed, on="name", how="inner")
print(type(site_visits_df), site_visits_df.shape)

