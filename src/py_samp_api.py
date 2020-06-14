# -*- coding: utf-8 -*-

"""
Created on Tue Mar 24 13:02:17 2020

@author: Teodoro_Bagwell
"""

from ctypes import windll, c_ubyte, c_int, c_float, pointer, cast, POINTER
from datetime import datetime
from struct import pack, unpack
from time import time
from win32gui import FindWindow
import win32process


# GTA offsets
ADDR_ZONECODE                = 0xA49AD4      # Player Zone
ADDR_POSITION_X              = 0xB6F2E4      # Player X Position
ADDR_POSITION_Y              = 0xB6F2E8      # Player Y Position
ADDR_POSITION_Z              = 0xB6F2EC      # Player Z Position
ADDR_CPED_PTR                = 0xB6F5F0      # Player CPED Pointer
ADDR_CPED_HPOFF              = 0x540         # Player Health
ADDR_CPED_ARMOROFF           = 0x548         # Player Armour
ADDR_CPED_MONEY              = 0x0B7CE54     # Player Money
ADDR_CPED_INTID              = 0xA4ACE8      # Player Interior-ID
ADDR_CPED_SKINIDOFF          = 0x22          # Player Skin-ID
ADDR_VEHICLE_PTR             = 0xBA18FC      # Vehicle CPED Pointer
ADDR_VEHICLE_HPOFF           = 0x4C0         # Vehicle Health
ADDR_VEHICLE_DOORSTATE       = 0x4F8         # Vehicle Door Status
ADDR_VEHICLE_ENGINESTATE     = 0x428         # Vehicle Engine Status
ADDR_VEHICLE_SIRENSTATE      = 0x1069        # Vehicle Siren Status
ADDR_VEHICLE_SIRENSTATE2     = 0x1300        # Vehicle AltSiren Status
ADDR_VEHICLE_LIGHTSTATE      = 0x584         # Vehicle Light Status
ADDR_VEHICLE_MODEL           = 0x22          # Vehicle Car-ID & Car-Name
ADDR_VEHICLE_TYPE            = 0x590         # Vehicle Typ-ID (1 = Car)
ADDR_VEHICLE_DRIVER          = 0x460         # Vehicle Driver
ADDR_VEHICLE_X               = 0x44          # Vehicle Speed X
ADDR_VEHICLE_Y               = 0x48          # Vehicle Speed Y
ADDR_VEHICLE_Z               = 0x4C          # Vehicle Speed Z
ADDR_VEHICLE_COLOR           = 0x434
ADDR_VEHICLE_COLOR2          = 0x435
ADDR_WANTED                  = 0x58DB60
ADDR_WEAPON                  = 0xBAA410
ADDR_WIDTH                   = 0xC9C040
ADDR_HEIGHT                  = 0xC9C044
ADDR_RADIO                   = 0x4CB7E1
ADDR_STATE                   = 0x530
ADDR_IS_IN_MENU              = 0xBA67A4
ADDR_MAP_POS_X               = 0xBA67B8
ADDR_MAP_POS_Y               = 0xBA67BC
ADDR_MAP_ZOOM                = 0xBA67AC
rmaddrs 					 = (0xC7DEC8, 0xC7DECC, 0xC7DED0)
ADDR_NIGHT_VISION            = 0xC402B8
ADDR_THERMAL_VISION          = 0xC402B9
ADDR_TIME                    = 0xB70153
ADDR_SETTIME                 = 0x52D168
ADDR_WEATHER                 = 0xC81320
ADDR_ANTI_BIKEFALL           = 0x4BA3B9
ADDR_DEAGLE_SKILL            = 0xB7949C
ADDR_9MM_SKILL               = 0xB79496
ADDR_SDPISTOL_SKILL          = 0xB79498
ADDR_SHOTGUN_SKILL           = 0xB794A0
ADDR_SPAS12_SKILL            = 0xB794A8
ADDR_UZI_SKILL               = 0xB794AC
ADDR_SMG_SKILL               = 0xB794B0
ADDR_AK47_SKILL              = 0xB794B4
ADDR_M4_SKILL                = 0xB794B8
ADDR_INVISIBLE_CARS          = 0x96914B
ADDR_BLOW_ALL_CARD           = 0x96914A
ADDR_RED_COLOR               = 0xBAB22C
ADDR_GREEN_COLOR             = 0xBAB230
ADDR_WHITE_COLOR             = 0xBAB238
ADDR_YELLOW_COLOR            = 0xBAB244
ADDR_RADIO_COLOR             = 0xBAB24C


aircraft_models = (417, 425, 447, 460, 469, 476, 487, 488, 497, 511, 512,     \
                   513, 519, 520, 548, 553, 563, 577, 592, 593)
bike_models = (481, 509, 510)
boat_models = (430, 446, 452, 453, 454, 472, 473, 484, 493, 539, 595)
unmanned_models = (435, 441, 449, 450, 464, 465, 501, 564, 569, 570, 584,     \
                   590, 591, 594, 606, 607, 608, 610, 611)
train_models = (449, 537, 538)
radio_names = ("Playback FM", "K Rose", "K-DST", "Bounce FM", "SF-UR",        \
               "Radio Los Santos", "Radio X", "CSR 103.9", "K-JAH West",      \
               "Master Sounds 98.3", "WCTR Talk Radio", "User Track Player",  \
               "Radio Off")
weather_names = ("EXTRASUNNY_LA", "SUNNY_LA", "EXTRASUNNY_SMOG_LA",           \
                 "SUNNY_SMOG_LA", "CLOUDY_LA", "SUNNY_SF", "EXTRASUNNY_SF",   \
                 "CLOUDY_SF", "RAINY_SF", "FOGGY_SF", "SUNNY_VEGAS",          \
                 "EXTRASUNNY_VEGAS", "CLOUDY_VEGAS",                          \
                 "EXTRASUNNY_COUNTRYSIDE", "SUNNY_COUNTRYSIDE",               \
                 "CLOUDY_COUNTRYSIDE", "RAINY_COUNTRYSIDE",                   \
                 "EXTRASUNNY_DESERT", "SUNNY_DESERT", "SANDSTORM_DESERT",     \
                 "UNDERWATER", "EXTRACOLOURS_1", "EXTRACOLOURS_2")
weapon_id_for_model = {1:331, 2:333, 3:334, 4:335, 5:336, 6:337, 7:338,       \
                       8:339, 9:341, 10:321, 11:322, 12:323, 13:324, 14:325,  \
                       15:326, 16:342, 17:343, 18:344, 22:346, 23:347,        \
                       24:348, 25:349, 26:350, 27:351, 28:352, 29:353,        \
                       30:355, 31:356, 32:372, 33:357, 34:358, 35:359,        \
                       36:360, 37:361, 38:362, 39:363, 40:364, 41:365,        \
                       42:366, 43:367, 44:368, 45:369, 46:371}
oVehiclePoolData = [0]


# SAMP Offsets
ADDR_SAMP_INCHAT_PTR                 = 0x21A10C  # R1 0x21a10c   R2 0x21a114
ADDR_SAMP_INCHAT_PTR_OFF             = 0x55      # R1 0x55    R2 0x60
ADDR_SAMP_USERNAME                   = 0x219A6F  # R1 0x219A6F, R2 0x219A77
FUNC_SAMP_SENDCMD                    = 0x65C60   # R1 0x65c60  R2 0x65d30
FUNC_SAMP_SENDSAY                    = 0x57F0    # R1 0x57f0  R2 0x57e0
FUNC_SAMP_ADDTOCHATWND               = 0x640E0
ADDR_SAMP_CHATMSG_PTR                = 0x21A0EC
ADDR_SAMP_INPUT_PTR                  = 0x21A0F0
SAMP_MY_INPUT_PTR                    = 0x12D8F8
FUNC_SAMP_SHOWGAMETEXT               = 0x9C370
ADDR_SAMP_SHOWDLG_PTR                = 0x21A0B8
FUNC_SAMP_PLAYAUDIOSTR               = 0x62E70
FUNC_SAMP_STOPAUDIOSTR               = 0x62A70

DIALOG_STYLE_MSGBOX			         = 0
DIALOG_STYLE_INPUT 			         = 1
DIALOG_STYLE_LIST			         = 2
DIALOG_STYLE_PASSWORD		         = 3
DIALOG_STYLE_TABLIST			     = 4
DIALOG_STYLE_TABLIST_HEADERS	     = 5

SAMP_DIALOG_STRUCT_PTR               = 0x21A0B8   # R1 0x21A0B8 R2 0x21a0c0
SAMP_DIALOG_PTR1_OFFSET				 = 0x1C
SAMP_DIALOG_LINES_OFFSET 			 = 0x44C
SAMP_DIALOG_INDEX_OFFSET			 = 0x443
SAMP_DIALOG_BUTTON_HOVERING_OFFSET	 = 0x465
SAMP_DIALOG_BUTTON_CLICKED_OFFSET	 = 0x466
SAMP_DIALOG_PTR2_OFFSET 			 = 0x20
SAMP_DIALOG_LINECOUNT_OFFSET		 = 0x150
SAMP_DIALOG_OPEN_OFFSET				 = 0x28
SAMP_DIALOG_STYLE_OFFSET			 = 0x2C
SAMP_DIALOG_ID_OFFSET				 = 0x30
SAMP_DIALOG_TEXT_PTR_OFFSET			 = 0x34
SAMP_DIALOG_CAPTION_OFFSET			 = 0x40
FUNC_SAMP_SHOWDIALOG                 = 0x6B9C0  # R1 0x6B9C0;  R2 0x6BA70
FUNC_SAMP_CLOSEDIALOG                = 0x6B210  # R1 0x6B210;  R2 0x6B2C0
FUNC_SAMP_PRESSBUTTON                = 0x6C040  # R1 0x6C040;  R2 0x6C0F0
FUNC_SAMP_SENDDIALOG                 = 0x30B30  # R1 0x30B30;  R2 0x30C10
SAMP_SENDDIALOG_ATR                  = 0xD7FA8  # R1 0xD7FA8;  R2 0xD7FB8
FUNC_SAMP_DELETE_TEXTLABEL           = 0x12D0   # R1 0x12D0;   R2 0x12E0
FUNC_SAMP_CREATE_TEXTLABEL           = 0x11C0   # R1 0x11C0;   R2 0x11D0
SAMP_PLAYER_COLOR_OFFSET             = 0x216378 # R1 0x216378; R2 0x216380
SAMP_FUNC_TEXTDRAW                   = 0x1AE20  # R1 0x1AE20;  R2 0x1AF00
FUNC_SAMP_DELETE_TEXTDRAW            = 0x1AD00  # R1 0x1AD00;  R2 0x

