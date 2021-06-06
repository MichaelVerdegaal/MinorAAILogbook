# Adverserial learning

Om adverserial learning te begrijpen is het eerst verstandig om te weten wat er met adverserial bedoeld wordt. Met 
een adverserial voorbeeld hebben we een voorbeeld dat express bedoeld is een model te laten misclassificeren. Dit wordt 
ook wel "poisoning" genoemd.

![adverserial example](https://openai.com/content/images/2017/02/adversarial_img_1.png)


Dit kunnen we toepassen in de context van machine learning om onze modellen. Dit doen we door een generator en een 
discriminator tegen elkaar op te zetten, de adversaries. De discriminator is je classifier, die voorspellingen maakt en 
getraind is op de training set, en data van de generator. De generator voert ruis aan de discriminator, waarbij die dus 
zo goed mogelijk zijn best doet om de discriminator in de malen te nemen. De discriminator moet zijn best doen om 
desondanks de ruis alsnog correct the voorspellen. Zo zet je deze twee modellen eigenlijk tegen elkaar op.


![ann](https://www.oreilly.com/library/view/java-deep-learning/9781788997454/assets/2cf8b4f1-7163-4af1-aa4b-6066329d554a.png)

