#Web Scraper

import requests, re, pickle, html
from bs4 import BeautifulSoup
from scrape_player_page import main

from file_path_converter import convert_path

pi = True

def scrape(link) :
    page = requests.get(link)
    
    soup = html.unescape(str(BeautifulSoup(page.content, 'html.parser')))
    return soup

teams_in_league = ['AFC Bournemouth', 'Barnsley', 'Birmingham City', 'Blackburn Rovers', 'Brentford', 'Bristol City', 'Cardiff City', 'Coventry City', 'Derby County', 'Huddersfield Town', 'Luton Town', 'Middlesbrough', 'Millwall', 'Norwich City', 'Nottingham Forest', 'Preston North End', 'Queens Park Rangers', 'Reading', 'Rotherham United', 'Sheffield Wednesday', 'Stoke City', 'Swansea City', 'Watford', 'Wycombe Wanderers']
team_fifaindex_indexes = {}
league_page = scrape('https://www.fifaindex.com/teams/?league=14')
remove_parts = ['&']

for team_in_league in teams_in_league :
    link_name = [part for part in team_in_league.lower().split(' ') if not part in remove_parts]
    team_fifaindex_indexes[team_in_league] = re.findall('\"/team/[0-9]+/'+'-'.join(link_name)+'/\"', league_page)[0].split('/')[2]



team_fifaindex_indexes = {'Arsenal': '1', 'Aston Villa': '2', 'Brighton & Hove Albion': '1808', 'Burnley': '1796', 'Chelsea': '5', 'Crystal Palace': '1799', 'Everton': '7', 'Fulham': '144', 'Leeds United': '8', 'Leicester City': '95', 'Liverpool': '9', 'Manchester City': '10', 'Manchester United': '11', 'Newcastle United': '13', 'Sheffield United': '1794', 'Southampton': '17', 'Tottenham Hotspur': '18', 'West Bromwich Albion': '109', 'West Ham United': '19', 'Wolverhampton Wanderers': '110'}
team_fifaindex_indexes = {'AFC Bournemouth': '1943', 'Barnsley': '1932', 'Birmingham City': '88', 'Blackburn Rovers': '3', 'Brentford': '1925', 'Bristol City': '1919', 'Cardiff City': '1961', 'Coventry City': '1800', 'Derby County': '91', 'Huddersfield Town': '1939', 'Luton Town': '1923', 'Middlesbrough': '12', 'Millwall': '97', 'Norwich City': '1792', 'Nottingham Forest': '14', 'Preston North End': '1801', 'Queens Park Rangers': '15', 'Reading': '1793', 'Rotherham United': '1797', 'Sheffield Wednesday': '1807', 'Stoke City': '1806', 'Swansea City': '1960', 'Watford': '1795', 'Wycombe Wanderers': '1933'}


file_path = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Database.dat'])
if pi :
    file_path = convert_path(file_path)

database = pickle.load(open(file_path, 'rb'))

for team_in_league in teams_in_league :
    link = 'https://www.fifaindex.com/team/'+team_fifaindex_indexes[team_in_league]+'/'
    soup = scrape(link)
    
    
    player_links = ['https://www.fifaindex.com'+li[6:]+'/' for li in list(set(re.findall('href=\"/player/[0-9]+', soup)))]
    final_dict = {}
    for player_link in player_links :
        player_data = main(player_link)
        if player_data['Team'] == team_in_league :
            final_dict[player_data['Name']] = player_data
    
    starting_lineup_findings = [finding[7:][:-9] for finding in re.findall('title=\"[^""]+\"', soup) if finding[-8:] == 'FIFA 21\"']
    starting_lineup = []
    for starting_lineup_finding in starting_lineup_findings :
        if starting_lineup_finding in final_dict and not starting_lineup_finding in starting_lineup :
            starting_lineup.append(starting_lineup_finding)
        if len(starting_lineup) == 11 :
            break 
    print("\'"+team_in_league+"_Lineup\':", starting_lineup)
    database[team_in_league] = final_dict
    
output_file = open(file_path, 'wb')
pickle.dump(database, output_file)

"""
final_dict = main()
for team in final_dict :
    file_path = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\', team, '.dat'])
    if pi :
        file_path = convert_path(file_path)
    output_file = open(file_path, 'wb')
    pickle.dump(final_dict[team], output_file)
    print(team)
    for player in final_dict[team] :
        print(final_dict[team][player])
    print()
    print()
    print()



file_path = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\Team Database', '\\ThrowawayFile.dat'])
if pi :
    file_path = convert_path(file_path)
output_file = open(file_path, 'wb')
pickle.dump({}, output_file)

print('Done')
"""

    
    
    