FUNC_UPDATESCOREBOARD                = 0x8A10   # R1 0x8A10
SAMP_INFO_OFFSET                     = 0x21A0F8 # R1 0x21A0F8, R2 0x21A100
SAMP_RAKCLIENT						 = 0x3C1  # R1 3C9, R2 3C1
SAMP_POOLS						     = 0x3CD  # R1 3CD, R2 3C5
SAMP_POOL_ACTOR						 = 0x0
SAMP_POOL_OBJECT					 = 0x4
SAMP_POOL_GANGZONE				     = 0x8
SAMP_POOL_TEXTLABEL					 = 0xC   # R1 0xC, R2 0x1C
SAMP_POOL_TEXTDRAW					 = 0x10  # R1 0x10, R2 0x20
SAMP_TEXTDRAW_LETTERWIDTH			 = 0x963
SAMP_TEXTDRAW_LETTERHEIGHT			 = 0x967
SAMP_TEXTDRAW_PROPORTIONAL			 = 0x97E
SAMP_TEXTDRAW_RIGHT 				 = 0x986
SAMP_TEXTDRAW_FONT 					 = 0x987
SAMP_TEXTDRAW_XPOS 					 = 0x98B
SAMP_TEXTDRAW_YPOS 					 = 0x98F
SAMP_POOL_PLAYERLABEL				 = 0x14
SAMP_POOL_PLAYER					 = 0x8
SAMP_REMOTEPLAYERS					 = 0x26
SAMP_LOCALPLAYER					 = 0x22
SAMP_POOL_VEHICLE					 = 0x1C
SAMP_POOL_PICKUP					 = 0x20
ADDR_SAMP_CRASHREPORT                = 0x5D00C
SAMP_PPOOL_PLAYER_OFFSET             = 0x18     # R1  0x18, R2 0x8
SAMP_SLOCALPLAYERID_OFFSET           = 0x4      # R1 0x4, R2 0x0
SAMP_ISTRLEN_LOCALPLAYERNAME_OFFSET  = 0x16
SAMP_SZLOCALPLAYERNAME_OFFSET        = 0x6
SAMP_PSZLOCALPLAYERNAME_OFFSET       = 0x6
SAMP_PREMOTEPLAYER_OFFSET            = 0x2E     # R1 0x2E  R2 0x26
SAMP_ISTRLENNAME_OFFSET              = 0x1C     # R1 0x1C, R2 0x24
SAMP_SZPLAYERNAME_OFFSET             = 0xC      # R1 0xC, R2 0x14
SAMP_PSZPLAYERNAME_OFFSET            = 0xC      # R1 0xC, R2 0x14
SAMP_ILOCALPLAYERPING_OFFSET         = 0x33
SAMP_ILOCALPLAYERSCORE_OFFSET        = 0x22
SAMP_IPING_OFFSET                    = 0x4
SAMP_ISCORE_OFFSET                   = 0x0
SAMP_ISNPC_OFFSET                    = 0x8
SAMP_PLAYER_MAX                      = 1004
SAMP_VEHPOOL                         = 0xC      # R1 = 0x1C
SAMP_LISTED                          = 0x3074
SAMP_VEHPTR                          = 0x4FB4
SAMP_VEH                             = 0x1134
SAMP_PLATE                           = 0x93
SIZE_SAMP_CHATMSG                    = 0xFC
SAMP_KILLSTAT_OFFSET                 = 0x21A0EC
SAMP_CHKPNT_OFFSET 				     = 0xC7DEEA

PLAYER_STATE_LEAVING_VEHICLE 	= 0
PLAYER_STATE_NORMAL 			= 1
PLAYER_STATE_DRIVING 			= 50
PLAYER_STATE_DYING 				= 54
PLAYER_STATE_DEAD 				= 55

GAMESTATE_WAIT_CONNECT 		= 9
GAMESTATE_CONNECTING 		= 13
GAMESTATE_AWAIT_JOIN 		= 15
GAMESTATE_CONNECTED 		= 14
GAMESTATE_RESTARTING 		= 18

FIGHT_STYLE_NORMAL 			= 4
FIGHT_STYLE_BOXING 			= 5
FIGHT_STYLE_KUNGFU 			= 6
FIGHT_STYLE_KNEEHEAD 		= 7
FIGHT_STYLE_GRABKICK 		= 15
FIGHT_STYLE_ELBOW 			= 16

VEHICLE_TYPE_CAR			= 1
VEHICLE_TYPE_BIKE			= 2
VEHICLE_TYPE_HELI			= 3
VEHICLE_TYPE_BOAT			= 4
VEHICLE_TYPE_PLANE			= 5

OBJECT_MATERIAL_TEXT_ALIGN_LEFT   	= 0
OBJECT_MATERIAL_TEXT_ALIGN_CENTER 	= 1
OBJECT_MATERIAL_TEXT_ALIGN_RIGHT  	= 2

OBJECT_MATERIAL_SIZE_32x32  		= 10
OBJECT_MATERIAL_SIZE_64x32			= 20
OBJECT_MATERIAL_SIZE_64x64			= 30
OBJECT_MATERIAL_SIZE_128x32			= 40
OBJECT_MATERIAL_SIZE_128x64			= 50
OBJECT_MATERIAL_SIZE_128x128		= 60
OBJECT_MATERIAL_SIZE_256x32			= 70
OBJECT_MATERIAL_SIZE_256x64			= 80
OBJECT_MATERIAL_SIZE_256x128		= 90
OBJECT_MATERIAL_SIZE_256x256		= 100
OBJECT_MATERIAL_SIZE_512x64			= 110
OBJECT_MATERIAL_SIZE_512x128		= 120
OBJECT_MATERIAL_SIZE_512x256		= 130
OBJECT_MATERIAL_SIZE_512x512		= 140

SAMP_MAX_PLAYERTEXTDRAWS			= 256
SAMP_MAX_TEXTDRAWS					= 2048
SAMP_MAX_TEXTLABELS					= 2048
SAMP_MAX_GANGZONES					= 1024
SAMP_MAX_PICKUPS					= 4096
SAMP_MAX_OBJECTS					= 1000
SAMP_MAX_PLAYERS					= 1004
SAMP_MAX_VEHICLES					= 2000

h_gta = 0x0
dw_gtapid = 0x0
dw_samp = 0x0
p_memory = 0x0
p_param1 = 0x0
p_param2 = 0x0
p_param3 = 0x0
p_param4 = 0x0
p_param5 = 0x0
p_inject_func = 0x0
n_zone = 1
n_city = 1
b_init_zac = 0
b_init_zac_two = 0;
multVehicleSpeed_tick = 0
i_refresh_scoreboard = 0
scoreboard_data = {}
text_draws = {}
text_labels = {}
i_refresh_handles = 0
i_update_tick = 2500


''' INTERNAL FUNCTIONS BLOCK '''

def get_pid(name):
    hw = FindWindow(0, name)
    if hw:
        return win32process.GetWindowThreadProcessId(hw)[1]
    return 0


def open_process(pid):
    return windll.kernel32.OpenProcess(0x1F0FFF, False, pid)


def close_handle(handle):
    return windll.kernel32.CloseHandle(handle)


def get_module_base_address(smodule, hprocess):
    if not hprocess:
        return None
    curdlls = win32process.EnumProcessModulesEx(hprocess,                     \
                                                win32process.LIST_MODULES_ALL)
    for dll in curdlls:
        dllname = str(win32process.GetModuleFileNameEx(hprocess, dll)).lower()
        if smodule in dllname:
            return dll
    return None


def read_string(hprocess, dwaddress, dwlen, encoding = 'windows-1251'):
    buffer = (c_ubyte * dwlen)()
    windll.kernel32.ReadProcessMemory(hprocess, dwaddress, buffer, dwlen, 0)    
    char2 = bytearray()
    for x in range(len(buffer)):
        if buffer[x] != 0:
            char2.append(buffer[x])
        else:
            break
    return char2.decode(encoding, errors='ignore')


def read_dword(hprocess, dwaddress):
    return read_mem(hprocess, dwaddress, 4)
  
    
def read_mem(hprocess, dwaddress, dwlen):
    if not hprocess:
        return 0
    buffer = (c_ubyte * dwlen)()
    windll.kernel32.ReadProcessMemory(hprocess, dwaddress, buffer, dwlen, 0)
    result_i = 0
    for i in range(dwlen):
        result_s = (str(hex(buffer[i])) + ('00' * i))
        result_i += int(result_s[2:], 16)
    return result_i

    
def virtual_alloc_ex(hprocess, dwsize, flprt):
    if not hprocess:
        return 0
    return windll.kernel32.VirtualAllocEx(hprocess, 0, dwsize,                \
                                         0x1000 | 0x2000, flprt)


def virtual_free_ex(hprocess, lpaddr, dwsize, dwtype):
    if not hprocess:
        return 0
    return windll.kernel32.VirtualFreeEx(hprocess, lpaddr, dwsize, dwtype)


def create_remote_thread(hprocess, lpattr, dwstacksz, lpstrtaddr, lpparam,    \
                         dwflags, lpthreadid):
    if not hprocess:
        return 0
    return windll.kernel32.CreateRemoteThread(hprocess, lpattr, dwstacksz,    \
                                             lpstrtaddr, lpparam, dwflags,    \
                                             lpthreadid)


