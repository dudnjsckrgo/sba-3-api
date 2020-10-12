import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
from model.crime import CrimeModel 
import folium
print(f'baseurl #### {baseurl}')
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
        reader.fname='seoul_map.json'
        seoul_map =reader.json_load()
        reader.fname ='police_norm.csv'
        reader.new_file()
        police_norm = reader.csv_to_dframe()
        crimeModel =CrimeModel()
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
        #crime in seoul csv 의 raw data
        reader =self.reader
        reader.context =os.path.join(baseurl,'saved_data')
        reader.fname = 'police_positiion.json'
        reader.new_file()
        police_pos =reader.csv_to_dframe()
        police_pos['lat'] = station_lats
        police_pos['lng'] = station_lngs
        
        map = folium.Map(location =[37.5502,126],zoom_start=5)
        map.choropleth( geo_data= seoul_map,
                       name= 'choropleth',
                       data = police_norm,
                       columns = ['구별','살인검거율'],
                       key_on = 'feature.id',
                       fill_color ='YlGn',
                       fill_opacity =0.7,
                       line_opacity =0.2,
                       legend_name ='살인 검거율(%)')
        folium.LayerControl().add_to(map)
        reader = self.reader
        reader.context = os.path.join(baseurl , 'saved_data')
        reader.fname ='police.html'
        
        map.save(reader.new_file())
    def get_unemploy(self):
        pass
    def set_unemploy(self):
        pass
if __name__ == '__main__':
    us = CrimeMap()
    us.create_seoul_crime_map()