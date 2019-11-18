# CrateDB bulk insert benchmark

An experimental project, benchmarking bulk importing data into CrateDB.

## Prerequisites

You will need Python 3 and virtualenv.

## Setup

Set up your environment and install the dependencies like this:

```
    $ virtualenv -p python3 env
    $ source ./env/bin/activate
    $ ./env/bin/pip install -r requirements.txt
```

## Run

1. First, please launch the crate db server: `./crate_up.sh`.
1. After the db has been successfully launched and is ready, launch the benchmark in a sepparate terminal session: `./env/bin/python benchmark.py`.

## Output

```
↓ Preparing benchmark! Downloading fixtures...
✓ Done! Fixtures can be found under '/Users/teo/crate-bench/fixtures'!

================ CRATEDB BULK INSERT BENCHMARK ======================


 ◎ Importing /Users/teo/crate-bench/fixtures/transfers.txt into 'transfers'...
 ◎ 100963 'transfers' imported in 20.61 seconds!

 ◎ Importing /Users/teo/crate-bench/fixtures/agency.txt into 'agencies'...
 ◎ 41 'agencies' imported in 0.07 seconds!

 ◎ Importing /Users/teo/crate-bench/fixtures/calendar_dates.txt into 'calendar_dates'...
 ◎ 9438 'calendar_dates' imported in 0.98 seconds!

 ◎ Importing /Users/teo/crate-bench/fixtures/stop_times.txt into 'stop_times'...
 ◎ 3419699 'stop_times' imported in 188.05 seconds!

 ◎ Importing /Users/teo/crate-bench/fixtures/frequencies.txt into 'frequencies'...
 ◎ 0 'frequencies' imported in 0.01 seconds!

 ◎ Importing /Users/teo/crate-bench/fixtures/shapes.txt into 'shapes'...
 ◎ 4560365 'shapes' imported in 193.54 seconds!

 ◎ Importing /Users/teo/crate-bench/fixtures/trips.txt into 'trips'...
 ◎ 156754 'trips' imported in 7.31 seconds!

 ◎ Importing /Users/teo/crate-bench/fixtures/stops.txt into 'stops'...
 ◎ 41645 'stops' imported in 2.45 seconds!

 ◎ Importing /Users/teo/crate-bench/fixtures/calendar.txt into 'calendar'...
 ◎ 1410 'calendar' imported in 0.11 seconds!

 ◎ Importing /Users/teo/crate-bench/fixtures/routes.txt into 'routes'...
 ◎ 1279 'routes' imported in 0.09 seconds!


================ AWWW YES! DONE IN 413.23 SECONDS! (⌐■_■) ===============
```
