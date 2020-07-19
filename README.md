# DrunkenMarkov
`DrunkenMarkov` is a verbose generator built using recurring markov chains. A graph data-set can be *learned* from and input text, effectively saving the possible word transitions with empirical occurence count as likelyhood to be written back. The learning process has a tweakable recurrence depth parameter, which gives interesting results at n=2 or n=3.

## Learning
The syntax to gather a data-set from an input text is as follows:
`py DrunkenMarkov.py --learn 2 source/the_odyssey.txt data/english_data.json`
Where `2` is the recurrence depth, and the file paths are `{input} {data-set}`

## Writing
The syntax to write text from a data-set is as follows:
`py DrunkenMarkov.py --write data/english_data.json out/english_verbose.txt`
Where the file paths are `{data-set} {output}`

## English Sample
With a data-set from the book *The Odyssey* (here is only a short part of it, but the whole book was used)

> As she spoke she infused fresh vigour into him, and when he had prayed to her he poised his spear and hurled it. He hit Eupeithes’ helmet, and the spear went right through it, for the helmet stayed it not, and his armour rang rattling round him as he fell heavily to the ground. Meantime Ulysses and his son fell upon the front line of the foe and smote them with their swords and spears; indeed, they would have killed every one of them, and prevented them from ever getting home again, only Minerva raised her voice aloud, and made every one pause. “Men of Ithaca,” she cried, “cease this dreadful war, and settle the matter at once without further bloodshed.” 

`DrunkenMarkov` has generated (once again, a short part of it, the output is generated as big as the original book)

> and she was afraid of her husband as was natural upon his estate, but no one seems to have been always good to me from mortal sight, or that i mean to kill the slut of a refund. if you could understand and heed. go in first? but do you, old friend ulysses to get all the maidservants that are over against elis who has never yet got past the fields and farm lands, follow briskly behind the dogs, for they mean nothing but of one plank and rode upon it in the hollow of some kind. then the goddess answered, ‘ulysses, noble son of evenor, answered him saying, “you shall pay for it, nor to their children, and all his days; still i would do my men, but wagged their great wickedness, and has left a son by him, the great and powerful goddess calypso. she took off her veil and put it in his heart growl with anger at the head till it had been borne in upon me and said, “aldermen and town

Which makes no sense at all! ...but follows the general feel and syntax of the original.

## French Sample
`DrunkenMarkov` was also tested with french, and it seems to yield interesting results just as with english:

> Fauchelevent s'était démis la rotule dans sa chute. Le père Madeleine le fit transporter dans une infirmerie qu'il avait établie pour ses ouvriers dans le bâtiment même de sa fabrique et qui était desservie par deux soeurs de charité. Le lendemain matin, le vieillard trouva un billet de mille francs sur sa table de nuit, avec ce mot de la main du père Madeleine: _Je vous achète votre charrette et votre cheval_. La charrette était brisée et le cheval était mort. Fauchelevent guérit, mais son genou resta ankylosé. M. Madeleine, par les recommandations des soeurs et de son curé, fit placer le bonhomme comme jardinier dans un couvent de femmes du quartier Saint-Antoine à Paris.

> où jugera-t-on monsieur le procureur du roi? il arriva à cette phase de calme où l'on peut écouter. m. bamatabois était au nombre des jurés. il chercha javert, mais il ne le chercha pas, il le vit. ses yeux allèrent là naturellement, comme s'ils avaient su d'avance où était cette figure. il crut se voir lui-même, vieilli, non pas sans doute absolument semblable de visage, mais tout pareil d'attitude et d'aspect, avec ces cheveux hérissés, avec cette prunelle fauve et inquiète, avec cette blouse, tel qu'il était le jour où il était arrivé à jean valjean depuis l'aventure de petit-gervais. à partir de 1813, il adhéra ou il applaudit à toutes les manifestations hostiles. il refusa de le voir à son passage au retour de l'île d'elbe, et s'abstint d'ordonner dans son diocèse les prières publiques pour l'empereur pendant les cent-jours.

## Contributors
Please reach out to @ngauthier12 if you wich to contribute to the project. Source is also available under the GNU GPL-V3 license.
