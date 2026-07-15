# NanoFast Results Compiler

🌐 Lisez ceci en : [English](README.md) | [Português (Brasil)](README.pt-br.md) | [Português (Portugal)](README.pt-pt.md) | [Español](README.es.md) | [Français](README.fr.md)

## À quoi sert le Script
Le Compilateur de Résultats NanoFast est un outil d'automatisation Python conçu pour simplifier le traitement et la présentation des résultats de tests Nanofast. Il compile automatiquement les résultats individuels depuis un lecteur ou enregistrés localement vers un modèle Excel maître structuré et facilement lisible pour une analyse ultérieure.

## Comment ça marche
1. **Récupération des Données :** Le script analyse les données dans le répertoire `Raw Data` ou depuis le lecteur pour trouver des dossiers de résultats. Pour chaque dossier, il ouvre le fichier CSV cible et son fichier `result.json` associé.
2. **Extraction des Métadonnées :** Il extrait des métadonnées spécifiques du JSON (y compris l'ID de l'Échantillon, l'Identifiant de la Cassette, le Code de Lot, les détails du Protocole, la Date/l'Heure et le Résultat Final) et les superpose aux données brutes du CSV.
3. **Injection dans le Modèle :** Le script crée un fichier Excel et colle les données compilées dans la feuille `Raw Data`, en attribuant une colonne par résultat de test.
4. **Traitement par Lots et Nommage :** Pour éviter de surcharger le modèle, le script traite les résultats par lots de 40. Il génère dynamiquement des fichiers de sortie nommés avec la date actuelle, l'heure et le numéro de lot (par exemple, `Compiled NanoFast Results - 07 Jul 26 - 15.43 - Part 1.xlsx`).
5. **Nettoyage :** Une fois l'opération réussie, si le script est exécuté localement, il purge automatiquement le dossier `Raw Data` contenant les données copiées pour s'assurer qu'il soit vide et prêt pour la prochaine exécution.

## Comment l'Installer
### Prérequis
* Installez Python *directement depuis le Microsoft Store*. Le script a été testé avec `Python 3.13`.
* Téléchargez la dernière version depuis le dépôt GitHub, en utilisant la section des versions (releases) dans la barre latérale.
* Dans la section des ressources (assets) de la page de la version, téléchargez le fichier .zip.
### Installation
* Extrayez le .zip directement dans votre disque C:. Les installations à d'autres emplacements ne sont pas recommandées et peuvent entraîner des erreurs de chemin d'accès.

### Première exécution
* Lors de la première utilisation, le script télécharge automatiquement les dépendances requises. Veuillez laisser ce processus se terminer.
* Après l'installation des paquets, il vous sera demandé de sélectionner votre langue préférée.
* Les exécutions ultérieures contourneront cette phase de configuration et passeront directement au compilateur.

## Comment l'Utiliser
### Étapes d'Exécution
1. Si vous traitez des données depuis un appareil, connectez le lecteur Nanofast au PC à l'aide d'un câble USB-C, allumez le lecteur et mettez l'appareil en 'Mode de Stockage de Masse' (Mass Storage Mode) via le Menu du lecteur. Si vous utilisez des données locales, copiez tous les dossiers de résultats de tests individuels (chacun contenant un CSV et un `result.json`) dans le dossier `Raw Data`.
2. Exécutez le fichier `Solus NanoFast Compliler.bat` en double-cliquant dessus.
3. Sélectionnez l'emplacement approprié pour le traitement des données.
    * Appuyez sur 1 pour Automatique. Cela récupère automatiquement les résultats depuis l'appareil.
    * Appuyez sur 2 pour Manuel. Pour cette option, copiez manuellement les résultats dans le dossier nommé `Raw Data`.  
4. Sélectionnez la plage de dates pour le traitement des données, en utilisant les flèches haut et bas et en validant avec Entrée.
5. Le script affichera un avertissement dans le terminal vous informant que le dossier `Raw Data` sera supprimé après le traitement. Tapez `Y` et/ou appuyez sur **Entrée** pour continuer. Les données stockées sur un Lecteur ne peuvent pas être supprimées ; cela ne compte que si vous avez transféré des fichiers manuellement.
6. Le terminal affichera la progression au fur et à mesure qu'il divise et exporte les données.
7. Une fois terminé, récupérez vos fichiers `Compiled NanoFast Results` nouvellement générés dans le répertoire principal. Le dossier `Raw Data` sera désormais vide.

## Problèmes Connus
1. Lors du premier lancement, le script installe pandas avec succès mais ne parvient pas à s'initialiser dans la même session. Comme solution de contournement temporaire, le redémarrage du script résoudra le problème. Il s'agit d'un problème connu qui devrait être résolu dans un prochain correctif.

## Traduction
La traduction a été réalisée par Google et non par un locuteur natif. Veuillez fournir vos retours sur la traduction sur GitHub. Nous nous excusons pour toute erreur.

---
Script créé par Steve Carter en 2026.