# Work with Python 3.6
import discord
import json
import asyncio

TOKEN = '-removed-'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    '''
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    '''
   
    #This stuff is reference material for server player list commands
    #xq = player_data["grids"][98]["players"][i]["name"]   to get player name in i position on list
    #xqc = len(player_data["grids"][98]["players"])  to get number of players in server
    #print(xq)
    
    #below is original loop used to get list of players
    #while i < len(player_data["grids"][98]["players"]):
                #if i == 0:
                    #player_string = str(player_data["grids"][98]["players"][i]["name"])
                #else:
                    #temp_data = str(player_data["grids"][98]["players"][i]["name"])
                    #player_string = player_string + '\n' + str(player_data["grids"][98]["players"][i]["name"])
                #i += 1
    
    if message.content.startswith('!'):
        try:
            grid_num_input = message.content[1:]
            #print(grid_num_input)
            grid_num = get_grid(grid_num_input)
            with open('data/na_pvp_players_dict.json') as json_data:
                player_data = json.load(json_data)
                #Below is used to verify that the correct grid info is being retrieved
                grid_num = await json_grid_verification(grid_num_input,grid_num)

                    
                        
                player_string = str(len(player_data["grids"][grid_num]["players"])) + ' players in ' + str(player_data["grids"][grid_num]["grid"]) + '   (most recent entry last)'
                i = 0
                while i < len(player_data["grids"][grid_num]["players"]):
                    player_string = player_string + '\n' + str(player_data["grids"][grid_num]["players"][i]["name"])
                    i += 1
            msg = player_string.format(message)
            await client.send_message(message.channel, msg)
        except TypeError:
            msg = ('INVALID INPUT')
            await client.send_message(message.channel, msg)

            
#Verifies that the correct grid is being checked when the json file is being read
#Subtracts 1 from the grid number until a match is found
#This is needed because when servers error out all grids past the errored server drop down a number
async def json_grid_verification(grid_input_check, grid_num_check):
    with open('data/na_pvp_players_dict.json') as json_data:
        player_data = json.load(json_data)
        json_grid_num_check = str(player_data["grids"][grid_num_check]['grid']).lower()
        print(json_grid_num_check + " INITIAL GRID NUM JSON VALUE")
        while (grid_input_check != json_grid_num_check):
            grid_num_check -= 1
            json_grid_num_check = str(player_data["grids"][grid_num_check]['grid']).lower()
            print(grid_input_check + " grid_input_check - A SERVER IS DOWN")
            print(json_grid_num_check + " json_grid_num_check - A SERVER IS DOWN")
    return grid_num_check

        
def get_grid(grid_input):
    grid_switch = {
        'a1': 0,
        'a2': 1,
        'a3': 2,
        'a4': 3,
        'a5': 4,
        'a6': 5,
        'a7': 6,
        'a8': 7,
        'a9': 8,
        'a10': 9,
        'a11': 10,
        'a12': 11,
        'a13': 12,
        'a14': 13,
        'a15': 14,
        'b1': 15,
        'b2': 16,
        'b3': 17,
        'b4': 18,
        'b5': 19,
        'b6': 20,
        'b7': 21,
        'b8': 22,
        'b9': 23,
        'b10': 24,
        'b11': 25,
        'b12': 26,
        'b13': 27,
        'b14': 28,
        'b15': 29,
        'c1': 30,
        'c2': 31,
        'c3': 32,
        'c4': 33,
        'c5': 34,
        'c6': 35,
        'c7': 36,
        'c8': 37,
        'c9': 38,
        'c10': 39,
        'c11': 40,
        'c12': 41,
        'c13': 42,
        'c14': 43,
        'c15': 44,
        'd1': 45,
        'd2': 46,
        'd3': 47,
        'd4': 48,
        'd5': 49,
        'd6': 50,
        'd7': 51,
        'd8': 52,
        'd9': 53,
        'd10': 54,
        'd11': 55,
        'd12': 56,
        'd13': 57,
        'd14': 58,
        'd15': 59,
        'e1': 60,
        'e2': 61,
        'e3': 62,
        'e4': 63,
        'e5': 64,
        'e6': 65,
        'e7': 66,
        'e8': 67,
        'e9': 68,
        'e10': 69,
        'e11': 70,
        'e12': 71,
        'e13': 72,
        'e14': 73,
        'e15': 74,
        'f1': 75,
        'f2': 76,
        'f3': 77,
        'f4': 78,
        'f5': 79,
        'f6': 80,
        'f7': 81,
        'f8': 82,
        'f9': 83,
        'f10': 84,
        'f11': 85,
        'f12': 86,
        'f13': 87,
        'f14': 88,
        'f15': 89,
        'g1': 90,
        'g2': 91,
        'g3': 92,
        'g4': 93,
        'g5': 94,
        'g6': 95,
        'g7': 96,
        'g8': 97,
        'g9': 98,
        'g10': 99,
        'g11': 100,
        'g12': 101,
        'g13': 102,
        'g14': 103,
        'g15': 104,
        'h1': 105,
        'h2': 106,
        'h3': 107,
        'h4': 108,
        'h5': 109,
        'h6': 110,
        'h7': 111,
        'h8': 112,
        'h9': 113,
        'h10': 114,
        'h11': 115,
        'h12': 116,
        'h13': 117,
        'h14': 118,
        'h15': 119,
        'i1': 120,
        'i2': 121,
        'i3': 122,
        'i4': 123,
        'i5': 124,
        'i6': 125,
        'i7': 126,
        'i8': 127,
        'i9': 128,
        'i10': 129,
        'i11': 130,
        'i12': 131,
        'i13': 132,
        'i14': 133,
        'i15': 134,
        'j1': 135,
        'j2': 136,
        'j3': 137,
        'j4': 138,
        'j5': 139,
        'j6': 140,
        'j7': 141,
        'j8': 142,
        'j9': 143,
        'j10': 144,
        'j11': 145,
        'j12': 146,
        'j13': 147,
        'j14': 148,
        'j15': 149,
        'k1': 150,
        'k2': 151,
        'k3': 152,
        'k4': 153,
        'k5': 154,
        'k6': 155,
        'k7': 156,
        'k8': 157,
        'k9': 158,
        'k10': 159,
        'k11': 160,
        'k12': 161,
        'k13': 162,
        'k14': 163,
        'k15': 164,
        'l1': 165,
        'l2': 166,
        'l3': 167,
        'l4': 168,
        'l5': 169,
        'l6': 170,
        'l7': 171,
        'l8': 172,
        'l9': 173,
        'l10': 174,
        'l11': 175,
        'l12': 176,
        'l13': 177,
        'l14': 178,
        'l15': 179,
        'm1': 180,
        'm2': 181,
        'm3': 182,
        'm4': 183,
        'm5': 184,
        'm6': 185,
        'm7': 186,
        'm8': 187,
        'm9': 188,
        'm10': 189,
        'm11': 190,
        'm12': 191,
        'm13': 192,
        'm14': 193,
        'm15': 194,
        'n1': 195,
        'n2': 196,
        'n3': 197,
        'n4': 198,
        'n5': 199,
        'n6': 200,
        'n7': 201,
        'n8': 202,
        'n9': 203,
        'n10': 204,
        'n11': 205,
        'n12': 206,
        'n13': 207,
        'n14': 208,
        'n15': 209,
        'o1': 210,
        'o2': 211,
        'o3': 212,
        'o4': 213,
        'o5': 214,
        'o6': 215,
        'o7': 216,
        'o8': 217,
        'o9': 218,
        'o10': 219,
        'o11': 220,
        'o12': 221,
        'o13': 222,
        'o14': 223,
        'o15': 224,
    }
    return grid_switch.get(grid_input, "Invalid input.")

