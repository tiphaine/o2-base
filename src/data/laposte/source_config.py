import os

laposte_raw = os.path.join('data', 'raw', 'laposte')
laposte_processed = os.path.join('data', 'processed', 'laposte')

laposte_code_postaux_url = 'https://datanova.legroupe.laposte.fr/explore/dataset/laposte_hexasmal/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'

laposte_code_postaux_files = {
    'raw': os.path.join(laposte_raw, 'laposte-base_code_postaux.csv'),
    'processed': os.path.join(laposte_processed, 'laposte-base_code_postaux.csv'),
}