def wait_for_single_object(hthread, ms):
    if not hthread:
        return 0
    ret = windll.kernel32.WaitForSingleObject(hthread, ms)
    if ret == 0xFFFFFFFF:
        return 0
    else:
        return ret


def refresh_gta():
    global h_gta
    global dw_gtapid
    global dw_samp
    global p_memory
    pid = get_pid('GTA:SA:MP')
    if pid == 0:
        if h_gta:
            virtual_free_ex(h_gta, p_memory, 0, 0x8000)
            close_handle(h_gta)
            h_gta = 0x0
        dw_gtapid = 0
        h_gta = 0x0
        dw_samp = 0x0
        p_memory = 0x0
        return False
    if h_gta == 0 or dw_gtapid != pid:
        h_gta = open_process(pid)
        dw_gtapid = pid
        dw_samp = 0x0
        p_memory = 0x0
        return True
    return True


def refresh_samp():
    global dw_samp
    if dw_samp:
        return True
    dw_samp = get_module_base_address('samp.dll', h_gta)
    if not dw_samp:
        return False
    return True


def refresh_memory():
    global p_memory
    global p_param1
    global p_param2
    global p_param3
    global p_param4
    global p_param5
    global p_inject_func
    if not h_gta:
        return False
    if not p_memory:
        p_memory = virtual_alloc_ex(h_gta, 6144, 0x40)
        p_param1 = p_memory
        p_param2 = p_memory + 1024
        p_param3 = p_memory + 2048
        p_param4 = p_memory + 3072
        p_param5 = p_memory + 4096
        p_inject_func = p_memory + 5120
    return True


def check_handles():
    if not refresh_gta() or not refresh_samp() or not refresh_memory():
        return False
    else:
        return True
    
    
def get_username():
    if not check_handles():
        return ''
    dw_address = dw_samp + ADDR_SAMP_USERNAME
    s_username = read_string(h_gta, dw_address, 25)
    return s_username


def hex_to_float(s):
    i = int(s, 16)                   # convert from hex to a Python int
    cp = pointer(c_int(i))           # make this into a c integer
    fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
    return fp.contents.value         # dereference the pointer, get the float


def read_float(hprocess, dw_address):
    if not hprocess:
        return 0
    hex_v = read_dword(hprocess, dw_address)
    float_str = str(hex((hex_v)))
    float_v = hex_to_float(float_str)
    return float_v


def byte_prepare(value, vtype = 'dword'): # 'dword', 'short', 'float'
    if vtype == 'float':
        value_in = hex(unpack('<I', pack('<f', value))[0])
        if str(value_in) == '0' or str(value_in) == '0x0':
            hex_str = '00000000'
        else:
            hex_str = str(value_in)[2:]
    else:
        if value < 0:
            value_in = hex((value + (1 << 32)) % (1 << 32))
        else:
            value_in = hex(value)
        hex_str = str(value_in)[2:]
    if len(hex_str) % 2 == 1:
        hex_str = '0' + hex_str
    hex_lst = []
    for i in range(1, int(len(hex_str)/2) + 1):
        hex_lst.append(hex_str[(i - 1) * 2:(i - 1) * 2 + 2])
    hex_lst = list(reversed(hex_lst))
    if vtype == 'short':
        for i in range(2 - len(hex_lst)):
            hex_lst.append('0')
    else:
        for i in range(4 - len(hex_lst)):
            hex_lst.append('0')
    for i in range(len(hex_lst)):
        hex_lst[i] = int(hex_lst[i], 16)
    return hex_lst


''' MAIN FUNCTIONS BLOCK '''

def get_player_hp():
    if not check_handles():
        return -1
    dw_cpedptr = read_dword(h_gta, ADDR_CPED_PTR)
    dw_address = dw_cpedptr + ADDR_CPED_HPOFF
    float_v = read_float(h_gta, dw_address)
    return float_v


def get_player_armor():
    if not check_handles():
        return -1
    dw_cpedptr = read_dword(h_gta, ADDR_CPED_PTR)
    dw_address = dw_cpedptr + ADDR_CPED_ARMOROFF
    float_v = read_float(h_gta, dw_address)
    return float_v


def get_coordinates():
    if not check_handles():
        return -1
    f_x = read_float(h_gta, ADDR_POSITION_X)
    f_y = read_float(h_gta, ADDR_POSITION_Y)
    f_z = read_float(h_gta, ADDR_POSITION_Z)
    return [f_x, f_y, f_z]


def get_red_marker():
    if not check_handles():
        return -1
    coords = [0, 0, 0]
    for i in range(3):
        coords[i - 1] = read_float(h_gta, rmaddrs[i - 1])
    if coords == [0, 0, 0]:
        return -1
    return coords


def get_distance(coords1, coords2):
    vect_diff = [0, 0, 0]
    if coords1 == -1 or coords2 == -1:
        return -1
    for i in range(3):
        vect_diff[i-1] = coords1[i-1] - coords2[i-1]
    vect_dist = (vect_diff[0] ** 2 + vect_diff[1] ** 2 +                      \
                 vect_diff[2] ** 2) ** 0.5
    return vect_dist


def get_player_money():
    if not check_handles():
        return -1
    money = read_mem(h_gta, ADDR_CPED_MONEY, 4)
    return money


def get_player_skin():
    if not check_handles():
        return -1
    dw_cpedptr = read_dword(h_gta, ADDR_CPED_PTR)
    dw_address = dw_cpedptr + ADDR_CPED_SKINIDOFF
    skin_id = read_mem(h_gta, dw_address, 2)
    return skin_id


def get_player_wanted():
    if not check_handles():
        return -1
    wanted = read_mem(h_gta, ADDR_WANTED, 1)
    return wanted


def get_player_weapon():
    if not check_handles():
        return -1
    weapon = read_mem(h_gta, ADDR_WEAPON, 4)
    return weapon    
    

def get_resolution():
    if not check_handles():
        return [-1, -1]
    width = read_dword(h_gta, ADDR_WIDTH)
    height = read_dword(h_gta, ADDR_HEIGHT)
    return [width, height]


def is_player_in_vehicle():
    if not check_handles():
        return 0
    dw_vehptr = read_dword(h_gta, ADDR_VEHICLE_PTR)
    return dw_vehptr > 0
    

def is_player_driver():
    if not check_handles():
        return 0
    dw_vehptr = read_dword(h_gta, ADDR_VEHICLE_PTR)
    dw_cpedptr = read_dword(h_gta, ADDR_CPED_PTR)
    dw_val = read_dword(h_gta, dw_vehptr + ADDR_VEHICLE_DRIVER)
    return dw_val == dw_cpedptr


def get_vehicle_health():
    if not check_handles():
        return 0
    dw_vehptr = read_dword(h_gta, ADDR_VEHICLE_PTR)
    health = read_float(h_gta, dw_vehptr + ADDR_VEHICLE_HPOFF)
    return health


def get_vehicle_id():
    if not check_handles():
        return 0
    dw_address = read_dword(h_gta, ADDR_VEHICLE_PTR)
    if not dw_address:
        return 0
    veh_id = read_mem(h_gta, dw_address + ADDR_VEHICLE_MODEL, 2)
    return veh_id


def get_vehicle_lights():
    if not check_handles():
        return 0
    dw_address = read_dword(h_gta, ADDR_VEHICLE_PTR)
    if not dw_address:
        return 0
    dw_val = read_mem(h_gta, dw_address + ADDR_VEHICLE_LIGHTSTATE, 1)
    return dw_val > 0


def get_vehicle_engine():
    if not check_handles():
        return 0
    dw_address = read_dword(h_gta, ADDR_VEHICLE_PTR)
    if not dw_address:
        return 0
    c_val = read_mem(h_gta, dw_address + ADDR_VEHICLE_ENGINESTATE, 1)
    return c_val == 24 or c_val == 56 or c_val == 88 or c_val == 120


def get_vehicle_siren():
    if not check_handles():
        return 0
    dw_address = read_dword(h_gta, ADDR_VEHICLE_PTR)
    if not dw_address:
        return 0
    c_val = read_mem(h_gta, dw_address + ADDR_VEHICLE_SIRENSTATE, 1)
    return c_val == -48


def get_vehicle_lock():
    if not check_handles():
        return 0
    dw_address = read_dword(h_gta, ADDR_VEHICLE_PTR)
    if not dw_address:
        return 0
    dw_val = read_dword(h_gta, dw_address + ADDR_VEHICLE_DOORSTATE)
    return dw_val == 2


def get_vehicle_color():
    if not check_handles():
        return 0
    dw_address = read_dword(h_gta, ADDR_VEHICLE_PTR)
    if not dw_address:
        return 0
    dw_val = read_mem(h_gta, dw_address + ADDR_VEHICLE_COLOR, 1)
    return dw_val


def get_vehicle_color2():
    if not check_handles():
        return 0
    dw_address = read_dword(h_gta, ADDR_VEHICLE_PTR)
    if not dw_address:
        return 0
    dw_val = read_mem(h_gta, dw_address + ADDR_VEHICLE_COLOR2, 1)
    return dw_val


def get_vehicle_speed():
    if not check_handles():
        return 0
    dw_address = read_dword(h_gta, ADDR_VEHICLE_PTR)
    if not dw_address:
        return 0
    speed_x = read_float(h_gta, dw_address + ADDR_VEHICLE_X)
    speed_y = read_float(h_gta, dw_address + ADDR_VEHICLE_Y)
    speed_z = read_float(h_gta, dw_address + ADDR_VEHICLE_Z)
    speed_inner = (speed_x ** 2 + speed_y ** 2 + speed_z ** 2) ** 0.5
    speed = speed_inner * 100 * 1.43
    return speed


def get_player_radio():
    if not check_handles():
        return -1
    if not is_player_in_vehicle():
        return -1
    dw_gta = get_module_base_address('gta_sa.exe', h_gta)
    radio_id = read_mem(h_gta, dw_gta + ADDR_RADIO, 1)
    return radio_id


def get_radio_name(rad_id):
    if rad_id == 0:
        return -1
    if rad_id >= 0 and rad_id < 14:
        return radio_names[rad_id - 1]
    return ''


