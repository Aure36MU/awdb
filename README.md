# AWBW/AWDB
***********************
*ADVANCE WARS DATABASE*
***********************

This is a project based on the game series Advance Wars.
One part will be a quick battle simulator using customized game balances (or game rules)
The other part will be a recreation of the game using these game balances. Really not the priority ATM.



Rules of the game (FR, extract from AWBW_class_hierarchy) :

```
Le jeu [Game] consiste en une bataille stratégique au tour par tour, sur une carte à dimensions finies [Map (fichier)]. De deux à quatre personnes peuvent s'affronter en tant que commandant [CO] d'une armée d'unités [Unit].

Les données d'une unité [Unit] : Chaque unité possède un nom, une division (par exemple Terrestre), un coût, une portée minimale et maximale, un déplacement maximal, un type de déplacement, une vision, un nombre de munitions pour l'arme primaire (maximal), un nombre d'unités de carburant (maximal), et quelques propriétés supplémentaires si besoin.
Les données d'un commandant [CO] : Chaque CO possède un nom, un type de COZone (Fixe, Croissante, Infinie...), la taille minimum de la COZone, une liste d'effets lorsque le général est embarqué, est-ce que le CO possède une rupture basique puis sa liste d'effets, même chose pour la SUPER rupture.
Les données d'une carte [Map (fichier)] : Chaque carte doit spécifier le nom, les dimensions (hauteur, largeur), une liste de terrains qui indique le contenu de cette carte case par case.

Beaucoup de données peuvent aussi être générées à partir d'un fichier que donne l'utilisateur, qui peut ainsi créer sa propre "balance" de jeu. Les fichiers Unitbalance, CObalance génèrent des classes [Unit] et [CO] respectivement, tandis que Gamebalance fixera d'autres données ainsi que les classes [Terrain], [Climate], [Charts].
Unitbalance (et CObalance ?) doivent être chargés APRES Gamebalance car leur données dépendent de ce qui est contenu dans Gamebalance.

[Terrain] : Un terrain possède un nom, un type, sa valeur de couverture, puis est-ce que ce terrain constitue une cachette ou non.
[Climate] : Un climat possède un nom, et une liste d'effets représentant des commandes. Voir AWBW_command_list.
Les mécaniques du brouillard de guerre (FoW) sont déjà implantées dans le jeu.
[Charts] : Les chartes décrivant la balance actuelle du jeu. Contient la damage_chart (x=Unit.name ; y=Unit.name) tableau 2d carrée dont les repères sont dans damage_chart_indexes la liste de Unit.name, ainsi que le movement_chart (x=Terrain.name ; y=Unit.movement_type) tableau 2d dont les repères sont dans movement_chart_indexes la liste de Terrain.name ainsi que dans movement_type_list la liste de Unit.movement_type.

Pour éviter des problèmes d'accessibilité aux données, ainsi que le fait que l'on peut faire affonter deux CO identiques sur la même carte, toutes les données du jeu / d'une partie actuel(le) sont une copie des données par défaut. Ainsi des sous-classes [CurrentUnit], [CurrentCO], [CurrentMap] sont créées à partir de leurs classes parents respectives. Ils contiennent les mêmes données que leurs classes parents mais avec quelques attributs en plus.

[CurrentUnit] : Chaque unité en jeu possède aussi une valeur de santé (différent des PV, les PV représentent un arrondi à l'unité supérieure de la santé), le nombre de munitions actuel, le nombre d'unités de carburant actuel, un rang (0;1;2;3), est-ce que l'unité est l'unité du général ou non, (et peut-être une référence au CO actuel qui l'utilise ?)
[CurrentCO] : Chaque CO en jeu possède aussi un numéro de joueur, (une affectation à une armée ?), le niveau de jauge de rupture actuel, le statut de jauge de rupture actuel. ...
[CurrentMap] : Chaque carte en jeu possède aussi le tour actuel, ...


Dans une partie : Chaque partie dure un certain nombre de tours, limité ou non dans ce nombre.
```
-------------------------------------------------------------


Contents :

/doc
Contains many documentation and notes about the project
(changelog, database, spreadsheet...)
The latest spreadsheet is AWBW_sheet_latest.xlsx
Some files written in french will probably be localized, idk

/pygame
The files used by the Pygame module (not used ATM)

/src
Source files
Currently working on data.py, game.py, main.py, textparser.py

-------------------------------------------------------------

TODOs : Many things including...
```
-Clean/delete unnecessary files, first commit was there to keep a version of everything
-Include class diagram (already done on paper)
-Rework the text parser in a simpler way :
 Create directly an instance with default parameters
 Then set parameters each time necessary
 Modify getWord, getLine (make getWordsInLine instead)
-Test calculations
-The other part
```




<sub>(slt Full_Korbe tu peux venir maintenant bsx)</sub>
