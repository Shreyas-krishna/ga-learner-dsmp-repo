# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here

df = pd.read_csv(path)

p_a = len(df[df['fico'] > 700]) / len(df)
p_b = len(df[df['purpose'] == 'debt_consolidation']) / len(df)
print(p_a)
print(p_b)

df1 = df[df['purpose'] == 'debt_consolation']
p_a_b = p_b/p_a

result = (p_a == p_a_b)
print(result)

# code ends here


# --------------
# code starts here

prob_lp = len(df[df['paid.back.loan']== 'Yes']) / len(df)
prob_cs = len(df[df['credit.policy']== 'Yes']) / len(df)
new_df = df[df['paid.back.loan'] == 'Yes']

prob_pd_cs = len(new_df[new_df['credit.policy']== 'Yes']) / len(new_df)

bayes = (prob_pd_cs * prob_lp) / prob_cs

print(prob_lp)
print(prob_cs)
print(prob_pd_cs)
print(bayes)

# code ends here


# --------------
# code starts here

df1 = df[df['paid.back.loan'] == 'No']

df1.plot(kind = 'bar')

# code ends here


# --------------
# code starts here

inst_median = df['installment'].median()
inst_mean = df['installment'].mean()

df['installment'].hist()
df['log.annual.inc'].hist()


# code ends here


