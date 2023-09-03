from pandas import DataFrame
import pickle

def predict(pid, pclass, name, sex, age, sib, par, tict, fare, cabin, emb):
    num_attribs = ['Age', 'SibSp', 'Parch', 'Fare']
    cat_attribs = ['Pclass', 'Sex', 'Embarked']

    
    df = DataFrame([[pid, pclass, name, sex, age, sib, par, tict, fare, cabin, emb]])

    df.columns = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket','Fare', 'Cabin', 'Embarked']

    
    with open('mlModels/titanic_pipeline.pkl', 'rb') as file:
        pipeline = pickle.load(file)

    num_attribs = ['Age', 'SibSp', 'Parch', 'Fare']
    cat_attribs = ['Pclass', 'Sex', 'Embarked']

    data= pipeline.transform(df[num_attribs + cat_attribs])
    print(data)
    with open('mlModels/svm.pkl', 'rb') as file:
        model = pickle.load(file)


    output = model.predict(data)
    return output
    





    

# if __name__=='__main__':
#     pid = 1
#     pclass = 3
#     name = 'harshit rathore'
#     sex = 'male'
#     age = 33
#     sib = 1
#     par = 0
#     tict = 'A/5 21171'
#     fare = 7.2500
#     cabin = 'C123'
#     emb = 'S'
#     df = DataFrame([[pid, pclass, name, sex, age, sib, par, tict, fare, cabin, emb]])

    # ans = predict(pid, pclass, name, sex, age, sib, par, tict, fare, cabin, emb)
    # print(ans)




    # df.columns = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket','Fare', 'Cabin', 'Embarked']
    # with open('mlModels/titanic_pipeline.pkl', 'rb') as file:
    #     pipeline = pickle.load(file)
    # num_attribs = ['Age', 'SibSp', 'Parch', 'Fare']
    # cat_attribs = ['Pclass', 'Sex', 'Embarked']
    # data= pipeline.transform(df[num_attribs + cat_attribs])
    # with open('mlModels/svm.pkl', 'rb') as file:
    #     model = pickle.load(file)
    # print(data)
    # print(len(data[0]))
    # print(model.predict(data))
    