def get_player_state():
    if not check_handles():
        return -1
    dw_cpedptr = read_dword(h_gta, ADDR_CPED_PTR)
    state = read_dword(h_gta, dw_cpedptr + ADDR_STATE)
    return state


def on_state(state):
    if get_player_state == state:
        return True
    else:
        return False
    
    
def is_player_in_menu():
    if not check_handles():
        return -1
    in_menu = read_mem(h_gta, ADDR_IS_IN_MENU, 4)
    return in_menu
    

def get_menu_map_data():
    if not check_handles():
        return -1
    map_data = [0, 0, 0]
    map_data[0] = read_float(h_gta, ADDR_MAP_POS_X)
    map_data[1] = read_float(h_gta, ADDR_MAP_POS_Y)
    map_data[2] = read_float(h_gta, ADDR_MAP_ZOOM)
    if map_data == [0, 0, 0]:
        return 0
    else:
        return map_data


def get_vehicle_plate():
    if not check_handles():
        return ''
    dw_vehptr = read_dword(h_gta, ADDR_VEHICLE_PTR)
    if dw_vehptr == 0:
        return ''
    dw_info = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    if dw_info == 0:
        return ''
    dw_pools = read_dword(h_gta, dw_info + SAMP_POOLS)
    if dw_pools == 0:
        return ''
    vehpool = read_dword(h_gta, dw_pools + 0xC)
    for i in range(2000):
        x = i - 1
        listed = read_dword(h_gta, vehpool + SAMP_LISTED + x * 4)
        if listed == 0:
            continue
        svehptr = read_dword(h_gta, vehpool + SAMP_VEHPTR + x * 4)
        if svehptr == dw_vehptr:
            sampveh = read_dword(h_gta, vehpool + SAMP_VEH + x * 4)
            if sampveh == 0:
                return ''
            plate = read_string(h_gta, sampveh + SAMP_PLATE, 32)
            return plate
    return ''


def toggle_night_vision():
    if not check_handles():
        return -1
    if read_mem(h_gta, ADDR_NIGHT_VISION, 1) == 0:
        write_mem(h_gta, ADDR_NIGHT_VISION, 1)
    elif read_mem(h_gta, ADDR_NIGHT_VISION, 1) == 1:
        write_mem(h_gta, ADDR_NIGHT_VISION, 0)
    return -1


def toggle_thermal_vision():
    if not check_handles():
        return -1
    if read_mem(h_gta, ADDR_THERMAL_VISION, 1) == 0:
        write_mem(h_gta, ADDR_THERMAL_VISION, 1)
    elif read_mem(h_gta, ADDR_THERMAL_VISION, 1) == 1:
        write_mem(h_gta, ADDR_THERMAL_VISION, 0)
    return -1


def float_to_hex(value):
    return hex(unpack('<I', pack('<f', value))[0])
    
def write_mem(hprocess, dwaddress, value, v_type = 'int'):
    if isinstance(value, float):
        value_in = hex(unpack('<I', pack('<f', value))[0])
        if str(value_in) == '0' or str(value_in) == '0x0':
            hex_str = '00000000'
        else:
            hex_str = str(value_in)[2:]
    elif isinstance(value, str):
        buffer = bytes(value, 'windows-1251')
        buffer += bytes([0])
        ret = windll.kernel32.WriteProcessMemory(hprocess, dwaddress,         \
                                                 buffer, len(buffer), 0)
        return False if ret == 0 else True
    else:
        value_in = hex(value)
        hex_str = str(value_in)[2:]
    if len(hex_str) % 2 == 1:
        hex_str = '0' + hex_str
    hex_lst = []
    for i in range(1, int(len(hex_str)/2) + 1):
        hex_lst.append(hex_str[(i - 1) * 2:(i - 1) * 2 + 2])
    if v_type == 'dword' or isinstance(value, float):
        hex_lst = list(reversed(hex_lst))
        for i in range(4 - len(hex_lst)):
            hex_lst.append('0')
    buffer = (c_ubyte * len(hex_lst))()
    for i in range(len(hex_lst)):
        buffer[i] = int(hex_lst[i], 16)
    ret = windll.kernel32.WriteProcessMemory(hprocess, dwaddress, buffer,     \
                                             len(buffer), 0)
    return False if ret == 0 else True

    
def set_time(hour):
    if not check_handles():
        return -1
    write_mem(h_gta, ADDR_SETTIME, 0x909090909090)
    write_mem(h_gta, ADDR_TIME, hour)


def hp_patch():
    if not check_handles():
        return False
    a = write_mem(h_gta, 0x4B35A0, 0x560CEC83)
    b = write_mem(h_gta, 0x4B35A4, 0xF18B)
    return a and b


def set_player_health(hp):
    if not check_handles():
        return -1
    dw_cpedptr = read_dword(h_gta, ADDR_CPED_PTR)
    dw_address = dw_cpedptr + ADDR_CPED_HPOFF
    hp = float(hp)
    return write_mem(h_gta, dw_address, hp)


def set_player_armor(hp):
    if not check_handles():
        return -1
    dw_cpedptr = read_dword(h_gta, ADDR_CPED_PTR)
    dw_address = dw_cpedptr + ADDR_CPED_ARMOROFF
    hp = float(hp)
    return write_mem(h_gta, dw_address, hp)


def set_vehicle_health(hp):
    if not check_handles():
        return -1
    if hp > 100.0:
        hp = 100.0
    dw_vehptr = read_dword(h_gta, ADDR_VEHICLE_PTR)
    dw_address = dw_vehptr + ADDR_VEHICLE_HPOFF
    fl_hp = float(hp) * 10
    return write_mem(h_gta, dw_address, fl_hp)
    

def toggle_anti_bikefall(tog = -1):
    if not check_handles():
        return -1
#    byte = read_mem(h_gta, ADDR_ANTI_BIKEFALL, 1)
    if tog == 1 or tog == True:
        write_mem(h_gta, ADDR_ANTI_BIKEFALL, 0xE9A703000090)
        return True
    else:
        write_mem(h_gta, ADDR_ANTI_BIKEFALL, 0x0F84A6030000)
        return False
    return -1


def anti_crash():
    if not check_handles():
        return False
    c_report = ADDR_SAMP_CRASHREPORT
    write_mem(h_gta, dw_samp + c_report, 0x90909090)
    c_report += 0x4
    write_mem(h_gta, dw_samp + c_report, 0x90)
    c_report += 0x9
    write_mem(h_gta, dw_samp + c_report, 0x90909090)
    c_report += 0x4
    write_mem(h_gta, dw_samp + c_report, 0x90)
    return True
    
    
def print_low(text, time):
    if not check_handles():
        return -1
    dw_func = 0x69F1E0
    call(h_gta, dw_func, [["s",text], ["i", time], ["i", 1], ["i", 1]], True)
    return True


def get_chat_line_ex(line = 0):
    # 0x152 - offset of 1-st message
    # 0xFC - size of message, 0xD0 - size of message without additional bytes
    # 99 - max messages
    if not check_handles():
        return ''
    dw_ptr = dw_samp + ADDR_SAMP_CHATMSG_PTR
    dw_address = read_dword(h_gta, dw_ptr)
    msg = read_string(h_gta, dw_address + 0x152 + ( (99 - line) * 0xFC), 0xD0)
    return msg


def set_chat_line_ex(text, line = 0):
    # 0x152 - offset of 1-st message
    # 0xFC - size of message, 0xD0 - size of message without additional bytes
    # 99 - max messages
    if not check_handles():
        return ''
    dw_ptr = dw_samp + ADDR_SAMP_CHATMSG_PTR
    dw_address = read_dword(h_gta, dw_ptr)
    msg = write_mem(h_gta, dw_address + 0x152 + ( (99 - line) * 0xFC), text)
    return msg


def get_chat_line_color(line = 0):
    if not check_handles():
        return ''
    dw_ptr = read_dword(h_gta, dw_samp + ADDR_SAMP_CHATMSG_PTR)
    cl_address = dw_ptr + 0x152 + ((99 - line) * 0xFC) + 0xD4
    clr = str(hex(read_mem(h_gta, cl_address, 3)))[2:].upper()
    for i in range(6 - len(clr)):
        clr = '0' + clr
    return clr


def get_chat_line_timestamp(line = 0, unix = False):
    if not check_handles():
        return -1
    dw_ptr = read_dword(h_gta, dw_samp + ADDR_SAMP_CHATMSG_PTR)
    ts_address = dw_ptr + 0x152 + ((99 - line) * 0xFC) - 0x20
    timestamp = read_mem(h_gta, ts_address, 4)
    ts = datetime.fromtimestamp(timestamp)
    return ts if not unix else timestamp


'''
def remove_chat_line(line = 0):
    if not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_swamp + ADDR_SAMP_CHATMSG_PTR)
    if not dw_address():
        return False
    for i in range(100 - line):
        a = ''
        dw_line = dw_address + 0x132 + ((99 - i - line) * 0xFC)
        for i in range(0xFC):
            # LATER
'''


def get_mem_chatlog():
    if not check_handles():
        return False
    for i in range(100):
        if get_chat_line_color(99-i) != '000000'                              \
        and get_chat_line_ex(99 - i) != '':
            color = '{' + get_chat_line_color(99-i) + '}'
            timestamp = '[' + str(get_chat_line_timestamp(99 - i))[11:] + '] '
            print(color, timestamp, get_chat_line_ex(99 - i), sep='')
    return True


