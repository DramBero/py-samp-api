# py-SAMP-api

A pure Python 3.X API for SA:MP client (0.3.7 R1)

## Function description
### Main functions block
**get_player_hp()** - returns local player's HP as a float.

**get_player_armor()** - returns local player's armor as a float.

**get_coordinates()** - returns local player's coordinates as a list of floats (x, y, z).

**get_red_marker()** - returns the coordinates of the red marker (the big red transparent cylinder-thingy).

**get_distance(coords1, coords2)** - accepts two vectors as arrays of three floats, returns the distance between them as a float.

**get_player_money()** - returns local player's money as an integer.

**get_player_skin()** - returns local player's skin ID as an integer.

**get_player_wanted()** - returns local player's wanted level as an integer.

**get_player_weapon()** - returns local player's weapon ID as an integer.

**get_resolution()** - returns game resolution as a list of two integers.

**is_player_in_vehicle()** - returns True (boolean) if the local player is in a vehicle and False (boolean) if he is not.

**is_player_driver()** - returns True (boolean) if the local player is in the vehicles driver seat and False (boolean) if he is not.

**get_vehicle_health()** - returns the used vehicle health as a float.

**get_vehicle_id()** - returns the used vehicle ID as an integer.

**get_vehicle_lights()** - returns the state of used vehicle's lights as a boolean.

**get_vehicle_engine()** - returns the state of used vehicle's engine as a boolean.

**get_vehicle_siren()** - returns the state of used vehicle's siren as a boolean.

**get_vehicle_lock()** - returns the state of used vehicle's lock as a boolean.

**get_vehicle_color()** - returns the used vehicle's primary color ID as an integer.

**get_vehicle_color2()** - returns the used vehicle's secondary color ID as an integer.

**get_vehicle_speed()** - returns the used vehicle's speed as a float.

**get_player_radio()** - returns the used vehicle's chosen radio station ID as an integer.

**get_radio_name(rad_id)** - accepts radio station ID as an integer. Returns radio station name as a string.

**get_player_state()** - returns the local player's state ID as an integer.

**on_state(state)** - accepts a state ID. Returns a boolean that shows if the local player has that state.

**is_player_in_menu()** - returns a boolean that shows if the local player is in the game menu.

**get_menu_map_data()** - returns local player's map data (x, y, zoom) as a list of floats.

**get_vehicle_plate()** - returns the used vehicle's plate as a string.

**toggle_night_vision()** - toggles the night vision mode.

**toggle_thermal_vision()** - toggles the thermal vision mode.

**set_time(hour)** - sets the local player's time (hour) to the accepted integer.

**hp_patch()** - toggles the clients HP patch.

**set_player_health(hp)** - sets local player's HP to the accepted integer.

**set_player_armor(hp)** - sets local player's armor to the accepted integer.

**set_vehicle_health(hp)** - sets used vehicle HP to the accepted integer.

**toggle_anti_bikefall(tog = -1)** - if tog is 1 or True - turns on the anti-bikefall patch, else - disables it.

**anti_crash()** - turns on the anti-crash patch.

**print_low(text, time)** - accepts a string and an integer. Shows the string as a GTA-hardcoded text to the specified amount of time.

**get_chat_line_ex(line = 0)** - accepts an integer. Returns the chat line (reads it from memory) as a string. 0 - is the last chat line, and so on.

**set_chat_line_ex(text, line = 0)** accepts a string and an integer. Sets the specified chat line to the accepted string. 0 - is the last chat line, and so on.

**get_chat_line_color(line = 0)** - accepts an integer. Returns the chat line color as an integer (hex-coded color). 0 - is the last chat line, and so on.

**get_chat_line_timestamp(line = 0, unix = False)** - accepts an integer and a boolean. Gets the timestamp of the specified line. 0 - is the last chat line, and so on. If "unix" is set to True - returns the unix-timestamp without the converting.

**get_mem_chatlog()** - prints the full memory chatlog to the python console. Used only for testing.

**add_chat_message(wtext, color = 'FFFFFF', timestamp = True)** - accepts a string for the message text, a string for the hex-coded color of the message, and a boolean for toggling of the message's timestamp. Adds a chat line that only the local player can see.

**send_chat(wtext)** - accepts a string. Sends the string as a chat input.

**show_game_text(text, time, size)** - accepts a string, and two integers. Shows the hardcoded GTA text for a specfied amount of time.

**refresh_scoreboard()** - refreshes the scoreboard (Tab).

**update_scoreboard()** - creates a dictionary with the scoreboard data.

**get_stream_ids()** - returns a list with player ID's in the streamable zone.

**get_target_ped()** - returns ID of the targeted ped as an integer.

**get_id_by_ped(ped)** - accepts an integer. Returns player ID of the ped ID as an integer.

**get_ped_by_id(plid)** - accepts an integer. Returns ped ID of the streamable player ID as an integer.

**get_id_by_name(name)** - accepts a string. Returns player ID of the player name as an integer.

**get_name_by_id(dw_id)** - accepts an integer. Returns player name of the player ID as a string.

**get_lvl_by_id(dw_id)** - accepts an integer. Returns player score (level) of the player ID as an integer.

**get_ping_by_id(dw_id)** - accepts an integer. Returns player ping of the player ID as an integer.

**get_hp_by_id(dw_id)** - accepts an integer. Returns player HP of the streamable player ID as an integer.

**get_armor_by_id(dw_id)** - accepts an integer. Returns player armor of the streamable player ID as an integer.

*Will write down the rest of the functions from the source code in the later updates.*

## Authors

* **DramBero (Teodoro_Bagwell)** - *Reworking of the most commonly used SAMP-client API functions to Python, finding some of the offsets.* - [DramBero](https://github.com/DramBero)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* The Autohotkey SAMP-UDF contributors, whose offsets and most of the functions I used as a base: Chuck_Floyd, Suchty112, paul-phoenix, Agrippa1994, RawDev, ELon, democrazy, MurKotik, McFree, aknqkzxlcs, Godarck, Слюнявчик, MrGPro, Phoenixxx_Czar, Dworkin, Ghost29, slavawar, Artur_iOS, ByNika.
* The Autohotkey and C++ SAMP API contributors, whose offsets and some of the functions I used as a base: Agrippa1994, MarcelGerber.
