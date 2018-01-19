import pandas as pd
import imports
from imports import descriptors, model

#dataSets=['../kaminski_unbalanced_600_50.csv','../all_balanced_100_predictable.csv','../kaminski_balanced_50.csv', '../all_multiplePerson.csv','../all_unbalanced_2600_1000.csv']
dataSets=['../kaminski_unbalanced_600_50.csv']
fieldToTest=['content','X-From','both']
descriptors_list=['tf_idf','frequence']

for dataSet in dataSets:
    #######################DATASET##################################################
    df = pd.read_csv(dataSet, na_values=['?'],header=0)
    for field in fieldToTest:
        if(field=='both'):
            df["features"] = df['content'].map(str)+df['X-From'].map(str)
        else:
            df["features"] = df[field].map(str)
        X=df['features']
        y=df['class']

        ########################DESCRIPTORS############################################
        for descriptor in descriptors_list:
            if(descriptor == "tf_idf"):
                res = descriptors.tf_idf(X)
            if(descriptor == "frequence"):
                res = descriptors.frequence(X)
            grid = model.decision_tree(res,y)

            #######################RESULTS##################################################
            print("The best model for: {} {} {}\n".format(dataSet,field,descriptor))
            print("- best score  : {}\n".format(grid.best_score_))
            print("- best params : {}\n".format(grid.best_params_))
            print("- best estimator : {}\n".format(grid.best_estimator_))