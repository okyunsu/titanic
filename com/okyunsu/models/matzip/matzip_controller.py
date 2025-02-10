from com.okyunsu.models.matzip.dataset import Dataset
from com.okyunsu.models.matzip.matzip_service import MatzipService

class MatzipController:
    dataset = Dataset()
    service = MatzipService()

    def modelling(self, matzip):
        print("🐮모델링")
        this = self.dataset
        this.matzip = self.service.new_model(matzip)
        print(this.matzip)
        print("🐺트레인")
        return this