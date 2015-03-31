all: inversion/build/P_0.pickle

inversion/build/originalVelocity.pickle:
	python src/createVelocity.py

inversion/build/stations.pickle: inversion/build/originalVelocity.pickle
	python src/createStations.py --nbStations 25 --randomSeed 10 --velocity \
	inversion/build/originalVelocity.pickle --buffer 0.05 --output \
	inversion/build/stations.pickle

inversion/build/events.pickle: inversion/build/originalVelocity.pickle
	python src/createEvents.py --nbEvents 100 --randomSeed 100 --velocity \
	inversion/build/originalVelocity.pickle --buffer 0.05 --output \
	inversion/build/events.pickle

inversion/build/P_0.pickle: inversion/build/stations.pickle inversion/build/events.pickle
	python src/calculatett.py --velocity inversion/build/originalVelocity.pickle \
	--rname inversion/build/P_ --eventFile inversion/build/events.pickle \
	--stationFile inversion/build/stations.pickle 
