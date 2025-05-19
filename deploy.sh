#!/bin/sh
USERNAME=karroyoohori

jekyll build
rsync --delete -pthrvz --group ./_site/ ${USERNAME}@geomatics01.bk.tudelft.nl:/var/www/courses/geo2021/
ssh ${USERNAME}@geomatics01.bk.tudelft.nl "chown -R karroyoohori:www-data /var/www/courses/geo2021/*; chmod -R 755 /var/www/courses/geo2021/*"