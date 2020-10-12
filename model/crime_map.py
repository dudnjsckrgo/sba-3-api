import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
from model.police import Police
from model.crime import CrimeModel
import folium
import numpy as np

class CrimeMap:

    def __init__(self):
        print(f'baseurl #### {baseurl}')
        self.reader = FileReader() 

    def hook_process(self):
        police = Police()
        police_norm = police.get_police_norm()
        
    def create_seoul_crime_map(self):
        reader = self.reader
        reader.context = os.path.join(baseurl,'data')
        reader.fname = 'seoul_map.json'
        reader.new_file()
        seoul_map = reader.json_load()
        reader.context = os.path.join(baseurl,'saved_data')
        reader.fname = 'police_norm.csv'
        reader.new_file()
        police_norm = reader.csv_to_dframe()
        crimeModel = CrimeModel()
        crime = crimeModel.get_crime()
        print(f'{police_norm.head()}')
        station_names = []
        for name in crime['관서명']:
            station_names.append('서울'+str(name[:-1]+'경찰서'))
        station_addrs = []
        station_lats = [] # 위도
        station_lngs = [] # 경도
        gmaps = reader.create_gmaps()
        for name in station_names:
            t = gmaps.geocode(name, language='ko')
            station_addrs.append(t[0].get('formatted_address'))
            t_loc = t[0].get('geometry')
            station_lats.append(t_loc['location']['lat'])
            station_lngs.append(t_loc['location']['lng'])
            print(name+'----->' + t[0].get('formatted_address'))

        # crime_in_seroul.csv 의 raw data
        reader = self.reader
        reader.context = os.path.join(baseurl,'saved_data')
        reader.fname = 'police_position.csv'
        reader.new_file()
        police_pos = reader.csv_to_dframe()
        police_pos['lat'] = station_lats
        police_pos['lng'] = station_lngs

        print(police_pos)

        col = ['살인 검거','강도 검거','강간 검거','절도 검거','폭력 검거']
        tmp = police_pos[col] /  police_pos[col].max()
        police_pos['검거'] = np.sum(tmp, axis = 1)





        # 지도 그리기
       
        map = folium.Map(location=[37.5502, 126.982], zoom_start=12)
        map.choropleth(
            geo_data = seoul_map,
            name = 'choropleth',
            data = tuple(zip(police_norm['구별'], police_norm['범죄'])),
            columns = ['구별','살인검거율'],
            key_on = 'feature.id',
            fill_color = 'PuRd',
            fill_opacity = 0.7,
            line_opacity = 0.2,
            legend_name = 'CRIME (%)'

        )
        folium.LayerControl().add_to(map)
        reader = self.reader
        reader.context = os.path.join(baseurl,'saved_data')
        reader.fname = 'police.html'
        map.save(reader.new_file())
        

if __name__ == '__main__':
    crime = CrimeMap()

    crime.create_seoul_crime_map()