def add_chat_message(wtext, color = 'FFFFFF', timestamp = True):
    if not check_handles():
        return False
    dw_func = dw_samp + FUNC_SAMP_ADDTOCHATWND
    if timestamp:
        tstmp = 4
    else:
        tstmp = 2
    if color:
        color2 = str(hex(int(color, 16)))[2:]
        color = int(color2, 16)
        if color < 0 or color > 16777216:
            color = 0xFFFFFFFF
    while True:
        if get_chat_line_ex().find('V') != -1 or \
        get_chat_line_ex(1).find('V') != -1 or\
        get_chat_line_ex(2).find('V') != -1 or\
        get_chat_line_ex(3).find('V') != -1:
            for i in range(19):
                if get_chat_line_ex(i+1).find('V') != -1:
                    line = get_chatlog_line(i+1)
                    line_ab = get_chatlog_line(i+2)
                    line_bl = get_chatlog_line(i)
                    if line_ab == get_chat_line_ex(i+2)                       \
                    and line_bl == get_chat_line_ex(i+1):
                        set_chat_line_ex(line, i+1)
                    if line_ab == get_chat_line_ex(i+3)                       \
                    and line_bl == get_chat_line_ex(i+1):
                        set_chat_line_ex(line, i+2)
                    elif line_ab == get_chat_line_ex(i+1):
                        set_chat_line_ex(line, i)
                    elif line_ab == get_chat_line_ex(i+4)                     \
                    and line_bl == get_chat_line_ex(i+2):
                        set_chat_line_ex(line, i+3)
                    else:
                        set_chat_line_ex(line, i+1)
            continue
        break
    call(h_gta, dw_func, \
         [['i', read_dword(h_gta, dw_samp + ADDR_SAMP_CHATMSG_PTR)],          \
           ['i', tstmp], ['s', wtext], ['i', 0], ['i', color],                \
           ['i', 0]], False, True)
    return True
    
    
def send_chat(wtext):
    if not check_handles():
        return False
    dw_func = 0
    if wtext[0] == '/':
        dw_func = dw_samp + FUNC_SAMP_SENDCMD
    else:
        dw_func = dw_samp + FUNC_SAMP_SENDSAY
    call(h_gta, dw_func, [["s", wtext]], False)
    return True


def show_game_text(text, time, size):
    time = int(time)
    size = int(size)
    if not check_handles():
        return False
    dw_func = dw_samp + FUNC_SAMP_SHOWGAMETEXT
    call(h_gta, dw_func, [["s", text], ["i", time], ["i", size]], False)
    return True


def refresh_scoreboard():
    if not check_handles():
        return 0
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    if dw_address == 0:
        return 0
    dw_func = dw_samp + FUNC_UPDATESCOREBOARD
    inject_data = (c_ubyte * 11)() # MOV + CALL + RETN
    inject_data[0] = 0xB9
    addr = str(hex(dw_address))[2:]
    for f in range(8 - len(addr)):
        addr = '0' + addr
    addr = '0x' + \
    ''.join(reversed([addr[g:g+2] for g in range(0, len(addr), 2)]))
    for x in range(4):
        if len(addr) < 5:
            inject_data[x + 1] = int(addr, 16)
            break
        if len(addr) > 4:
            inject_data[x + 1] = int(addr[:4], 16)
            addr = addr[:2] + addr[4:]
    inject_data[5] = 0xE8
    offset = dw_func - (p_inject_func + 10)
    if offset < 0:
        offset = hex((offset + (1 << 32)) % (1 << 32))
    else:
        offset = hex(offset)
    offs = str(offset)[2:]
    for f in range(8 - len(offs)):
        offs = '0' + offs
    offs = '0x' + \
    ''.join(reversed([offs[g:g+2] for g in range(0, len(offs), 2)]))
    for xx in range(4):
        if len(offs) < 5:
            inject_data[6 + xx] = int(offs, 16)
            break
        if len(offs) > 4:
            inject_data[6 + xx] = int(offs[:4], 16)
            offs = offs[:2] + offs[4:]
    inject_data[10] = 0xC3
    windll.kernel32.WriteProcessMemory(h_gta, p_inject_func,                  \
                                       inject_data, 11, 0)
    h_thread = create_remote_thread(h_gta, 0, 0, p_inject_func, 0, 0, 0)
    wait_for_single_object(h_thread, 0xFFFFFFFF)
    close_handle(h_thread)
    return True


def update_scoreboard():
    global scoreboard_data
    if not check_handles():
        return 0
    if not refresh_scoreboard():
        return 0
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_players = read_dword(h_gta, dw_address + SAMP_PPOOL_PLAYER_OFFSET)
    w_id = read_mem(h_gta, dw_players + SAMP_SLOCALPLAYERID_OFFSET, 2)
    dw_ping = read_mem(h_gta, dw_players + SAMP_ILOCALPLAYERPING_OFFSET, 4)
    dw_score = read_mem(h_gta, dw_players + SAMP_ILOCALPLAYERSCORE_OFFSET, 4)
    dw_temp = read_mem(h_gta, dw_players +                                    \
                       SAMP_ISTRLEN_LOCALPLAYERNAME_OFFSET, 4)
    s_username = ''
    if dw_temp <= 0xF:
        s_username = read_string(h_gta, dw_players +                          \
                                 SAMP_SZLOCALPLAYERNAME_OFFSET, 16)
    else:
        dw_address = read_dword(h_gta, dw_players +                           \
                                SAMP_PSZLOCALPLAYERNAME_OFFSET)
        s_username = read_string(h_gta, dw_address, 25)
    scoreboard_data[w_id] = {'NAME' : s_username, 'ID' : w_id,                \
                   'PING' : dw_ping, 'SCORE' : dw_score, 'ISNPC' : 0}
    for i in range(SAMP_PLAYER_MAX):
        dw_remoteplayer = read_dword(h_gta, dw_players +                      \
                                     SAMP_PREMOTEPLAYER_OFFSET + i * 4)
        if dw_remoteplayer == 0:
            continue
        dw_ping = read_mem(h_gta, dw_remoteplayer + SAMP_IPING_OFFSET, 4)
        dw_score = read_mem(h_gta, dw_remoteplayer + SAMP_ISCORE_OFFSET, 4)
        dw_isnpc = read_mem(h_gta, dw_remoteplayer + SAMP_ISNPC_OFFSET, 4)
        dw_temp = read_mem(h_gta, dw_remoteplayer + SAMP_ISTRLENNAME_OFFSET, 4)
        s_username = ''
        if dw_temp <= 0xF:
            s_username = read_string(h_gta, dw_remoteplayer +                 \
                                     SAMP_SZPLAYERNAME_OFFSET, 16)
        else:
            dw_address = read_dword(h_gta, dw_remoteplayer +                  \
                                    SAMP_PSZPLAYERNAME_OFFSET)
            if dw_address == 0:
                return 0
            s_username = read_string(h_gta, dw_address, 25)
        scoreboard_data[i] = {'NAME' : s_username, 'ID' : i,                  \
                       'PING' : dw_ping, 'SCORE' : dw_score,                  \
                       'ISNPC' : dw_isnpc, 'MPOS' : [0, 0, 0]}
        dw_remoteplayer_data = read_dword(h_gta, dw_remoteplayer + 0xC)
        if dw_remoteplayer_data == 0:
            continue
        dw_address = read_dword(h_gta, dw_remoteplayer_data + 0x1E9)
        if dw_address:
            ix = read_mem(h_gta, dw_remoteplayer_data + 0x1E9, 4)
            iy = read_mem(h_gta, dw_remoteplayer_data + 0x1ED, 4)
            iz = read_mem(h_gta, dw_remoteplayer_data + 0x1F1, 4)
            scoreboard_data[i]['MPOS'] = [ix, iy, iz]
        dw_samp_actor = read_dword(h_gta, dw_remoteplayer_data + 0x0) #R1 0x0
        if dw_samp_actor == 0:
            continue
        f_hp = read_float(h_gta, dw_remoteplayer_data + 444)
        f_armr = read_float(h_gta, dw_remoteplayer_data + 440)
        scoreboard_data[i]['HP'] = f_hp
        scoreboard_data[i]['ARMOR'] = f_armr
        dw_ped = read_dword(h_gta, dw_samp_actor + 0x40)
        if dw_ped == 0:
            continue
        scoreboard_data[i]['PED'] = dw_ped
    return True


def get_stream_ids():
    id_data = []
    if not check_handles():
        return id_data
    if not refresh_scoreboard():
        return id_data
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_players = read_dword(h_gta, dw_address + SAMP_PPOOL_PLAYER_OFFSET)
    for i in range(SAMP_PLAYER_MAX):
        dw_remoteplayer = read_dword(h_gta, dw_players +                      \
                                     SAMP_PREMOTEPLAYER_OFFSET + i * 4)
        if dw_remoteplayer == 0:
            continue
        dw_remoteplayer_data = read_dword(h_gta, dw_remoteplayer + 0x0) #r1 0x0
        if dw_remoteplayer_data == 0:
            continue
        dw_samp_actor = read_dword(h_gta, dw_remoteplayer_data + 0x0) # r1 0x0
        if dw_samp_actor == 0:
            continue
        dw_ped = read_dword(h_gta, dw_samp_actor + 676)
        if dw_ped == 0:
            continue
        id_data.append(i)
    return id_data


def get_target_ped():
    if not check_handles():
        return -1
    dw_address = read_dword(h_gta, 0xB6F3B8)
    if dw_address == 0:
        return -1
    dw_address = read_dword(h_gta, dw_address + 0x79C)
    return dw_address


def get_id_by_ped(ped):
    if ped == -1 or not check_handles():
        return -1
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_players = read_dword(h_gta, dw_address + SAMP_PPOOL_PLAYER_OFFSET)
    for i in range(SAMP_PLAYER_MAX):
        dw_remoteplayer = read_dword(h_gta, dw_players +                      \
                                     SAMP_PREMOTEPLAYER_OFFSET + i * 4)
        if dw_remoteplayer == 0:
            continue
        dw_remoteplayer_data = read_dword(h_gta, dw_remoteplayer + 0xC)
        if dw_remoteplayer_data == 0:
            continue
        dw_samp_actor = read_dword(h_gta, dw_remoteplayer_data + 0x1C)
        if dw_samp_actor == 0:
            continue
        dw_ped = read_dword(h_gta, dw_samp_actor + 0x40)
        if dw_ped == ped:
            return i
    return -1


