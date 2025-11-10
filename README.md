Ce projet propose un dashboard interactif construit à partir du dataset public https://www.kaggle.com/datasets/alperenmyung/international-hotel-booking-analytics.
L’objectif est d’explorer et de visualiser les tendances du secteur hôtelier international à travers des données réelles sur les hôtels et leurs utilisateurs.

# User Guide

<<<<<<< HEAD
une section User Guide qui fournit les instructions pour déployer et utiliser votre dashboard sur une autre machine ;


# Data 

### hotels.csv : 

### reviews.csv :

### users.csv :


une section Data qui renseigne sur les données utilisées ;

# Developper Guide

une section Developer Guide qui renseigne sur l’architecture du code et qui permet en particulier d’ajouter simplement une page ou un graphique ;

# Rapport d’Analyse

une section Rapport d'analyse qui met en avant les principales conclusions extraites des données ;

# Copyright

une section Copyright qui atteste de l’originalité du code fourni. Par exemple :

je déclare sur l’honneur que le code fourni a été produit par moi/nous même, à l’exception des lignes ci dessous ;

pour chaque ligne (ou groupe de lignes) empruntée, donner la référence de la source et une explication de la syntaxe utilisée ;

toute ligne non déclarée ci dessus est réputée être produite par l’auteur (ou les auteurs) du projet. L’absence ou l’omission de déclaration sera considéré comme du plagiat.
=======
*(Décris ici comment déployer et utiliser ton dashboard sur une autre machine : installation, dépendances, lancement, etc.)*


# Data
## Présentation des données

Le dataset public regroupe des informations sur des hôtels internationaux et leurs clients. Il s'agit d'une base relationnelle composée de trois fichiers CSV : 

### hotels.csv : 
Ce fichier recense les données de 25 hôtels cinq étoiles localisées sur l'ensemble des continents. Chaque hôtel est identifié par un ID unique et accompagné de plusieurs notes de base évaluant dofférents critères de qualité : 

 | **Nom du paramètre** | **Description**                                                                                                                                      |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| hotel_id             | Identifiant unique de l’hôtel.                                                                                                                       |
| hotel_name           | Nom complet de l’hôtel (ex. : The Azure Tower).                                                                                                      |
| city                 | Ville où se situe l’hôtel.                                                                                                                           |
| country              | Pays où se situe l’hôtel.                                                                                                                            |
| star_rating          | Nombre d’étoiles officielles attribuées à l’hôtel.                                                                                         |
| lat                  | Latitude géographique de l’hôtel en decimal.                                                                                                         | 
| lon                  | Longitude géographique de l’hôtel en decimal.                                                                                                        |
| cleanliness_base     | Note moyenne de base sur la propreté(sur 10).                                                                                                   |
| comfort_base         | Note moyenne de base sur le confort (sur 10).                                                                                                    |
| facilities_base      | Note moyenne de base sur les équipements et installations(sur 10).                                                                              |
| location_base        | Note moyenne de base sur la localisation (sur 10).                                                                                               |
| staff_base           | Note moyenne de base sur le personnel (amabilité, professionnalisme, disponibilité) (sur 10).                                                    |
| value_for_money_base | Note moyenne de base sur le rapport qualité/prix (sur 10).                                                                                       |

### users.csv :
Ce fichier fournit des données démographiques sur les utilisateurs ayant séjourné dans les hôtels (âge, genre, pays,...).

 | **Nom du paramètre** | **Description**                                                                                                                                      |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| user_id             | Identifiant unique du client.                                                                                                                       |
| user_gender           | Sexe/Genre de la personne réservante.                                                                                                      |
| country                 | Pays où le client est résident                                                                                                                           |
| age_group              | Tranche d'âge du client                                                                                                                            |
| traveller_type          | Cause du voyage (ex : Voyage solo, familiale, Business,...)                                                                                         |
| join_date                  | Date à laquelle le client a commencé son séjour à l'hôtel.                                                                                                         | 
                                                                                     |
                                                                                     
### reviews.csv :
Ce fichiers fournit les avis et notes des clients selon l'hôtel auquel ils ont séjourné. Il est donc à la fois lié à users.csv et hotels.csv pour effectuer des analyses croisées. 

 | **Nom du paramètre** | **Description**                                                                                                                                      |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| review_id             | Identifiant unique de la review.                                                                                                                       |
| user_id           | Identifiant unique du client.                                                                                                      |
| hotel_id                 | Identifiant unique de l’hôtel.                                                                                                                           |
| review_date              | Date de l'émission de la review.                                                                                                                            |
| score_overall          | Moyenne globale de l'expérience à l'hôtel du client (sur 10).                                                                                         |
| score_cleanliness                  | Note du client sur la propreté de l'hôtel du client (sur 10).                                                                                                         | 
| score_comfort                 | Note du client sur le confort de l'hôtel du client (sur 10).                                                                                                        |
| score_facilities     | Note du client sur les équipements et installations de l'hôtel (sur 10).                                                                                                   |
| score_location         | Note du client sur la localisation de l'hôtel (sur 10).                                                                                                    |
| score_staff      | Note du client sur le personnel de l'hôtel (amabilité, professionnalisme, disponibilité) (sur 10).                                                                              |
| score_value_for_money        | Note du client sur le rapport qualité/prix de l'hôtel (sur 10)                                                                                              |
| review_text           | Informations supplémentaires sur l'expérience à l'hôtel.                                                    |

## Traitement des données

Avant d'utiliser les données pour réaliser notre dashboard, nous devons stocker et nettoyer nos tableaux de possibles erreurs. Pour ce faire, on vient alors créer deux fichiers principaux : 

- get_data.py : Fichier contenant le script de récupération des données.
- clean_data.py : Fichier contenant le script de nettoyage des données.

Cette structure permet de pouvoir gérer les deux fonctions indépendamment l'un de l'autre.

### get_data : 

get_data.py a pour objectif de télécharger le dataset, puis copier tous les fichiers CSV dans un répertoire local. On définit une fonction charger_csvs(), sans paramètre ni retour, qui nous permettra de charger nos fichiers dans le dossier data/raw.

(charger image de la fonction)

- On vient tout d'abord télécharger notre dataset via la fonction telecharger_dataset(nom_dataset).
- On réalise ensuite un parcours de boucle :



*(Explique ici les données utilisées : sources, structure, prétraitement, localisation des fichiers, etc.)*

# Developer Guide

*(Décris ici l’architecture du code, les dossiers principaux, et la procédure pour ajouter une page ou un graphique au dashboard.)*


# Rapport d'analyse

*(Présente ici les principales conclusions issues de ton analyse de données : tendances, corrélations, résultats clés, etc.)*


# Copyright

*(Indique ici que le code est original, éventuellement sous quelle licence il est publié, et à qui il appartient.)*
>>>>>>> f72d9cf9ec7ab9f0b2706d54fdd601d1d7f7c66e
