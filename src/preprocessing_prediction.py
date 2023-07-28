def preprocess_predict_newdata(new_array):
    # first transformation for the pipeline which is SimpleImputer
    trans_1 = ColumnTransformer([('simple_imputer',SimpleImputer(strategy='most_frequent'),[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12])], remainder='passthrough' )
    
    # second transformation for the pipeline which is OneHotEncoder
    trans_2 = ColumnTransformer([('ohe_trans',OneHotEncoder(sparse_output=False,handle_unknown='ignore'), [0,1,4,12])], remainder='passthrough' )

    # third transformation for the pipeline which is scaling
    trans_3 = ColumnTransformer([('scale', StandardScaler(), slice(0, 12))], remainder='passthrough')

    # fourth transformation for the pipeline which is creating an instance from linear models
    trans_4 = RandomForestClassifier()

    # creating a pipeline with above transformers
    pipe = Pipeline([('trans_1',trans_1),
                    ('trans_2',trans_2),
                    ('trans_3',trans_3),
                    ('trans_4',trans_4)])
    
    y_predict = pipe.predict(new_array)

    return y_predict
    
    


