# mmMBop

View MBtiles on localhost

python implementation of [mbview](https://github.com/mapbox/mbview)

Tested with python `2.7.10` and `3.5.1`

![example2](https://raw.githubusercontent.com/l-r/mmmbop/master/screenshots/mbtile.png)

## Installation

```bash
git clone https://github.com/l-r/mmmbop.git
cd mmmbop
pip install -r requirements.txt
```

## Usage

#### To view a single file

`python mmmbop/cli.py data/baja-highways.mbtiles`

#### To view multiple files

`python mmmbop/cli.py data/baja-highways.mbtiles data/another_file.mbtiles`

#### To view all .mbfiles in the current directory (non-recursive)

`python mmmbop/cli.py`


#### Warning & disclaimer

Please don't use this on anything else than a development machine. Debug options are on and there is a CORS wrapper on the entire app to allow cross-origin requests.