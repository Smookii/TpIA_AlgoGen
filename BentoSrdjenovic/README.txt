Particularité : 

La mutation à une certaine chance d'arriver à chaque tour de boucle, le taux de chance est défini dans chanceToMut, et ensuite le nombre de chemin à concraitement muter est défini avec la pourcentageMut multiplier par la population de chemins.

La sélection se fait par rapport à la population de chemin multiplier par pourcentageSel, qui elle représente le pourcentage des meilleurs chemins actuels nous sélectionnons, il restera donc (1-pourcentageSel)*population à ajouter à la sélection que nous prenderons aléatoirement dans les chemins restant.

Pour le croisement je sélectionne deux parent aléatoirement :
Parent 1, [1,2,4,3,5,6,7,8]
Parent 2, [8,1,4,5,6,2,3,7]

Après je définit une sélection par rapport à deux index aléatoire
index = [1,2,3]
Sel1, [2,4,3]
Sel2, [1,4,5]

Ensuite je crée les enfants en mixant le parent 1 avec la selection 2 et vice-versa.
Child1, [1,1,4,5,5,6,7,8]
Child2, [8,2,4,3,6,2,3,7]

Dans notre cas la première case de l'enfant 1 à une valeur qui se trouve déjà dans la Sélection 2, donc je vais la modifier par une valeur dans la Sélection 1, qui ne se trouve pas dans la sélection 2.
On fait pour l'ensemble des case qui ne sont pas dans l'index et on obtient des enfants qui passe par toutes les villes.

Child1, [2,1,4,5,3,6,7,8]
Child1, [8,2,4,3,6,1,5,7]