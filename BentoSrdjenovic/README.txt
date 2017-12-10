Particularit� : 

La mutation � une certaine chance d'arriver � chaque tour de boucle, le taux de chance est d�fini dans chanceToMut, et ensuite le nombre de chemin � concraitement muter est d�fini avec la pourcentageMut multiplier par la population de chemins.

La s�lection se fait par rapport � la population de chemin multiplier par pourcentageSel, qui elle repr�sente le pourcentage des meilleurs chemins actuels nous s�lectionnons, il restera donc (1-pourcentageSel)*population � ajouter � la s�lection que nous prenderons al�atoirement dans les chemins restant.

Pour le croisement je s�lectionne deux parent al�atoirement :
Parent 1, [1,2,4,3,5,6,7,8]
Parent 2, [8,1,4,5,6,2,3,7]

Apr�s je d�finit une s�lection par rapport � deux index al�atoire
index = [1,2,3]
Sel1, [2,4,3]
Sel2, [1,4,5]

Ensuite je cr�e les enfants en mixant le parent 1 avec la selection 2 et vice-versa.
Child1, [1,1,4,5,5,6,7,8]
Child2, [8,2,4,3,6,2,3,7]

Dans notre cas la premi�re case de l'enfant 1 � une valeur qui se trouve d�j� dans la S�lection 2, donc je vais la modifier par une valeur dans la S�lection 1, qui ne se trouve pas dans la s�lection 2.
On fait pour l'ensemble des case qui ne sont pas dans l'index et on obtient des enfants qui passe par toutes les villes.

Child1, [2,1,4,5,3,6,7,8]
Child1, [8,2,4,3,6,1,5,7]