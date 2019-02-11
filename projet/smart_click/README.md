# smart_click : Betclic Hiring Challenge

## Mission

You will find on the .csv dataset attached the following columns:
- User Id: Unique customer identifier
- Country/Gender/Birthdate: Customer demographics
- PartnerType: The affiliation through which the customer was recruited
- FirstDespositDate: The date during which the first deposit was effectuated
- BetDate: The date of the bet
- Application: Application used by the customer to place bet
- ProductName: The betting product (SportsBook, Casino, …)
- IsLive: If bet was placed during live or not
- BetAmount: The amount placed on a bet
- AmountWon: The amount won from the customer
- Odds: Odds taken by customer
- Cashout: Amount the customer cashed out

### Question 1
EDA on the data provided

#### Reponse
Les données dont nous disposons nous permettent d'avoir une idée du client et du comportement d'utilisation du site ainsi que ces strategies et de son aversion au rique.
Parmis les chiffres les plus marquant, on notera que :    
- les clients ont en moyenne 30 ans  
- sur 8.3 euro parié par le client, 6.8 euro sont gagnés  
- plus de 7000 paris par jour sur betclic  
- un homme gagne en moyenne 6.8 et les femmes 6.5  
Quelques distributions interessantes


### Question 2
If the average lifetime of a customer is 90 days since their first deposit, build a model to predict the Lifetime Value of a customer given his first 15 days of activity. What other data could be pertinent to answer this question? Given the data provided is the assumption of 90 days valid?
Tools to be used: Python
To be delivered: 
A notebook or script with the code
A ppt with 5 slides of the key results as they would be presented to someone non data-savvy

#### Resultat
De facon classique, ce probleme peut etre traité comme un probleme de regression.
En prenant le probleme non pas comme un probleme supervisé en appliquant une regression mais plutot en regroupant les comportmens clients en cluster nous constatons qu'en 15 jours d'activités :  
- les clients generant un ltv haut parient des montants elevé en moyenne, jouent assez peu souvant, sont des femmes, francaise/italienne, sur de Odds assez bas, rarement en live et ont un assez bon ratio de gain.

## Piste

- https://stackoverflow.com/questions/41866841/using-pca-on-linear-regression
- https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60



