# Residual neural networks

Als we een convolutional neuraal netwerk met een image classification probleem als voorbeeld nemen, dan doet ons model 
het waarschijnlijk als we meer lagen toevoegen. Maar, dit gaat niet oneindig door, en op een bepaald punt gaat ons 
model het juist weer slechter doen. Dit komt doordat er langzaamaan informatie verlies plaats vindt.

Residual nn's proberen dit probleem op te lossen. Dit gebeurt met zogenaamde "skip connections", die informatie vrij 
direct van de eerdere lagen ver naar de achtere doorgeven.
