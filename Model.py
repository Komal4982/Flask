# # Import dependencies
# import pandas as pd
# import numpy as np
# import warnings
# warnings.filterwarnings("default", category=DeprecationWarning)
#
# # Load the dataset in a dataframe object and include only four features as mentioned
# url = "Dataset/titanic.csv"
# df = pd.read_csv(url)
# include = ['Age', 'Sex', 'Embarked', 'Survived'] # Only four features
# df_ = df[include]
#
# # Data Preprocessing
# categoricals = []
# for col, col_type in df_.dtypes.iteritems():
#      if col_type == 'O':
#           categoricals.append(col)
#      else:
#           df_[col].fillna(0, inplace=True)
#
# df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)
#
# # Logistic Regression classifier
# from sklearn.linear_model import LogisticRegression
# dependent_variable = 'Survived'
# x = df_ohe[df_ohe.columns.difference([dependent_variable])]
# y = df_ohe[dependent_variable]
# lr = LogisticRegression()
# lr.fit(x, y)
#
# # Save your model
# from sklearn.externals import joblib
# joblib.dump(lr, 'model.pkl')
# print("Model dumped!")
#
# # Load the model that you just saved
# lr = joblib.load('model.pkl')
#
# # Saving the data columns from training
# model_columns = list(x.columns)
# joblib.dump(model_columns, 'model_columns.pkl')
# print("Models columns dumped!")




# Import dependencies
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("default", category=DeprecationWarning)

df = pd.read_csv("Dataset/titanic.csv")
df.head()

include = ['Age', 'Sex', 'Embarked', 'Survived'] # Only four features
df= df[include]


df.replace(np.NaN,df.mean(),inplace=True)

df=pd.get_dummies(df,columns=["Sex","Embarked"])

from sklearn.model_selection import train_test_split
train,test=train_test_split(df,test_size=0.2,random_state=0)

x_train=train.iloc[:,0:3]
y_train=train.iloc[:,3]

x_test=test.iloc[:,0:3]
y_test=test.iloc[:,3]

# Logistic Regression classifier
from sklearn.linear_model import LogisticRegression
# dependent_variable = 'Survived'
# x = df_ohe[df_ohe.columns.difference([dependent_variable])]
# y = df_ohe[dependent_variable]
# lr = LogisticRegression()
# lr.fit(x_train, y_train)
from sklearn.ensemble import RandomForestClassifier
lr=RandomForestClassifier(n_estimators=20)
lr.fit(x_train, y_train)
pred=lr.predict(x_test)


from sklearn.metrics import accuracy_score
acc=accuracy_score(pred,y_test)*100
print(acc)

import pickle
fileobject=open("model.pkl","wb")
pickle.dump(lr,fileobject)
fileobject.close()
print("Model dumped!")


# Load the model that you just saved
fileobject=open("model.pkl","rb")
lr = pickle.load(fileobject)

# Saving the data columns from training
model_columns = list(x_train.columns)
fileobject=open("model_columns.pkl","wb")
pickle.dump(model_columns,fileobject)
print("Models columns dumped!")