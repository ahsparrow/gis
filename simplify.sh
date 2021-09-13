#!/bin/bash

# Convert to separate polygons, clip North of mainland, Lambert
# Conformal Conic projection
ogr2ogr -f GeoJSON clip_explode_proj.json data/GBR_adm.gpkg GBR_adm0 \
    -t_srs data/lcc_ukair.wkt \
    -explodecollections \
    -clipsrc -10 49 10 58.70 \
    -nln gb_coast

# Exclude small islands, simplify geometry and back to WGS84
ogr2ogr -f GeoJSON data/coast.json clip_explode_proj.json \
    -sql "SELECT * from gb_coast WHERE OGR_GEOM_AREA > 100000000" \
    -s_srs data/lcc_ukair.wkt \
    -t_srs EPSG:4326 \
    -simplify 500

rm clip_explode_proj.json
