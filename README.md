# site-gaz
Site basé sur django, crée pour le PJT sur la digitalisation des capteurs gaz du campus des Arts et Métiers d'Aix-en-Provence.
Sert a récupèrer les données envoyées par les différents capteur. Un capteur peut envoyée des données sur l'endpoint /api/datas.
Les données doivent être au format suivant :
```
{
  "capteur":<mac_adresse>,
  "data":[
          {
            "d":<date>,
            "v":<value>
          },
          {
            "d":<date>,
            "v":<value>
          },
        ],
}
```
