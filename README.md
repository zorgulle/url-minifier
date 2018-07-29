# url-minifier
Minify url
Deminify them

Pre requis create a DB
Bind the DB

Method used is base64 of encoding the url id

#Use
##minify
python app.py --url www.test.com --action minify
==> QW2x

##deminify
python app.py --url QW2x --action deminify
==> www.text.com

#TODO
 * Add config file to handle db name connection
 method and so on
 * Refacto the way the engine is made
 * Add more Strategy of encoding
 * Add mysql and pgsql db support