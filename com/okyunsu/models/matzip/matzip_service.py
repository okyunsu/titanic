from com.okyunsu.models.matzip.dataset import Dataset
import pandas as pd

class MatzipService:

    dataset = Dataset()

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = "C:\\Users\\bitcamp\\Documents\\Titanic\\com\\okyunsu\\datas\\matzip\\"
        this.fname = fname
        return pd.read_csv(this.context + this.fname)