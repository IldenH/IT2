# Persons

Personer registrert i WCA databasen.

Det er viktig å bemerke seg at dersom en person endrer `name`, `countryId` eller `gender`, lages det en ny person, dette bruker WCA for å bevare historikk for hvem personene har vært tidligere.
Dette betyr at det er flere personer i databasen enn som har deltatt i en konkurranse.

`id`-en deres endres ikke. Kan brukes til å fjerne duplicates.
Da bør man beholde den med `subid == 1`, da det er den som er nyest.

## Kolonner

```python
import pandas as pd
df = pd.read_csv("data/WCA_export_Persons.tsv", delimiter="\t")
df.columns
```

Oppgir følgende koloner:

### `subid`

Antall ganger personen har endret `name`, `countryId` eller `gender`.

Tallet begynner på 1. Det vil si at om `subid` er lik 3 har personen endret 2 ganger.

### `name`

Fullt navn til personen.

For de med navn skrevet på et språk svært ulikt fra latin gjøres det om til latin. Eksempel:
[Yiheng Wang (王艺衡)](https://www.worldcubeassociation.org/persons/2019WANY36)

### `countryId`

Landet personen representerer.

### `gender`

Kjønnet til personen.

Følger dette systemet:

| databasen | forklaring |
| --------- | ---------- |
| `m`       | male       |
| `f`       | female     |
| `o`       | other      |

### `id`

WCA sitt system for å identifisere personer.

#### Eksempel

`1999SMIL99`, kan leses som `YYYYNAMEID`, betyr at de:

- Deltok i sin første konkurranse i 1999
- Har et etternavn hvor de første 4 bokstavene er "Smil". Dersom etternavnet har færre enn 4 bokstaver/lyder/tegn fortsetter det med fornavnet til personen. For tidligere nevnte Yiheng Wang får han da `WANY` grunnet "ng" er én lyd på mandarin kinesisk.
- Hvor det er den 99-ende personen som har fått 1999SMIL.
