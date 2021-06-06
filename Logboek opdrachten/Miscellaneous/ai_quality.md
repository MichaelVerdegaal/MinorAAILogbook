# AI quality

Terwijl AI niet technisch nieuw is, voelt het nieuw omdat het pas de laatste jaren echt is opgestegen. We kunnen veel 
revolutionaire dingen bereiken met deze sector, maar er is één groot nadeel aan een sector die in de "hype-bubbel" zit: 
iedereen doet maar wat, zonder enige richting. Dat brengt de vraag naar boven, zijn er bepaalde kwaliteits-standaarden 
waar AI aan kan voldoen? Hieronder een paar voorstellen voor precies dit probleem.

## DIN SPEC 92001

DIN SPEC 92001 is een kwaliteits-standaard ontwikkeld in 2019, die een metamodel beschrijft voor AI kwaliteit. Dit 
model doet dit via drie zogenaamde "pilaren", die bedoeld zijn een geunificeerd oplossing aan te bieden. 

- Pilaar 1, functionaliteit en performance

Deze pilaar staat voor de mate waarin je AI model de taak kan voldoen onder de gestelde voorwaarden. Kwaliteitsdoelen 
betreffen probleemstelling, taakanalyse, gegevensverzameling/analyse/verwerking. Performance evaluatie en model selectie 
zijn ook dingen die je hier behandelt. Je product moet doen wat ie moet doen.

- Pilaar 2, robuustheid

Deze pilaar beschrijft de mate waarijn jouw model om kan gaan met slechte, onbekende, ruizige of adverserial data. AI 
modellen verwerken verschrikkelijk veel parameters, en ze moeten natuurlijk niet kapot gaan met kleine fouten in de 
data. Ook over adverserial data moet je goed nadenken, sinds dit een beveiligings risico kan zijn. In kort, hoe 
"stevig" is je model, en hoe goed kan hij tegen (expres) slechte data. 

- Pilaar 3, begrijpelijkheid

Deze pilaar beschrijft de mate van begrijpelijkheid van je model. AI zijn vaak een soort black box, waar je data erin 
stopt, er wat "magie" gebeurt, en er gewenste data uitkomt. Het is belangrijk voor de stakeholders dat de modellen 
zo transparant als mogelijk zijn. Hierbij wordt de voorkeur dus gegeven aan "white box" modellen.

Ref: Artificial Intelligence – Life Cycle Processes and Quality Requirements – Part 1: Quality Meta Model; 

## ISO/IEC 25010:2011

ISO 25010 is niet technisch een framework voor AI, maar voor software producten in het algemeen. ISO is een organizatie 
voor de standaardizatie van producten, services en systemen, en de 25010 is goed bekend onder praktisch alle software 
engineers. De standaard beschrijft 8 kwaliteits-karakeristieken; functional suitability, reliability, performance 
efficiency, useability, security, maintainability en portability.

Aangezien AI producten ook volledig software gerelateerd zijn, kan je het argument maken dat ISO 25010 ook 
toe te passen is op AI.

## Conclusie

Het lijkt erop dat er niet een standaard is die globaal geaccepteerd is betreft kunstmatige intelligentie, wat te zien 
is in het compleet gebrek aan onderzoeks-papieren die te vinden zijn online.  

De huidige voorstellen hierboven zijn dus ook niet perfect naar mijn mening; Ik ben het bijvoorbeeld niet eens met de
derde pilaar in DIN SPEC, en denk niet dat deze bij alle problemem toegepast zou moeten worden. Ook denk ik niet dat 
de ISO standaard perfect is, aangezien dit bepaalde onderdelen mist, zoals data kwaliteit of explainability.

Er is dus nog niet een perfecte standaard, en alles nu is de voorkeur van de betrokkenen. Mijn voorstel hier is om 
niet te moeilijk na te denken, en je gewoon te houden aan de code conventies van jouw programmeer-teel.





