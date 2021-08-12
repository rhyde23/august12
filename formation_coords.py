formation_coords = {
	'4-2-3-1 (Wide)': {'ST': (254, 210), 'LM': (54, 275), 'RM': (454, 275), 'CAM': (254, 299), 'LDM': (154, 357), 'RDM': (354, 357), 'LB': (54, 430), 'LCB': (184, 442), 'RCB': (324, 442), 'RB': (454, 430), 'GK': (254, 500)},
	'5-3-2 (Attacking)': {'LS': (184, 214), 'RS': (324, 214), 'CAM': (254, 270), 'LCM': (184, 330), 'RCM': (324, 330), 'LWB': (54, 380), 'LCB': (139, 428), 'CB': (254, 428), 'RCB': (369, 428), 'RWB': (454, 380), 'GK': (254, 500)},
	'4-4-2 (Flat)': {'LS': (184, 214), 'RS': (324, 214), 'LM': (54, 296), 'LCM': (184, 330), 'RCM': (324, 330), 'RM': (454, 296), 'LB': (54, 434), 'LCB': (184, 446), 'RCB': (324, 446), 'RB': (454, 434), 'GK': (254, 500)},
	'5-2-3 (Flat)': {'ST': (254, 224), 'LW': (54, 238), 'RW': (454, 238), 'LCM': (154, 320), 'RCM': (354, 320), 'LWB': (54, 380), 'LCB': (139, 428), 'CB': (254, 420), 'RCB': (369, 428), 'RWB': (454, 380), 'GK': (254, 500)},
	'4-3-3 (Defensive)': {'ST': (254, 210), 'LW': (54, 238), 'RW': (454, 238), 'LCM': (184, 335), 'RCM': (324, 335), 'CDM': (254, 386), 'LB': (54, 434), 'LCB': (184, 446), 'RCB': (324, 446), 'RB': (454, 434), 'GK': (254, 500)}, 
	'4-5-1 (Defensive)': {'ST': (254, 210), 'LM': (54, 317), 'LCM': (184, 328), 'RCM': (324, 328), 'RM': (454, 317), 'CDM': (254, 377), 'LB': (54, 434), 'LCB': (184, 446), 'RCB': (324, 446), 'RB': (454, 434), 'GK': (254, 500)}, 
	'4-3-3 (False 9)': {'CF': (254, 262), 'LW': (54, 238), 'RW': (454, 238), 'LCM': (184, 328), 'RCM': (324, 328), 'CDM': (254, 377), 'LB': (54, 434), 'LCB': (184, 446), 'RCB': (324, 446), 'RB': (454, 434), 'GK': (254, 500)}, 
	'5-3-2 (Flat)': {'LS': (184, 214), 'RS': (324, 214), 'LCM': (139, 311), 'CM': (254, 311), 'RCM': (369, 311), 'LWB': (54, 380), 'LCB': (139, 428), 'CB': (254, 428), 'RCB': (369, 428), 'RWB': (454, 380), 'GK': (254, 500)}, 
	'4-3-3 (Flat)': {'ST': (254, 224), 'LW': (54, 238), 'RW': (454, 238), 'LCM': (153, 328), 'RCM': (354, 328), 'CM': (254, 351), 'LB': (54, 434), 'LCB': (184, 446), 'RCB': (324, 446), 'RB': (454, 434), 'GK': (254, 500)}, 
	'4-3-3 (Attacking)': {'ST': (254, 224), 'LW': (54, 238), 'RW': (454, 238), 'CAM': (254, 313), 'LCM': (153, 343), 'RCM': (354, 343), 'LB': (54, 434), 'LCB': (184, 446), 'RCB': (324, 446), 'RB': (454, 434), 'GK': (254, 500)}, 
	'4-2-3-1 (Narrow)': {'ST': (254, 210), 'LAM': (86, 286), 'CAM': (254, 286), 'RAM': (422, 286), 'LDM': (154, 357), 'RDM': (354, 357), 'LB': (54, 430), 'LCB': (184, 442), 'RCB': (324, 442), 'RB': (454, 430), 'GK': (254, 500)}, 
	'4-1-2-1-2 (Narrow)': {'LS': (184, 214), 'RS': (324, 214), 'CAM': (254, 267), 'LCM': (184, 333), 'RCM': (324, 333), 'CDM': (254, 382), 'LB': (54, 430), 'LCB': (184, 442), 'RCB': (324, 442), 'RB': (454, 430), 'GK': (254, 500)}
}

def get_coords(formation) :
	return formation_coords[formation]
