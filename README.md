o2-base
==============================

Collection of useful and heterogeneous data.

## Usage
------------

- INSEE data 
	- population counts
	- confiance des ménages

```make data_insee```

- World Bank data
	- [Inflation, consumer prices (annual %)](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG) 
		
```make data_world_bank```


## How to add a new data source

- **Sourcing** / Put the url in `data/<data_source_name>/source_config.py` (url, raw and processed file)
- **Downloading** /  Add the function to download the data in `data/<data_source_name>/get_data.py`* 
- **Formatting final data** / Add the function to format and write the final data in `data/<data_source_name>/make_data.py`*
- **Automating** / Add the automation lines in the `data/make_dataset.py` script and in the `Makefile`
- Don't forget to document all your functions !
- **And, you're done !**

\* It is good practice to rely on existing functions from `data/utils.py` to download and write files.