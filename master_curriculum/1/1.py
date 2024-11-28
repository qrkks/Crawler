import sys
import os
from pathlib import Path
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(str(Path(__file__).parent.parent))  # noqa
from log import log_conifg  # noqa

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(Path(__file__).parent.parent)

logger = log_conifg.setup_logging(__name__)


logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')


logger.debug(__file__)
logger.debug(Path(__file__)/'a')
logger.debug(Path(__file__).resolve())
logger.debug(type(Path(__file__).resolve()))
logger.debug(Path(__file__).parent)
logger.debug(type(Path(__file__).parent))
logger.debug(Path('1.py'))
logger.debug(Path('1.py').resolve())
