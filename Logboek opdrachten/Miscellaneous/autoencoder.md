Autoencoders zijn een type neural netwerk, waar je als output een opnieuw opgebouwde input terugkrijgt.

Dit doen ze door een vrij specifieke structuur in het netwerk model, die opgebouwed is uit een encoder, een tussenlaag, 
en een decoder. De encoder comprimeert de input data, en geeft dan aan de tussenlaag deze data mee in een lagere 
dimensie. In de tussenlaag doe je wat je zelf wil, en daarna geef je de input door aan de encoder, die een 
reconstructie maakt van de input op basis van je criteria.

![autoencoder](https://miro.medium.com/max/700/1*MMRDQ4g3QvQNc7iJsKM9pg@2x.png)

Autoencoder zijn een een popularie keuze voor veel problemen, maar er zijn een paar problemen waar ze specifiek heel 
goed in zijn. Deze betreffen:

- Ruis verwijderen, e.g. foto's smoothen
- Het veranderen van de dimensionaliteit, e.g. plaatjes resizen
- Sequence to sequence (seq2seq) problemen, e.g. vertalingen maken