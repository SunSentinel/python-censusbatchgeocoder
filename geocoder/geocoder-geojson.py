import pandas as pd
import censusbatchgeocoder
import simplejson as json


df = pd.read_csv(
    "./addresses.csv"
)

result = censusbatchgeocoder.geocode(
    df.to_dict("records")[0:],
    id="id",
    address="address",
    city="city",
    state="state",
    zipcode="zipcode"
)

result_df = pd.DataFrame(result)

def df_to_geojson(df, properties, lat='latitude', lon='longitude'):
    geojsondata = {'type':'FeatureCollection', 'features':[]}
    for _, row in df.iterrows():
        feature = {'type':'Feature',
                   'properties':{},
                   'geometry':{'type':'Point',
                               'coordinates':[]}}
        feature['geometry']['coordinates'] = [row[lon],row[lat]]
        for prop in properties:
            feature['properties'][prop] = row[prop]
        geojsondata['features'].append(feature)
    return geojsondata

cols = ['id', 'address', 'city', 'state', 'zipcode', 'metadata']
geojsondata = df_to_geojson(result_df, cols)

output_file = 'output.json'
with open(output_file, 'w') as output_file:
	json.dump(geojsondata, output_file)