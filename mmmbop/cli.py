"""mmMBop

Usage:
  cli.py
  cli.py <mbfile>...
  cli.py (-h | --help)
  cli.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from MBTile import MBTile
from MBTilesMetadata import MBTilesMetadata
from flask import Flask, render_template, Response
from flask_cors import CORS
from docopt import docopt
import json
import util
import config
app = Flask(__name__)
CORS(app)


@app.route("/")
def main():
    mb_tiles_metadata = MBTilesMetadata(app.config['sources'])
    md = mb_tiles_metadata.get_metadata()

    return render_template('map.html', metadata=json.dumps(md))


@app.route("/get_tiles/<int:src_index>/<int:z>/<int:x>/<int:y>")
def get_tiles(src_index, z, x, y):
    source = app.config['sources'][src_index]
    tile = MBTile(source, z, x, y)
    data = tile.get_data()

    resp = Response(data)
    resp.headers['Content-type'] = 'application/x-protobuf'
    resp.headers['Content-Encoding'] = 'gzip'

    return resp


def serve():
    options = docopt(__doc__, version='{} {}'.format(config.name, config.version))
    util.parse_args(options, app)

    app.run(debug=True)

if __name__ == "__main__":
    serve()
