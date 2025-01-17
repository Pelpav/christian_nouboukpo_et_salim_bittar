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
