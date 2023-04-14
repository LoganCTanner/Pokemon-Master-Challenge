'''
the purpose of this program is to download the pokemon main game spawn rate information
to a database


database:
poke_number{
    name: str,
    region{
        GenerationI{
            location0{
                games: [bool,bool,bool]
                sublocation: str,
                levels{
                    highest: int,
                    lowest: int
                }
                spawn rate: int
            }
        }
        GenerationII{
            location0{
                games: boolArr,
                sublocation: str,
                levels{
                    highest: int,
                    lowest: int
                }
                time: boolArr,
                spawn rate: int
            }
        }
        GenerationIII{
            location0{
                games: boolArr,
                sublocation: str,
                levels{
                    highest: int,
                    lowest: int
                }
                spawn rate: int
            }
        }
        GenerationIV{
            location0{
                games: boolArr,
                sublocation: str,
                levels{
                    highest: int,
                    lowest: int
                }
                time: boolArr
                spawn rate: int
            }
        }
        GenerationVII{
            location0{
                games: boolArr,
                sublocation: str,
                levels{
                    highest: int,
                    lowest: int
                }
                spawn rate: int
            }
        }
        .
        .
        .
        generationIV{}
    }
}


regions
Kanto, Johto, Hoenn, Sinnoh, Unova, Kalos, Alola, Galar, and Paldea
- each region has a set of functions for generations
-- generation conditional -> generation function, for location in region

generation conditional

<span id="generation_[I-VIIII]">






generation function
https://bulbapedia.bulbagarden.net/wiki/Category:[region]_locations



html>
    body>
        div>
        div id="globalWrapper>
            div id="column-content">
                div id="content">
                    div id="bodyContent">
                        div id="mw-content-text">
                            div class="mw-parswer-output">






    

1
- pokmeon info: pokemon, games, location, levels, rate

tr>
    td>
        table>
            tbody>
                tr>
                    th>
                        a>
                            img>                    
                    td>
                        a>
                            span> [Pokemon.name]                
    th> style != "background:#FFF;"
    th> style != "background:#FFF;"
    th> style != "background:#FFF;"
    td> 
        table>
            tbody>
                tr>
                    td>
                        a>
                            img>
                    td>
                        a>
                            span>
                                [Pokemon.sublocation]
    td>
        if str contains ",":
            list(str)
        else if str contains "-":
            range(str)
        else:
            single(str)
    td>
        if str contains "%":
            str = str[:-1]
            int(str)


            
            

2
- pokmeon info: pokemon, games, location, levels, time, rate

3
- pokmeon info: pokemon, games, location, levels, rate

4
- pokmeon info: pokemon, games, location, levels, time, rate
5
6
7
8
9


- levels function (maybe don't use)
-- cases: "2-5", "2,3,5", "6"
--- if str in [1,...,9] add str to levelsList, 
    elif str contains ",": for i in str: if i != ",": levelsList.append(i),
    else seperate numbers before & after "-" 

'''



from lxml import html

def get_single_match(parent, query):
    matches = parent.xpath(query)
    if len(matches) == 0:
        return None
    elif len(matches) > 1:
        print('Should be just one sadge')

    return matches[0].text.strip()

def get_multi_match(parent, query):
    return parent.xpath(query)

def get_name(row):
    return get_single_match(row, './td[1]//a/span')

def get_games(row):
    matches = get_multi_match(row, './th//span')
    if len(matches) == 0:
        return None

    return [x.text for x in matches]

def get_location(row):
    match = get_single_match(row, './td[2]//span')
    if match:
        return match
    match = get_single_match(row, './td[2]//td[not(a)]')
    return match

def get_levels(row):
    return get_single_match(row, './td[3]')

def parse_number(entry):
    if entry is None:
        return entry
    if entry[-1] == '%':
        return int(entry[:-1])
    return entry

def get_rate(row):
    matches = get_multi_match(row, './td')
    if len(matches) < 4:
        return None

    return [parse_number(x.text.strip()) for x in matches[3:]]

with open('kantoRoute1.htm', 'rb') as f:
    root = html.parse(f)

    gens = ['I', 'II', 'III', 'IV', 'VII']
    for gen in gens:
        print(f'gen {gen}')
        matches = root.xpath(f'.//span[@id="Generation_{gen}"]/../following-sibling::table[1]')
        for table in matches:
            rows = table.xpath('./tbody/tr')
            for row in rows:
                name = get_name(row)
                games = get_games(row)
                location = get_location(row)
                levels = get_levels(row)
                rate = get_rate(row)

                if name is None or games is None or location is None or levels is None or rate is None:
                    # invalid row
                    continue

                print(f'name: {name}, games: {games}, location: {location}, levels: {levels}, rate: {rate}')

        print('----')