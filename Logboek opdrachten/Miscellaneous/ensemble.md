Ensemble learning verwijst naar het combineren van meerdere sub-modellen, die samen trainen, en ze bij het voorspellen
gezamelijk tot een conclusie laten komen.

Het primaire doel van deze techniek is om meer the generaliseren, en zo overfitting te voorkomen. In het geval dat je
e.g. 3 sub-modellen hebt die samen stemmen voor een resultaat, dan krijg je alleen outliers als 2/3 van de modellen de
fout maakt, en niet bij 1/3. We snappen nu het doel wel, maar hoe leer je in ensemble dan eigenlijk? Daar zijn vrij veel
opties voor. Hieronder een paar highlights:

- Bagging. Je neemt willekeurig subsets van je train dataset, en traint sub-modellen op die subsets. Bij het voorspellen
  combineer je de voorspellingen, met voting of averaging, afhankelijk van of je classificatie of regressie doet.
  
![bagging](https://cdn.discordapp.com/attachments/697855611643232394/847107146276798474/ImageGlass_eTpJb7P205.png)
- Boosting. Je traint sequentieel 1 model per keer, maar bij elke iteratie geef je meer gewicht aan de voorspellingen
  waar het model het fout heeft gedaan, die je dan aan het volgende model meegeeft.
  
![boosting](https://cdn.discordapp.com/attachments/697855611643232394/847107154312691782/ImageGlass_R6cKvB8fNS.png)
- Stacking. Je neemt meerdere basis sub-modellen, die elk een voorspelling maken, en je heb dan een soort aggregator die
  puur bedoeld is om de voorspellingen te combineren.
  
![stacking](https://miro.medium.com/max/946/1*T-JHq4AK3dyRNi7gpn9-Xw.png)

Er zijn wel toch nadelen voor ensemble learning. Primair:

- Training tijd. Je traint meer modellen, dus het duurt langer, spreekt voor zich zelf.
- Modellen trainen is van nature stochastisch, en het kan gebeuren dat sub-modellen niet de optimale gradients bereiken.
- De data heeft een te grote bias, en alle sub-modellen leren die bias gezamelijk.