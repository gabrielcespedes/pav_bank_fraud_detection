import pandas as pd

# Leer claves desde archivo .csv
keys_df = pd.read_csv("python_s3_accessKeys.csv")

# Acceso como variables globales
AWS_ACCESS_KEY = keys_df.loc[0, "Access key ID"]
AWS_SECRET_KEY = keys_df.loc[0, "Secret access key"]

# Región por defecto del bucket
AWS_REGION = "us-east-2"

# Nombre del bucket
S3_BUCKET = "bfd-gabriel"

# Nombres de los archivos en S3
S3_SOURCE_KEYS = [
    "Variant I.csv",
    "Variant II.csv",
    "Variant III.csv",
    "Variant IV.csv"
]

#print(f"AWS_ACCESS_KEY: {AWS_ACCESS_KEY[:4]}***")
#print(f"AWS_SECRET_KEY: {AWS_SECRET_KEY[:4]}***")
#print(f"Bucket: {S3_BUCKET}")