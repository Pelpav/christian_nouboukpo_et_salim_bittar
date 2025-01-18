# Models

User (id: int, firstname: string, lastname: string, email: string, username: string, password: string)
Client hérite de User (id: int, tel: string, adresse: string, numPieceID: string[Unique], typePieceID: string, photo: image)
Le client effectue une Location (id: int, dateLocation: dateTime, datePaiement: dateTime, dateSortie: dateTime, dateRetour: dateTime, statut: string, adresseLivraison: string[Parking par défaut]): Méthode (total():int)
Une location peut faire suite à un avis (id: int, note: float, commentaire: text)
Une location concerne un Véhicule (id: int, immatriculation: string[Unique], prix: int, etat: string, description: string, marque: string, modele: string, type: string, couleur: string, carburant: string, boitevitesse: string, climatisation: boolean == True, nbrRoues: int == 4, nbrPlaces: int == 5, nbrPortes: int == 5, kilometrage: float, cylindre: float, anneeFabrication: int, anneeCirculation: int)
Un Véhicule doit avoir des Documents (id: int, nom: string, dateEmission: dateTime, dateValidite: dateTime, src: file)
Un Véhicule peut avoir une Photo ou non (id: int, indication: string, src: image)
Location_Vehicule (id: int, etatSortie: string, etatRetour: string)
Location_Vehicule peut avoir Dommage (id: int, description: string, photo: image)
Un Dommage fait l'objet d'une maintenance qui se répercute sur un Véhicule (id: int, causes: text, traitement: text, montant: int, dateEntree: dateTime, dateSortie: dateTime, preuves: file)

# Structure du projet

Back: backend
Front: frontend
Myauth: authentification

# Informations

Username : Admin
Password : 12345678


# Bugs actuels de l'application :
# 1. Erreur de récupération lors du checkout : Cela se produit lorsque les détails des véhicules ne peuvent pas être récupérés correctement, entraînant un échec de la validation du panier.
# 
# 2. Problème de redirection après validation : L'utilisateur n'est pas redirigé vers la page de confirmation après avoir validé l'achat.
# 
# 3. Gestion des erreurs : Les messages d'erreur ne sont pas toujours clairs pour l'utilisateur, ce qui complique le diagnostic des problèmes.
# 
# 4. Problème de session utilisateur : Dans certains cas, l'utilisateur peut être déconnecté de manière inattendue pendant le processus de paiement.
# 
# 5. Validation des données : Les données du formulaire de paiement ne sont pas toujours validées correctement, ce qui peut entraîner des erreurs lors de la soumission.
# 
# 6. Problèmes de performance : Le chargement des détails des véhicules peut être lent, affectant l'expérience utilisateur.
# 
# 7. Problème de compatibilité : L'application peut rencontrer des problèmes sur certains navigateurs ou appareils mobiles.
# 
# 8. Erreurs de sécurité : Des failles potentielles dans la gestion des sessions et des données sensibles.
# 
# 9. Problèmes d'affichage : Certains éléments de l'interface utilisateur peuvent ne pas s'afficher correctement sur toutes les résolutions d'écran.
# 
# 10. Bugs liés aux notifications : Les notifications de confirmation d'achat ne sont pas toujours envoyées à l'utilisateur.
# 
# Il est recommandé de corriger ces bugs pour améliorer l'expérience utilisateur et la fiabilité de l'application.
# End of Selection