def get_ped_by_id(plid):
    if not check_handles():
        return -1
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_players = read_dword(h_gta, dw_address + SAMP_PPOOL_PLAYER_OFFSET)
    dw_remoteplayer = read_dword(h_gta, dw_players +                          \
                                 SAMP_PREMOTEPLAYER_OFFSET + plid * 4)
    dw_remoteplayer_data = read_dword(h_gta, dw_remoteplayer + 0xC)
    dw_samp_actor = read_dword(h_gta, dw_remoteplayer_data + 0x1C)
    return read_dword(h_gta, dw_samp_actor + 0x40)



def get_id_by_name(name):
    if not name or not check_handles():
        return -1
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_players = read_dword(h_gta, dw_address + SAMP_PPOOL_PLAYER_OFFSET)
    if name == get_username():
        return read_mem(h_gta, dw_players + SAMP_SLOCALPLAYERID_OFFSET, 2)
    for i in range(SAMP_PLAYER_MAX):
        dw_remoteplayer = read_dword(h_gta, dw_players +                      \
                                     SAMP_PREMOTEPLAYER_OFFSET + i * 4)
        dw_temp = read_mem(h_gta, dw_remoteplayer + SAMP_ISTRLENNAME_OFFSET, 4)
        s_username = ''
        if dw_temp <= 0xF:
            s_username = read_string(h_gta, dw_remoteplayer +                 \
                                     SAMP_SZPLAYERNAME_OFFSET, 16)
        else:
            dw_address = read_dword(h_gta, dw_remoteplayer +                  \
                                    SAMP_PSZPLAYERNAME_OFFSET)
            if dw_address == 0:
                continue
            s_username = read_string(h_gta, dw_address, 25)
        if s_username == name:
            return i
    return -1


def get_name_by_id(dw_id):
    if not check_handles():
        return ''
    if dw_id == -1:
        return get_username()
    if dw_id < 0 or dw_id > SAMP_PLAYER_MAX or not check_handles():
        return ''
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_players = read_dword(h_gta, dw_address + SAMP_PPOOL_PLAYER_OFFSET)
    dw_remoteplayer = read_dword(h_gta, dw_players +                          \
                                 SAMP_PREMOTEPLAYER_OFFSET + dw_id * 4)
    dw_temp = read_mem(h_gta, dw_remoteplayer + SAMP_ISTRLENNAME_OFFSET, 4)
    s_username = ''
    if dw_temp <= 0xF:
        s_username = read_string(h_gta, dw_remoteplayer +                     \
                                 SAMP_SZPLAYERNAME_OFFSET, 16)
    else:
        dw_address = read_dword(h_gta, dw_remoteplayer +                      \
                                SAMP_PSZPLAYERNAME_OFFSET)
        if dw_address == 0:
            return 0
        s_username = read_string(h_gta, dw_address, 25)
    return s_username


def get_lvl_by_id(dw_id):
    if dw_id < 0 or dw_id > SAMP_PLAYER_MAX or not check_handles():
        return -1
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_players = read_dword(h_gta, dw_address + SAMP_PPOOL_PLAYER_OFFSET)
    dw_remoteplayer = read_dword(h_gta, dw_players +                          \
                                 SAMP_PREMOTEPLAYER_OFFSET + dw_id * 4)
    dw_score = read_mem(h_gta, dw_remoteplayer + SAMP_ISCORE_OFFSET, 4)
    if dw_score == 0:
        refresh_scoreboard()
        dw_score = read_mem(h_gta, dw_remoteplayer + SAMP_ISCORE_OFFSET, 4)
    return dw_score


def get_ping_by_id(dw_id):
    if dw_id < 0 or dw_id > SAMP_PLAYER_MAX or not check_handles():
        return -1
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_players = read_dword(h_gta, dw_address + SAMP_PPOOL_PLAYER_OFFSET)
    dw_remoteplayer = read_dword(h_gta, dw_players +                          \
                                 SAMP_PREMOTEPLAYER_OFFSET + dw_id * 4)
    dw_ping = read_mem(h_gta, dw_remoteplayer + SAMP_IPING_OFFSET, 4)
    if dw_ping == 0:
        refresh_scoreboard()
        dw_ping = read_mem(h_gta, dw_remoteplayer + SAMP_IPING_OFFSET, 4)
    return dw_ping


def get_hp_by_id(dw_id):
    if dw_id < 0 or dw_id > SAMP_PLAYER_MAX or not check_handles():
        return -1
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_players = read_dword(h_gta, dw_address + SAMP_PPOOL_PLAYER_OFFSET)
    dw_remoteplayer = read_dword(h_gta, dw_players +                          \
                                 SAMP_PREMOTEPLAYER_OFFSET + dw_id * 4)
    if dw_remoteplayer == 0:
        return -1
    dw_remoteplayer_data = read_dword(h_gta, dw_remoteplayer + 0xC)
    if dw_remoteplayer_data == 0:
        return -1
    f_hp = read_float(h_gta, dw_remoteplayer_data + 444)
    return f_hp


def get_armor_by_id(dw_id):
    if dw_id < 0 or dw_id > SAMP_PLAYER_MAX or not check_handles():
        return -1
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_players = read_dword(h_gta, dw_address + SAMP_PPOOL_PLAYER_OFFSET)
    dw_remoteplayer = read_dword(h_gta, dw_players +                          \
                                 SAMP_PREMOTEPLAYER_OFFSET + dw_id * 4)
    if dw_remoteplayer == 0:
        return -1
    dw_remoteplayer_data = read_dword(h_gta, dw_remoteplayer + 0xC)
    if dw_remoteplayer_data == 0:
        return -1
    f_armr = read_float(h_gta, dw_remoteplayer_data + 440)
    return f_armr
        

def get_ped_in_vehicle(place):
    if not check_handles():
        return -1
    c_veh = read_dword(h_gta, ADDR_VEHICLE_PTR)
    if not c_veh:
        return -1
    return read_dword(h_gta, c_veh + 0x460 + (place * 4))


def get_player_color(dw_id):
    if not check_handles():
        return ''
    color = str(hex(read_dword(h_gta, dw_samp + SAMP_PLAYER_COLOR_OFFSET +    \
                               4 * dw_id)))[2:] #R1 0x216378, R2 +8
    for i in range(8 - len(color)):
        color = '0' + color
    color = color[:6]
    return color


def get_ped_coords(dw_ped):
    if not dw_ped:
        return 0
    dw_address = read_dword(h_gta, dw_ped + 0x14)
    f_x = read_float(h_gta, dw_address + 0x30)
    f_y = read_float(h_gta, dw_address + 0x34)
    f_z = read_float(h_gta, dw_address + 0x38)
    return [f_x, f_y, f_z]


def get_dist_by_ped_id(ped_id):
    player_coords = get_coordinates()
    char_coords = get_ped_coords(ped_id)
    dist = get_distance(player_coords, char_coords)
    return int(dist)
        

def water_drive(value = 0):
    if not check_handles():
        return False
    if value:
        write_mem(h_gta, 0x969151, 0x1)
    else:
        write_mem(h_gta, 0x969151, 0x0)
    return True


def get_skin_by_ped(ped):
    if not check_handles():
        return -1
    dw_addr = ped + ADDR_CPED_SKINIDOFF
    skin = read_mem(h_gta, dw_addr, 2)
    return skin


def full_deagle():
    if not check_handles():
        return -1
    write_mem(h_gta, 0xB7949C, 1000.0)
    return True
#0xB7949C


def get_last_input():
    if not check_handles():
        return ''
    dw_address = read_dword(h_gta, dw_samp + ADDR_SAMP_INPUT_PTR)
    msg = read_string(h_gta, dw_address + 0x1565, 128)
    return msg


def set_last_input(text = ''):
    if not check_handles():
        return ''
    dw_address = read_dword(h_gta, dw_samp + ADDR_SAMP_INPUT_PTR)
    msg = write_mem(h_gta, dw_address + 0x1565, text)
    return msg


def call(hprocess, dw_func, a_params, clean_stack = True, this_call = False):
    if not hprocess:
        return 0
    valid_params = 0
    i = len(a_params)
    dw_len = i * 5 + 5 + 1              # i * PUSH + CALL + RETN
    if clean_stack:
        dw_len += 3
    inject_data = (c_ubyte * (i * 5 + 5 + 3 + 1))()
    j = 1
    while i > 0:
        if a_params[i-1][0] != '':
            dw_address = 0x0
            if a_params[i-1][0] == 'p':
                dw_address = a_params[i-1][1]
            elif a_params[i-1][0] == 's':
                if j == 1:
                    dw_address = p_param1
                elif j == 2:
                    dw_address = p_param2
                elif j == 3:
                    dw_address = p_param3
                elif j == 4:
                    dw_address = p_param4
                else:
                    return False
                write_mem(hprocess, dw_address, a_params[i-1][1])
                j += 1
            elif a_params[i-1][0] == 'i':
                dw_address = a_params[i-1][1]
            elif a_params[i-1][0] == 'f':
                dw_address = int(float_to_hex(a_params[i-1][1]), 16)
            else:
                return False
            if this_call == True and i == 1:
                inject_data[valid_params * 5] = 0xB9
            else:
                inject_data[valid_params * 5] = 0x68
            inject_data[valid_params * 5 + 1] = byte_prepare(dw_address)[0]
            inject_data[valid_params * 5 + 2] = byte_prepare(dw_address)[1]
            inject_data[valid_params * 5 + 3] = byte_prepare(dw_address)[2]
            inject_data[valid_params * 5 + 4] = byte_prepare(dw_address)[3]
            valid_params += 1
        i = i - 1
    inject_data[valid_params * 5] = 0xE8 #9A - E8
    addr = dw_func - (p_inject_func + valid_params * 5 + 5)
    inject_data[valid_params * 5 + 1] = byte_prepare(addr)[0]
    inject_data[valid_params * 5 + 2] = byte_prepare(addr)[1]
    inject_data[valid_params * 5 + 3] = byte_prepare(addr)[2]
    inject_data[valid_params * 5 + 4] = byte_prepare(addr)[3]
    if clean_stack:
        inject_data[valid_params * 5 + 5] = 0x83
        inject_data[valid_params * 5 + 6] = 0xC4
        inject_data[valid_params * 5 + 7] = valid_params * 4
        inject_data[valid_params * 5 + 8] = 0xC3
    else:
        inject_data[valid_params * 5 + 5] = 0xC3
    windll.kernel32.WriteProcessMemory(h_gta, p_inject_func,                  \
                                       inject_data, dw_len, 0)
    h_thread = create_remote_thread(h_gta, 0, 0, p_inject_func, 0, 0, 0)
    wait_for_single_object(h_thread, 0xFFFFFFFF)
    close_handle(h_thread)
    return True


