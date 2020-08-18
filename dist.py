import pathlib
import argparse
from tqdm import tqdm
from PIL import Image
from lxml import etree, HTML

parser = argparse.ArgumentParser(description = 'Distribute emojis into various sizes and generate README')
parser.add_argument(
  '-c', '--config', 
  metavar = 'PATH', 
  help = 'path to the config file',
  action = 'store',
  required = True
)
parser.add_argument(
  '--debug', 
  metavar = 'FUNCTION', 
  help = 'run specific debug program',
  action = 'store'
)
switches = parser.add_argument_group('switches', 'Choose what to generate  * NOTE: the default is to generate both emojis and README')
switches.add_argument(
  '-e', '--gen-emoji',
  help = 'generate emojis',
  action = 'store_true'
)
switches.add_argument(
  '-e', '--gen-readme',
  help = 'generate README',
  action = 'store_true'
)

args = parser.parse_args()