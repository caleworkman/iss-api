# iss-api
Command line tool to get information about the ISS from http://api.open-notify.org/.

## Usage
The tool will prompt you for input or you may supply it in the command line. Available function names are `loc`, `pass`, and `people`.

    > iss-api.py
    Please supply a function name.

### Get the current location of the ISS
    > iss-api.py loc
    The ISS current location at 2020-07-23 00:26:31.864122 is (-50.0239, 53.1447).

### Get overhead passing times and durations for a location
Pass a latitude and a longitude.

    > iss-api.py pass 10 20
    The ISS will be overhead at (10, 20) at 08:36:00 on 07/23/2020 for 91 seconds.
    The ISS will be overhead at (10, 20) at 10:07:49 on 07/23/2020 for 650 seconds.
    The ISS will be overhead at (10, 20) at 11:47:12 on 07/23/2020 for 349 seconds.
    The ISS will be overhead at (10, 20) at 20:03:36 on 07/23/2020 for 560 seconds.
    The ISS will be overhead at (10, 20) at 21:39:56 on 07/23/2020 for 595 seconds.

### Get people in space
Print all the people in space on board each craft.

    > iss-api.py people
    People on the ISS: Chris Cassidy, Anatoly Ivanishin, Ivan Vagner, Doug Hurley, Bob Behnken
