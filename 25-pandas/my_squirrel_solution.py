import pandas as pd
# Primary Fur Color

# cuantos rojos, grises, and black hay

data = pd.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
list_colors = data['Primary Fur Color'].to_list()


def count_by_color(color):
    count_color_result = [ x for x in list_colors if x == color]
    return len( count_color_result )

def create_data_frame( squirrels_data ):
    try:
        squirrels = pd.DataFrame(squirrels_data)
        squirrels.to_csv('squirrel_count2.csv')
    
    except Exception as e:
        print('Error', e)

gray_count  = count_by_color("Gray")
red_count   = count_by_color("Cinnamon")
black_count = count_by_color("Black")

table = {
    "Color": ["gray", "cinnamon", "black"], 
    "Count": [ gray_count, red_count, black_count]
}

create_data_frame(table)