from com.okyunsu.models.titanic.dataset import Dataset
import pandas as pd


"""
PassengerId  고객ID,
Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Gender,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
print(f'결정트리 활용한 검증 정확도 {None}')
print(f'랜덤포레스트 활용한 검증 정확도 {None}')
print(f'나이브베이즈 활용한 검증 정확도 {None}')
print(f'KNN 활용한 검증 정확도 {None}')
print(f'SVM 활용한 검증 정확도 {None}')
"""
 
class TitanicService: 

    dataset = Dataset()

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = "C:\\Users\\bitcamp\\Documents\\Titanic\\com\\okyunsu\\datas\\titanic\\"
        this.fname = fname
        return pd.read_csv(this.context + this.fname) 
        
    
    def preprocess(self, train_fname, test_fname)->object:
        print("-----------모델 전처리 시작-------------")
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Gender', 'Age',
                   'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        this = self.dataset
        this.train= self.new_model(train_fname)
        this.test = self.new_model(test_fname)
        this.id = this.test['PassengerId']
        # 'SibSp', 'Parch', 'Cabin', 'Tictet' 가 지워야 할 teature 이다..
        drop_features = ['SibSp', 'Parch', 'Cabin', 'Ticket']
        this = self.drop_feature(this, *drop_features)
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate_title(this)
        this = self.title_nominal(this, title_mapping)
        this = self.drop_feature(this, 'Name')
        this = self.gender_nominal(this)
        this = self.drop_feature(this, 'Gender')
        this = self.embarked_nominal(this)  
        self.df_info(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        this = self.drop_feature(this, "Fare")
        return this

    

    @staticmethod
    def create_labels(this) -> object: 
        return this.train["Survived"]

    @staticmethod
    def create_train(this)->object:
        return this.train.drop("Survived", axis = 1) 

    @staticmethod
    def drop_feature(this, *feature)-> object:
  
        [i.drop(j, axis = 1, inplace = True) for j in feature for i in [this.test, this.train]]
           
        return this    

    # @staticmethod
    # def null_check(this):
    #     for i in [this.train, this.test]:
    #         print("🐶🐮🐈",i.isnull().sum())
    #     [print(i.isnull().sum(), inplace = True) for i in [this.test, this.train]]
    #     return this
        
    # @staticmethod
    # def kwargs_sample(**kwargs) -> None:
    #     {print(''.join(f'키워드: {i} 값: {j}')) for i, j in  kwargs.items()}


    @staticmethod
    def pclass_ordinal(this):
        return this

    @staticmethod
    def gender_nominal(this):
        return this


    @staticmethod
    def embarked_nominal(this):
        this.train = this.train.fillna({"Embarked": "S"}) #사우스햄튼이 가장 많으니까
        this.test = this.test.fillna({"Embarked": "S"}) 
        this.train['Embarked'] = this.train['Embarked'].map({'S':1,'C':2,"Q":3})
        this.test['Embarked'] = this.test['Embarked'].map({'S':1,'C':2,"Q":3})

        return this 
    
    @staticmethod
    def remove_duplicate_title(this):
        return this

    @staticmethod
    def extract_title_from_name(this):
        
        for i in [this.train, this.test]:
            i['Titele']= i['Name'].str.extract('([A-Za-z]+)\.', expand=False)

        [i.__setitem__('Titele', i['Name'].str.extract('([A-Za-z]+)\.', expand=False))
        for i in [this.train, this.test]]

        return this




    @staticmethod
    def title_nominal(this):
        return this

    @staticmethod
    def df_info(this):
        return this

    @staticmethod
    def age_ratio(this):
        return this

    @staticmethod
    def fare_ratio(this):
        return this