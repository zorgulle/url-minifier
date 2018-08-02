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
 * Add mysql and pgsql db support