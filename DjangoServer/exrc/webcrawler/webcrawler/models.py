

import pandas as pd

from isort._future._dataclasses import dataclass


context = 'C:/Users/SJMoon/AIA/MSAProject/DjangoServer/webcrawler/'


@dataclass
class Scrap:
    html = ""
    parser = ""
    domain = ""
    query_string = ""
    headers = {}
    tag_name = ""
    fname = ""
    class_names = []
    artists = []
    titles = []
    diction = {}
    df = None

    def dict_to_dataframe(self):
        print(len(self.diction))
        self.df = pd.DataFrame.from_dict(self.diction, orient='index')

    def dataframe_to_scv(self):
        path = 'save/result_bugsmusic.csv'
        self.df.to_csv(f"C:\\Users\\SJMoon\\AIA\\MSAProject\\DjangoServer\\exrc\\webcrawler\\save")