import glob
import sys
import logging


def parse_args(arguments, app):
    sources = arguments.get('<mbfile>')
    if not sources:
        files = glob.glob("*.mbtiles")
        if not files:
            logging.error('Could not find any .mbtiles in this directory. Please specify an .mbtiles file.')
            sys.exit(1)

        app.config['sources'] = files
    else:
        app.config['sources'] = sources
