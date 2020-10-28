"""
.. biblioteca:: Classification with a basic neural network
   :plataforma: Unix, Windows, MAC
   :sinopsis: Classification
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tqdm

from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

# sigmoid function
def sigmoid_function(inputs, weights):
    #input1 * weight1 + input2 * weight2 + input3*weight3....
    x = inputs.dot(weights) # retorna un valor

    f = 1./(1+np.exp(-x))
    return f


# rectifier linear unit (ReLU)
def ReLU_function(inputs, weights):
    #input1 * weight1 + input2 * weight2 + input3*weight3....
    x = inputs.dot(weights)

    if x>0:
        f = x
    else:
        f = 0
    return f


def fit(X,y, alpha=0.005, epochs=600, function='Sigmoid'):
    weights = np.zeros(len(X[0]))
    errors  = []
    data    = list(zip(X,y))

    for _ in tqdm.tqdm(range(0, epochs)):
        error = 0
        for inputs, target in data:
            if function == "Sigmoid":
                output = sigmoid_function(inputs, weights)
            else:
                output = ReLU_function(inputs, weights)

            if output >= 0.5 and target == 0:  #target = 1
                error +=1
            elif output < 0.5 and target ==1: # target =0
                error +=1

            #Wj = Wj + LR * Ij * Error
            # Learning Rate: alpha (tasa de aprendizaje)
            #Ij : instances
            # Error :

            #weights = weights +( alpha * (target - output) * (output) * (1-output) * inputs)
            weights += alpha * (target - output) * (output) * (1-output) * inputs
        errors.append(error)
    return weights, errors

data = pd.read_csv("titanic_train.csv")

#Sibsp numero de hermanos o esposos abordo
#Parch numero  de padres/ hijos que estan a bordo
data = data[['Pclass','Sex', 'Parch', 'SibSp', 'Survived']]
#print(data)

data['Sex'] = data['Sex'].apply(lambda x:0 if x == 'female' else 1)
#print(data.head())

X = data.iloc[:,0:-1].values
X = np.insert(X,0,1,axis=1) #constante para la red
y = data['Survived'].values


#X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)


# forma manual de dividir el conjunto
data = data.sample(frac=1.) #shuffle

test_length = int(0.3 *len(y))
train_length = len(y)-test_length

X_train, X_test = X[0:train_length], X[train_length:]
y_train, y_test = y[0:train_length], y[train_length:]


weights, errors = fit(X_train, y_train, alpha=0.005, epochs=600)
print(weights)


plt.plot(errors)
plt.xlabel('Epochs')
plt.ylabel('Errors')
plt.show()



pred_y = []
function = 'Sigmoid'

correctly, wrong =0, 0

#Positive es clase 1 y negative es clase 0
tp = 0 # true positives - los que son de la clase 1 y fueron predichos como clase 1
tn = 0 #true negatives - los que son de la clase 0 y fueron predichos como clase 0
fp = 0 #false positives - los que son de la clase 0 y fueron predichos como clase 1
fn = 0 # false negatives - los que son de la clase 1 y fueron predichos como clase 0


for inputs, target in zip(X_test, y_test):
    if function == "Sigmoid":
        output = sigmoid_function(inputs, weights)
    else:
        output = ReLU_function(inputs, weights)

    if output >= 0.5:
        pred_y.append(1)
    elif output< 0.5:
        pred_y.append(0)

        # fp = fp + 5
        #fp +=5

    if output >= 0.5 and target == 0 :
        fp += 1
    elif output < 0.5 and target == 1:
        fn += 1
    elif output >= 0.5 and target == 1 :
        tp +=1
    else:
        tn +=1

    correctly = tp + tn
    wrong = fp + fn

plt.pie([correctly, wrong],
        labels=['correctly ({})'.format(correctly), 'wrong ({})'.format(wrong)],
        colors=['green', 'red'])
plt.show()


# Precision: TP / (TP+FP)
#Porcentaje de predicciones positivas correctas
precision = tp/(tp+fp)

#Accuracy / exactitud
#Porcentaje de predicciones correctas
accuracy = (tp + tn)/(tp+tn+fp+fn)

#recall - sensitivity
#Porcentaje de instancias etiquetadas como positivas, que también fueron predichas como positivas
recall = tp/(tp+fn)

# Specificity
#Porcentaje de instancias etiquetadas como negativas, que también fueron predichas como negativas

specificity = tn / (tn+fp)


# f1
f1 = 2 *(precision*recall)/ (precision + recall)


print("Precision "+ str(precision))
print("Accuracy "+ str(accuracy))
print("Recall " + str(recall))
print("Specificity " + str(specificity))
print("F1 " + str(f1))


fpr, tpr, thresholds = roc_curve(y_test, pred_y)
auc_perceptron = roc_auc_score(y_test, pred_y)
print("auc " + str(auc_perceptron))


y_test0= [0 for _ in range(len(y_test))]
fpr0, tpr0, thresholds0 = roc_curve(y_test, y_test0)
plt.plot(fpr0, tpr0, linestyle='--', label='No Skill')
plt.plot(fpr, tpr, marker='.', label='ROC')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.show()