def update_text_labels():
    global text_labels
    if not check_handles():
        return False
    text_labels = {}
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_text_labels = read_dword(h_gta, dw_address + SAMP_POOL_TEXTLABEL)
    if not dw_text_labels:
        return False
    for i in range(SAMP_MAX_TEXTLABELS):
        if not read_dword(h_gta, dw_text_labels + (0xE800 + i * 4)):
            continue
        dw_address = read_dword(h_gta, dw_text_labels + i * 0x1D)
        if not dw_address:
            continue
        string = read_string(h_gta, dw_address, 256)
        if string == '':
            for i in range(4096):
                if not read_mem(h_gta, dw_address + i, 1):
                    offs = i
                    break
            string = read_string(h_gta, dw_address, offs)
        if string == '':
            continue
        fx = read_float(h_gta, dw_text_labels + (i * 0x1D + 0x8))
        fy = read_float(h_gta, dw_text_labels + (i * 0x1D + 0xC))
        fz = read_float(h_gta, dw_text_labels + (i * 0x1D + 0x10))
        vehid = read_mem(h_gta, dw_text_labels + (i * 0x1D + 0x1B), 2)
        plid = read_mem(h_gta, dw_text_labels + (i * 0x1D + 0x19), 2)
        vis = read_mem(h_gta, dw_text_labels + (i * 0x1D + 0x18), 1)
        dist = read_float(h_gta, dw_text_labels + (i * 0x1D + 0x14))
        text_labels[i] = {'Text' : string, 'Xpos' : fx, 'Ypos' : fy, \
                   'Zpos' : fz, 'VehID' : vehid, 'PlID' : plid, \
                   'Visible' : vis, 'Distance' : dist}
    return True


def create_text_label(text, color, xpos, ypos, zpos, draw_dist = 46.0,\
                      test_los = 0, player = 0xFFFF, vehicle = 0xFFFF):
    if not check_handles():
        return -1
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOL_TEXTLABEL)
    if not dw_address:
        return -1
    for i in range(SAMP_MAX_TEXTLABELS - 1):
        if read_dword(h_gta,dw_address + 0xE800 + (SAMP_MAX_TEXTLABELS - i)*4):
            continue
        ret = call(h_gta, dw_samp + FUNC_SAMP_CREATE_TEXTLABEL,               \
                                            [['i', dw_address],               \
                                             ["i", SAMP_MAX_TEXTLABELS - i],  \
                                             ["s", text], ["i", color],       \
                                             ["f", xpos], ["f", ypos],        \
                                             ["f", zpos], ["f", draw_dist],   \
                                             ["i", test_los], ["i", player],  \
                                             ["i", vehicle]], False, True)   
        if not ret:
            return -1
        return SAMP_MAX_TEXTLABELS - i
    return -1


def delete_text_label(tlid):
    if not check_handles() or tlid < 0:
        return -1
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOL_TEXTLABEL)
    if not call(h_gta, dw_samp + FUNC_SAMP_DELETE_TEXTLABEL,                  \
                [['i', dw_address], ['i', tlid]], False, True):
        return -1
    return tlid


def update_text_label(tlid, text):
    if not check_handles() or tlid < 0:
        return -1
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOL_TEXTLABEL)
    dw_address = read_dword(h_gta, dw_address + tlid * 0x1D)
    return write_mem(h_gta, dw_address, text)


def is_chat_open():
    if not check_handles():
        return -1
    dw_ptr = dw_samp + ADDR_SAMP_INCHAT_PTR
    dw_addr = read_dword(h_gta, dw_ptr)
    dw_addr = dw_addr + ADDR_SAMP_INCHAT_PTR_OFF
    dw_in_chat = read_dword(h_gta, dw_addr)
    if dw_in_chat > 0:
        return True
    else:
        return False


def get_chatlog_path():
    if not check_handles():
        return -1
    dw_address = read_dword(h_gta, dw_samp + ADDR_SAMP_CHATMSG_PTR)
    path = read_string(h_gta, dw_address + 0x11, 256)
    return path


def get_chatlog_line(line = 0):
    with open(get_chatlog_path()) as f:
        mylist = f.read().splitlines() 
        chatline = (line + 1) * -2
        last_line = mylist[chatline]
        return last_line[11:]


''' DIALOG FUNCTIONS BLOCK '''

def show_dialog(style, caption, text, button1, button2 = '', dlid = 1):
    if 0 > dlid > 32767 or 0 > style > 5 or len(caption) > 64 or              \
    len(text) > 4095 or len(button1) > 10 or len(button2) > 10 or             \
    not check_handles():
        return False
    return call(h_gta, dw_samp + FUNC_SAMP_SHOWDIALOG,                        \
                [["i", read_dword(h_gta, dw_samp + SAMP_DIALOG_STRUCT_PTR)],  \
                  ["i", dlid], ["i", style], ["s", caption], ["s", text],     \
                  ["s", button1], ["s", button2], ["i", 0]], False, True)


def is_dialog_open():
    if not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_DIALOG_STRUCT_PTR)
    is_open = read_mem(h_gta, dw_address + SAMP_DIALOG_OPEN_OFFSET, 4)
    if is_open:
        return True
    else:
        return False
    
    
def get_dialog_style():
    if not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_DIALOG_STRUCT_PTR)
    return read_mem(h_gta, dw_address + SAMP_DIALOG_STYLE_OFFSET, 4)


def get_dialog_id():
    if not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_DIALOG_STRUCT_PTR)
    return read_mem(h_gta, dw_address + SAMP_DIALOG_ID_OFFSET, 4)


def set_dialog_id(dlid):
    if not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_DIALOG_STRUCT_PTR)
    return write_mem(h_gta, dw_address + SAMP_DIALOG_ID_OFFSET, dlid, 'dword')


def get_dialog_caption():
    if not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_DIALOG_STRUCT_PTR)
    return read_string(h_gta, dw_address + SAMP_DIALOG_CAPTION_OFFSET, 64)


def get_dialog_text():
    if not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_DIALOG_STRUCT_PTR)
    dw_pointer = read_dword(h_gta, dw_address + SAMP_DIALOG_TEXT_PTR_OFFSET)
    text = read_string(h_gta, dw_pointer, 4096)
    if not text:
        for i in range(4096):
            if not read_mem(h_gta, dw_pointer + i, 1):
                offs = i
                break
        text = read_string(h_gta, dw_pointer, offs)
    return text


def get_dialog_line_count():
    if not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_DIALOG_STRUCT_PTR)
    dw_pointer = read_dword(h_gta, dw_address + SAMP_DIALOG_PTR2_OFFSET)
    return read_mem(h_gta, dw_pointer + SAMP_DIALOG_LINECOUNT_OFFSET, 4)


def get_dialog_selected_line():
    if not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_DIALOG_STRUCT_PTR)
    dw_pointer = read_dword(h_gta, dw_address + SAMP_DIALOG_PTR2_OFFSET)
    return read_mem(h_gta, dw_pointer + 0x143, 1) + 1


def set_dialog_selected_line(index):
    if not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_DIALOG_STRUCT_PTR)
    dw_pointer = read_dword(h_gta, dw_address + SAMP_DIALOG_PTR2_OFFSET)
    return write_mem(h_gta, dw_pointer + 0x143, index - 1, 1)


def is_dialog_button_selected(btn = 1):
    if not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_DIALOG_STRUCT_PTR)
    dw_pointer = read_dword(h_gta, dw_address + SAMP_DIALOG_PTR2_OFFSET)
    if btn == 1:
        offset = 0x165
    else:
        offset = 0x2C5
    return read_mem(h_gta, dw_pointer + offset, 1)


def close_dialog():
    if not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_DIALOG_STRUCT_PTR)
    return call(h_gta, dw_samp + FUNC_SAMP_CLOSEDIALOG, [['i', dw_address]],  \
         False, True)


def press_dialog_button(button = 1):
    if not check_handles() or 0 > button > 1:
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_DIALOG_STRUCT_PTR)
    return call(h_gta, dw_samp + FUNC_SAMP_PRESSBUTTON, [['i', dw_address],   \
                                                  ['i', button]], False, True)


def move_in_dialog(line, btn = 1):
    if not check_handles():
        return False
    timeout = time.time() + 3
    while True:
        if time.time() > timeout:
            break
        if is_dialog_open():
            set_dialog_selected_line(line)
            press_dialog_button(btn)
            return True
    return False


''' TEXT DRAW BLOCK '''

def update_text_draws():
    global text_draws
    text_draws = {}
    if not check_handles():
        return text_draws
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_txtdr = read_dword(h_gta, dw_address + SAMP_POOL_TEXTDRAW)
    if not dw_txtdr:
        return text_draws
    for i in range(SAMP_MAX_TEXTDRAWS - 1):
        if not read_dword(h_gta, dw_txtdr + (i * 4)):
            continue
        dw_address = read_dword(h_gta, dw_txtdr + (i * 4 +                    \
                        (4 * (SAMP_MAX_PLAYERTEXTDRAWS + SAMP_MAX_TEXTDRAWS))))
        if not dw_address:
            continue
        if not read_string(h_gta, dw_address, 800):
            continue
        text_draws.update({i : {'Text' : read_string(h_gta, dw_address, 800,  \
                            encoding = 'windows-1251'), 'Type' : 'Global'}})
    for i in range(SAMP_MAX_PLAYERTEXTDRAWS - 1):
        if not read_dword(h_gta, dw_txtdr + (i * 4) + SAMP_MAX_TEXTDRAWS * 4):
            continue
        dw_address = read_dword(h_gta, dw_txtdr + (i * 4 +                    \
                    (4 * (SAMP_MAX_PLAYERTEXTDRAWS + SAMP_MAX_TEXTDRAWS * 2))))
        if not dw_address:
            continue
        if not read_string(h_gta, dw_address, 800):
            continue
        text_draws.update({i : {'Text' : read_string(h_gta, dw_address, 800,  \
                            encoding = 'windows-1251'), 'Type' : 'Player'}})
    return text_draws


