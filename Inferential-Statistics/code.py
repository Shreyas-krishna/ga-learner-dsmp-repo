# --------------
import pandas as pd
import numpy as np
from scipy import stats
import math

data = pd.read_csv(path)

sample_size = 2000
data_sample = data.sample(n = sample_size, random_state = 0)
sample_mean = data_sample['installment'].mean()
sample_std = data_sample['installment'].std()

z_critical = stats.norm.ppf(q=0.95)
margin_of_error = z_critical*(sample_std / math.sqrt(sample_size))

confidence_interval = (sample_mean - margin_of_error , sample_mean + margin_of_error)  

true_mean = data['installment'].mean()

print("Value of True mean :",true_mean)
print("Confidence intervals :",confidence_interval)
print("Value of sample mean :",sample_mean)


# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])
fig,axes = plt.subplots(3,1,)
#Code starts here

for i in range(len(sample_size)):
    m = []
    for j in (range(1000)):
        sample_data = data['installment'].sample(n= sample_size[i])
        m.append(sample_data.mean())
    mean_series = pd.Series(m)

axes[0].hist(mean_series)
axes[1].hist(mean_series)
axes[2].hist(mean_series)


# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here

data['int.rate'] =  pd.to_numeric(data['int.rate'].map(lambda x: x.rstrip("%"))).apply(lambda x : x/100)
data['int.rate'].unique()
data['int.rate'].describe()

z_statistic, p_value = ztest(x1 = data[data['purpose']=='small_business']['int.rate'], value = data['int.rate'].mean(), alternative =                                    'larger')
print(z_statistic,p_value)

if p_value < 0.05:
    print("we reject the null hypothesis")
if p_value > 0.05:
    print("we accept the null hypothesis")


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here

z_statistic, p_value = ztest(x1 = data[data['paid.back.loan']=='No']['installment'], x2 = data[data['paid.back.loan']=='Yes']                                           ['installment'],alternative='two-sided')

print(z_statistic,p_value)

if p_value < 0.05:
    print("we can reject the null hypothesis")
if p_value > 0.05:
    print("we cannot reject the null hypothesis")


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data[data['paid.back.loan'] == 'Yes']['purpose'].value_counts()
no = data[data['paid.back.loan']=='No']['purpose'].value_counts()
print("have paid back loan:",yes)
print("have not paid back loan:",no)
observed = pd.concat([yes.transpose(),no.transpose()], axis = 1, keys = ['Yes','No'])

chi2,p,dof,ex = chi2_contingency(observed)

if chi2 > critical_value:
    print("we reject the null hypothesis")
if chi2 < critical_value:
    print("null hypothsis cannot be rejected")





