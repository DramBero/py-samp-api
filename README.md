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

*Will write down the rest of the functions from the source code in the later updates.*

## Authors

* **DramBero (Teodoro_Bagwell)** - *Reworking of the most commonly used SAMP-client API functions to Python, finding some of the offsets.* - [DramBero](https://github.com/DramBero)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* The Autohotkey SAMP-UDF contributors, whose offsets and most of the functions I used as a base: Chuck_Floyd, Suchty112, paul-phoenix, Agrippa1994, RawDev, ELon, democrazy, MurKotik, McFree, aknqkzxlcs, Godarck, Слюнявчик, MrGPro, Phoenixxx_Czar, Dworkin, Ghost29, slavawar, Artur_iOS, ByNika
* The Autohotkey and C++ SAMP API contributors, whose offsets and some of the functions I used as a base: Agrippa1994, MarcelGerber.