def create_text_draw(text, xPos, yPos, letterColor = 0xFFFFFFFF, font = 3,    \
            letterWidth = 0.4, letterHeight = 1, shadowSize = 0, outline = 1, \
            shadowColor = 0xFF000000, box = 0, boxColor = 0xFFFFFFFF,         \
            boxSizeX = 0.0, boxSizeY = 0.0, left = 0, right = 0, center = 1,  \
            proportional = 1, modelID = 0, xRot = 0.0, yRot = 0.0,            \
            zRot = 0.0, zoom = 1.0, color1 = 0xFFFF, color2 = 0xFFFF):
    if font > 5 or len(text) > 800 or not check_handles():
        return -1
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_txtdr = read_dword(h_gta, dw_address + SAMP_POOL_TEXTDRAW)
    if dw_txtdr == 0:
        return -1
    for i in range(2048):
        j = 2047 - i
        if read_dword(h_gta, dw_txtdr + j * 4):
            continue
        rstruct = (c_ubyte * 63)()
        params = 0
        if box:
            params += 1
        if left:
            params += 2
        if right:
            params += 4
        if center:
            params += 8
        if proportional:
            params += 16
        rstruct[0] = params
        rstruct[1] = byte_prepare(letterWidth, 'float')[0]
        rstruct[2] = byte_prepare(letterWidth, 'float')[1]
        rstruct[3] = byte_prepare(letterWidth, 'float')[2]
        rstruct[4] = byte_prepare(letterWidth, 'float')[3]
        rstruct[5] = byte_prepare(letterHeight, 'float')[0]
        rstruct[6] = byte_prepare(letterHeight, 'float')[1]
        rstruct[7] = byte_prepare(letterHeight, 'float')[2]
        rstruct[8] = byte_prepare(letterHeight, 'float')[3]
        rstruct[9] = byte_prepare(letterColor)[0]
        rstruct[10] = byte_prepare(letterColor)[1]
        rstruct[11] = byte_prepare(letterColor)[2]
        rstruct[12] = byte_prepare(letterColor)[3]
        rstruct[13] = byte_prepare(boxSizeX, 'float')[0]
        rstruct[14] = byte_prepare(boxSizeX, 'float')[1]
        rstruct[15] = byte_prepare(boxSizeX, 'float')[2]
        rstruct[16] = byte_prepare(boxSizeX, 'float')[3]
        rstruct[17] = byte_prepare(boxSizeY, 'float')[0]
        rstruct[18] = byte_prepare(boxSizeY, 'float')[1]
        rstruct[19] = byte_prepare(boxSizeY, 'float')[2]
        rstruct[20] = byte_prepare(boxSizeY, 'float')[3]
        rstruct[21] = byte_prepare(boxColor)[0]
        rstruct[22] = byte_prepare(boxColor)[1]
        rstruct[23] = byte_prepare(boxColor)[2]
        rstruct[24] = byte_prepare(boxColor)[3]
        rstruct[25] = shadowSize
        rstruct[26] = outline
        rstruct[27] = byte_prepare(shadowColor)[0]
        rstruct[28] = byte_prepare(shadowColor)[1]
        rstruct[29] = byte_prepare(shadowColor)[2]
        rstruct[30] = byte_prepare(shadowColor)[3]
        rstruct[31] = font
        rstruct[32] = 1
        rstruct[33] = byte_prepare(xPos, 'float')[0]
        rstruct[34] = byte_prepare(xPos, 'float')[1]
        rstruct[35] = byte_prepare(xPos, 'float')[2]
        rstruct[36] = byte_prepare(xPos, 'float')[3]
        rstruct[37] = byte_prepare(yPos, 'float')[0]
        rstruct[38] = byte_prepare(yPos, 'float')[1]
        rstruct[39] = byte_prepare(yPos, 'float')[2]
        rstruct[40] = byte_prepare(yPos, 'float')[3]
        rstruct[41] = byte_prepare(modelID, 'short')[0]
        rstruct[42] = byte_prepare(modelID, 'short')[1]
        rstruct[43] = byte_prepare(xRot, 'float')[0]
        rstruct[44] = byte_prepare(xRot, 'float')[1]
        rstruct[45] = byte_prepare(xRot, 'float')[2]
        rstruct[46] = byte_prepare(xRot, 'float')[3]
        rstruct[47] = byte_prepare(yRot, 'float')[0]
        rstruct[48] = byte_prepare(yRot, 'float')[1]
        rstruct[49] = byte_prepare(yRot, 'float')[2]
        rstruct[50] = byte_prepare(yRot, 'float')[3]
        rstruct[51] = byte_prepare(zRot, 'float')[0]
        rstruct[52] = byte_prepare(zRot, 'float')[1]
        rstruct[53] = byte_prepare(zRot, 'float')[2]
        rstruct[54] = byte_prepare(zRot, 'float')[3]
        rstruct[55] = byte_prepare(zoom, 'float')[0]
        rstruct[56] = byte_prepare(zoom, 'float')[1]
        rstruct[57] = byte_prepare(zoom, 'float')[2]
        rstruct[58] = byte_prepare(zoom, 'float')[3]
        rstruct[59] = byte_prepare(color1, 'short')[0]
        rstruct[60] = byte_prepare(color1, 'short')[1]
        rstruct[61] = byte_prepare(color2, 'short')[0]
        rstruct[62] = byte_prepare(color2, 'short')[1]
        if not windll.kernel32.WriteProcessMemory(h_gta, p_param5,            \
                                                  rstruct, len(rstruct), 0):
            return -1
        if not call(h_gta, dw_samp + SAMP_FUNC_TEXTDRAW, [["i", dw_txtdr],    \
                    ["i", j], ["i", p_param5], ["s", text]], False, True):
            return -1
        return j
    return -1


def set_text_draw(index, text):
    if not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_txtdr = read_dword(h_gta, dw_address + SAMP_POOL_TEXTDRAW)
    if not dw_txtdr:
        return False
    if not read_dword(h_gta, dw_txtdr + (index * 4 + SAMP_MAX_TEXTDRAWS * 4)):
        return False
    dw_address = read_dword(h_gta, dw_txtdr + (index * 4 + (4 *               \
                    (SAMP_MAX_PLAYERTEXTDRAWS + SAMP_MAX_TEXTDRAWS * 2))))
    if not dw_address:
        return False
    return write_mem(h_gta, dw_address, text)


def get_text_draw(index):
    if not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_txtdr = read_dword(h_gta, dw_address + SAMP_POOL_TEXTDRAW)
    if not dw_txtdr:
        return False
    if not read_dword(h_gta, dw_txtdr + (index * 4 + SAMP_MAX_TEXTDRAWS * 4)):
        return False
    dw_address = read_dword(h_gta, dw_txtdr + (index * 4 + (4 *               \
                    (SAMP_MAX_PLAYERTEXTDRAWS + SAMP_MAX_TEXTDRAWS * 2))))
    if not dw_address:
        return False
    return read_string(h_gta, dw_address, 100)


def delete_text_draw(index):
    if not check_handles() or 0 > index > SAMP_MAX_TEXTDRAWS - 1:
        return -1
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_txtdr = read_dword(h_gta, dw_address + SAMP_POOL_TEXTDRAW)
    if not call(h_gta, dw_samp + FUNC_SAMP_DELETE_TEXTDRAW,                   \
        [["i", dw_txtdr], ["i", index]], False, True):
        return -1
    return index
    

def get_text_draw_pos(tdid):
    pos = [-1, -1]
    if tdid < 0 or tdid > 2047 or not check_handles():
        return pos
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_txtdr = read_dword(h_gta, dw_address + SAMP_POOL_TEXTDRAW)
    dw_tdid = read_dword(h_gta, dw_txtdr + (tdid * 4 +                        \
                        (4 * (SAMP_MAX_PLAYERTEXTDRAWS + SAMP_MAX_TEXTDRAWS))))
    if dw_tdid == 0:
        dw_tdid = read_dword(h_gta, dw_txtdr + (tdid * 4 +                    \
                    (4 * (SAMP_MAX_PLAYERTEXTDRAWS + SAMP_MAX_TEXTDRAWS * 2))))
    if dw_tdid == 0:
        return pos
    pos[0] = read_float(h_gta, dw_tdid + 0x98B)
    pos[1] = read_float(h_gta, dw_tdid + 0x98F)
    return pos


def set_text_draw_pos(tdid, xpos, ypos):
    if tdid < 0 or tdid > 2047 or not check_handles():
        return False
    dw_address = read_dword(h_gta, dw_samp + SAMP_INFO_OFFSET)
    dw_address = read_dword(h_gta, dw_address + SAMP_POOLS)
    dw_txtdr = read_dword(h_gta, dw_address + SAMP_POOL_TEXTDRAW)
    dw_tdid = read_dword(h_gta, dw_txtdr + (tdid * 4 + (4 *                   \
                            (SAMP_MAX_PLAYERTEXTDRAWS + SAMP_MAX_TEXTDRAWS))))
    if dw_tdid == 0:
        dw_tdid = read_dword(h_gta, dw_txtdr + (tdid * 4 + (4 *               \
                        (SAMP_MAX_PLAYERTEXTDRAWS + SAMP_MAX_TEXTDRAWS * 2))))
    return write_mem(h_gta, dw_tdid + 0x98B, xpos, 'float')                   \
     and write_mem(h_gta, dw_tdid + 0x98F, ypos, 'float')

