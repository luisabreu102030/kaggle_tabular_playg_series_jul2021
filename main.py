import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn as sk


def load_data():
    train = pd.read_csv("data/train.csv", index_col="date_time")
    test = pd.read_csv("data/test.csv", index_col="date_time")

    return train, test


def plot_3_variables(train):

    ploter = train.copy().drop(columns=["deg_C","relative_humidity","absolute_humidity","sensor_1","sensor_2","sensor_3","sensor_4","sensor_5"])

    ploter.plot(figsize=(16, 10))
    plt.legend(fontsize="large")
    plt.xlabel("date_time")
    plt.ylabel("Gases evolution");
    plt.show()


def explore_train(train):
    #show all columns
    pd.set_option('display.max_columns', None)

    #general values
    describe = train.describe()
    #print(describe)
    '''
                 deg_C  relative_humidity  absolute_humidity     sensor_1  
    count  7111.000000        7111.000000        7111.000000  7111.000000   
    mean     20.878034          47.561004           1.110309  1091.572100   
    std       7.937917          17.398731           0.398950   218.537554   
    min       1.300000           8.900000           0.198800   620.300000   
    25%      14.900000          33.700000           0.855900   930.250000   
    50%      20.700000          47.300000           1.083500  1060.500000   
    75%      25.800000          60.800000           1.404150  1215.800000   
    max      46.100000          90.800000           2.231000  2088.300000   
    
              sensor_2     sensor_3     sensor_4     sensor_5  
    count  7111.000000  7111.000000  7111.000000  7111.000000   
    mean    938.064970   883.903305  1513.238349   998.335565   
    std     281.978988   310.456355   350.180310   381.537695   
    min     364.000000   310.600000   552.900000   242.700000   
    25%     734.900000   681.050000  1320.350000   722.850000   
    50%     914.200000   827.800000  1513.100000   928.700000   
    75%    1124.100000  1008.850000  1720.400000  1224.700000   
    max    2302.600000  2567.400000  2913.800000  2594.600000   
    
           target_carbon_monoxide  target_benzene  target_nitrogen_oxides  
    count             7111.000000     7111.000000             7111.000000  
    mean                 2.086219       10.237083              204.066784  
    std                  1.447109        7.694426              193.927723  
    min                  0.100000        0.100000                1.900000  
    25%                  1.000000        4.500000               76.450000  
    50%                  1.700000        8.500000              141.000000  
    75%                  2.800000       14.200000              260.000000  
    max                 12.500000       63.700000             1472.300000  

    '''

    #types of attributes
    dtypes = train.dtypes
    #print(dtypes)
    '''
        deg_C                     float64
    relative_humidity         float64
    absolute_humidity         float64
    sensor_1                  float64
    sensor_2                  float64
    sensor_3                  float64
    sensor_4                  float64
    sensor_5                  float64
    target_carbon_monoxide    float64
    target_benzene            float64
    target_nitrogen_oxides    float64
    '''

    #number of missing values
    nr_missing_v = train.isnull().sum()
    #print(nr_missing_v)
    '''
    dtype: object
    deg_C                     0
    relative_humidity         0
    absolute_humidity         0
    sensor_1                  0
    sensor_2                  0
    sensor_3                  0
    sensor_4                  0
    sensor_5                  0
    target_carbon_monoxide    0
    target_benzene            0
    target_nitrogen_oxides    0
    '''

    #plot the the 3 objective variables
    plot_3_variables(train)





if __name__ == '__main__':

    train, test = load_data()

    #see if loaded well
    #print(train.head(5))
    #print(test.head(5))

    #explore trainning data
    explore_train(train)

    print("It's done ! ! !")