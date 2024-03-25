# JSON-PATHS

Prints paths in JSON file. Pipe into sort and use diff to compare JSON structure.

Arrays are printed once as the key and for each array element with no index as

```json
.key1
.key1[].key2
```

e.g.

```bash
python json-paths.py --json "C:\Program Files\Microsoft Office\root\Office16\sdxs\FA000000050\dist\config.json"

.AssetID
.Version
.Titles
.Titles[].Locale
.Titles[].Title
.Hosts
.RequirementSets
.RequirementSets[].Name
.RequirementSets[].Version
.Platforms
.DefaultLocale
.Locales
.Locales.macos
.Locales.win32
.Locales.web
.OnDemand
.ConfigSchemaVersion
```
