NPROCESS = 4
SITE_DIR = /Users/jpmercier/git-projects/estuary/src/estuaire/site_scons

all : .PHONY

.PHONY :
	scons --site-dir=${SITE_DIR} -j${NPROCESS}

tree :
	scons --site-dir=${SITE_DIR} --tree=all

clean :
	scons --site-dir=${SITE_DIR} -c
	#rm -rf ./build -
