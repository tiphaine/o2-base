o2-base
==============================

Collection of useful and heterogeneous data.

## Usage
------------

- INSEE data 
	- population counts
	- confiance des ménages
	- climat des affaires

```make data_insee```

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