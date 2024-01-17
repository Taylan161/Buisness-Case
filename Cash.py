import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

#Coefficients can be modified for best, median and worst case
#Worst Case
avg_cost = 6000
years = 40
delay = 12
tax_boost = 10000
pp_gain = 5
tax_rate = 25/100
bond = 1.06
name = "Worst Case"
color = "red"

#Median Case
'''
avg_cost = 6000
years = 20
delay = 12
tax_boost = 20000
pp_gain = 10
tax_rate = 25/100
bond = 1.06
'''


#Best Case
'''
avg_cost = 6000
years = 20
delay = 12
tax_boost = 40000
pp_gain = 20
tax_rate = 25/100
bond = 1.06
'''

for nix in range(3):
    #creating the dict with years, constant cost, delayed tax boost
    holder = { "year":[(2023+x) for x in range(years)] ,
               "cost":[ avg_cost for x in range(years)],
               "gain":[0 if x <= delay else pp_gain *(x-delay) * tax_boost * tax_rate for x in range(years) ]}
                #test for sinusoidal cost, to consider changing costs
                # "cost": [avg_cost * (0.2 + abs( + math.sin(2 * math.pi * x/4))) for x in range(years)],

    #dataframe conversion
    real = pd.DataFrame(holder)

    #cumulative cost and gain
    real["cum_cost"] = real["cost"].cumsum()
    real["cum_gain"] = real["gain"].cumsum()


    #adding the time value of money
    real["deval_coef"] = bond ** (real["year"]-2023)

    real["cost_depr"] = real["cost"] / real["deval_coef"]
    real["gain_depr"] = real["gain"] / real["deval_coef"]

    real["cum_cost_depr"] = real["cost_depr"].cumsum()
    real["cum_gain_depr"] = real["gain_depr"].cumsum()

    print(name)
    print(real["cum_gain_depr"]-real["cum_cost_depr"])

    #creating the plots

    #plt.plot(real["year"], real["cost"], label="Cost")
    #plt.plot(real["year"], real["gain"], label="Gain")
    #plt.plot(real["year"], real["cum_cost"], label="Cumulative Cost")
    #plt.plot(real["year"], real["cum_gain"], label="Cumulative Cost")


    plt.plot(real["year"], real["cum_cost_depr"], color = "black" , label="Cumulative Kosten") if nix == 0 else None
    plt.plot(real["year"], real["cum_gain_depr"], color = color,  label= name)



    if nix == 0 :
        # Median Case
        avg_cost = 6000
        years = 20
        delay = 12
        tax_boost = 20000
        pp_gain = 10
        tax_rate = 25 / 100
        bond = 1.06
        name = "Base Case"
        color = "orange"
    elif nix == 1:
        #Best Case
        avg_cost = 6000
        years = 20
        delay = 12
        tax_boost = 40000
        pp_gain = 20
        tax_rate = 25 / 100
        bond = 1.06
        name = "Best Case"
        color = "green"

#additional cosmetics

#plt.xlim(2033,2042)
#plt.ylim(0, 0.25e6)

plt.ylabel("Kosten und Umsatz in €", fontsize="12")
plt.xlabel("Jahre", fontsize="12")
plt.legend()

plt.show()

plt.savefig('Kosten.pdf', bbox_inches='tight')