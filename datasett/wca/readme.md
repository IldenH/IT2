# [World Cube Association](https://www.worldcubeassociation.org)

Det er to måter å anskaffe data fra WCA databasen:

1. [Den uoffisielle API-en](https://wca-rest-api.robiningelbrecht.be). Den er gjerne tregere siden man må hente litt og litt data i stedet for å bare ha hele databasen lastet ned. Man blir også gjerne fort rate-limited.
2. [WCA export](https://www.worldcubeassociation.org/export/results). Her laster man ned TSV zip filen av hele databasen og pakker den ut som en mappe med navn: `data`.

Noen av python filene bruker API-en, men de fleste bruker databasen lokalt grunnet det er raskere.

## Tabeller

[Persons (tabellen jeg har valgt å fokusere på)](persons/readme.md)
