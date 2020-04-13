o2-base
==============================

Collection of useful and heterogeneous data.

## Usage
------------

- All data

    ```make data_all```

- INSEE data 
	- population counts
	- confiance des ménages
	- climat des affaires
	- couple-famille-menages (France / [ex: 2016](https://www.insee.fr/fr/statistiques/4171359?sommaire=4171370&q=couple+famille+menage))
	- diplome-formation (France / [ex: 2016](https://www.insee.fr/fr/statistiques/4171395?sommaire=4171407))
	
    ```make data_insee```

- CAF data 
	- [allocations foyers bas revenus](http://data.caf.fr/dataset/beneficiaire-bas-revenus)

    ```make data_caf```
    
- LA POSTE data 
	- [base des codes postaux](https://datanova.legroupe.laposte.fr/explore/dataset/laposte_hexasmal/information/?disjunctive.code_commune_insee&disjunctive.nom_de_la_commune&disjunctive.code_postal&disjunctive.ligne_5)

    ```make data_laposte```
    
- World Bank data
	- [Inflation, consumer prices (annual %)](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG) 
		
    ```make data_world_bank```


- European Central Bank
	- [FOREX for Euros/ Euro foreign exchange reference rates](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html) 
		
    ```make data_ecb```


## How to add a new data source

- **Sourcing** / Put the url in `data/<data_source_name>/source_config.py` (url, raw and processed file)
- **Downloading** /  Add the function to download the data in `data/<data_source_name>/get_data.py`* 
- **Formatting final data** / Add the function to format and write the final data in `data/<data_source_name>/make_data.py`*
- **Automating** / Add the automation lines in the `data/make_dataset.py` script and in the `Makefile`
- **Documentation and usage** / Add the Makefile command in the Usage section of the README.md file with the url of the source
- Don't forget to document your functions !
- **And, you're done !**

\* It is good practice to rely on existing functions from `data/utils.py` and `data/helpers.py` to download and write files.