#Used to monitor for large number of joining players
#changed from async def status_task():
global num_g9_players_prev
async def g9_influx_monitor():
    num_g9_players_prev = 0 #Needed for reasons. Only fires one time.
    while True:
        try:
            #await g9_grid_num = json_grid_verification('g9',98)
            with open('data/na_pvp_players_dict.json') as json_data:
                player_data_monitor = json.load(json_data)
                g9_grid_num = await json_grid_verification('g9',98)
                num_g9_players = len(player_data_monitor["grids"][g9_grid_num]["players"])
                #Below used for initial setting of num_g9_players so that it doesn't activate on startup
                if num_g9_players_prev is 0:
                    num_g9_players_prev = num_g9_players
                else:
                    player_diff = num_g9_players - num_g9_players_prev
                    #*********************************************
                    #Edit below value to change the trigger number
                    if player_diff >= 4:
                        msg = 'A large number of players have entered G9.' + '\n' + str(num_g9_players) + ' players in g9. Previously ' + str(num_g9_players_prev)
                        #Below channel number must be manually set. DO NOT FORGET THE '' AROUND THE NUMBER.
                        await client.send_message(client.get_channel('540205948845948948'), msg)
                    else:
                        pass 
                print(str(player_data_monitor["grids"][g9_grid_num]['grid']) + " monitor grid num")
                num_g9_players_prev = num_g9_players #Update prev num to current num value
                print(num_g9_players) #debugging display
                print(num_g9_players_prev) #debugging display
        except ValueError:
            print('No players in server. PLAYER INFLUX MONITOR')
        await asyncio.sleep(10)
        
        
async def g9_intruder_detection():
    print("INTRUDER DETECTION CHECK")
    while True:
        try:
            g9_grid_num = await json_grid_verification('g9',98)
            intruder_detect_flag = 0
            with open('data/na_pvp_players_dict.json') as json_data:
                player_intruder_check = json.load(json_data)
                num_g9_players = len(player_intruder_check["grids"][g9_grid_num]["players"])
                i = 0
                while i < num_g9_players:
                    player_intruder_check_string = str(player_intruder_check["grids"][g9_grid_num]["players"][i]["name"])
                    j = 0
                    for j in range(len(player_intruder_check_string)):
                        if player_intruder_check_string[j] > '\u4e00' and player_intruder_check_string[j] < '\u9fff':
                            print (player_intruder_check_string[j])
                            intruder_detect_flag = 1
                    i += 1
            if intruder_detect_flag == 1:
                print("POSSIBLE INTRUDERS IN G9")
                intruder_detected_msg = ('CHINESE DETECTED IN G9')
                await client.send_message(client.get_channel("540275952400203796"), intruder_detected_msg)
            else:
                pass
        except ValueError:
            print('No players in server. INTRUDER DETECTION MONITOR')
        await asyncio.sleep(180)
        


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    asyncio.ensure_future(g9_influx_monitor())
    asyncio.ensure_future(g9_intruder_detection())


client.run(TOKEN)
