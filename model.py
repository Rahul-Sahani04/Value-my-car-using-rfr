import numpy
import pandas
from  sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def predic(final_features):
    df = pandas.read_csv("mappedData.csv")
    df = df.dropna()
    df = df.drop(["engine_fuel"],axis=1)
    drop_list = ['УАЗ','Opel', 'Москвич', 'Dacia','Lancia','SsangYong', 'Daewoo','Geely', 'ВАЗ', 'Lifan', 'ЗАЗ','ГАЗ', 'Great Wall', 'Buick', 'Pontiac','Iveco',  'Saab', 'Infiniti', 'Chery', 'Peugeot']
    for i in range(len(drop_list)):
        df.drop(df.index[df["manufacturer_name"] == drop_list[i]],inplace=True)
    outlairs = ["year_produced" , "odometer_value", "engine_capacity" , "price_usd"] 
    for i in range(len(outlairs)):
        Q1 = df[outlairs[i]].quantile(0.25)
        Q3 = df[outlairs[i]].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df[outlairs[i]] >= Q1 - 1.5*IQR) & (df[outlairs[i]] <= Q3 + 1.5*IQR)]
    df.drop_duplicates()
    df["manufacturer_name"] = df["manufacturer_name"].astype(int)


    x = df.drop("price_usd",axis=1)
    y = df["price_usd"]
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

    model = RandomForestRegressor(n_estimators=9 , random_state=42)
    model.fit(X_train,y_train)
    return (model.predict([final_features])[0])