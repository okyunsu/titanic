from com.okyunsu.models.titanic.dataset import Dataset
from com.okyunsu.models.titanic.titanic_service import TitanicService
from icecream import ic

class TitanicController:
    dataset = Dataset() 
    service = TitanicService()

    def modeling(self, train, test):
        this = self.service.preprocess(train, test)
        self.print_this(this)
        
        #print("🐶🐶트레인: 머신에게 내는 문제")
        #this.train = self.service.create_train(this)
        #ic(train)
        #this.label = self.service.create_labels(this)
        #print("😽🤑labels: 머신이 맞춰야 하는 답")
        #ic(labels)
        return this

    def learning(self):
        pass

    def submit(self):
        pass


    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(f'1. Train 의 type \n {type(this.train)} ')
        print(f'2. Train 의 column \n {this.train.columns} ')
        print(f'3. Train 의 상위 1개 행\n {this.train.head()} ')
        print(f'4. Train 의 null 의 갯수\n {this.train.isnull().sum()}개')
        print(f'5. Test 의 type \n {type(this.test)}')
        print(f'6. Test 의 column \n {this.test.columns}')
        print(f'7. Test 의 상위 1개 행\n {this.test.head()}개')
        print(f'8. Test 의 null 의 갯수\n {this.test.isnull().sum()}개')
        print('*' * 100)
    
