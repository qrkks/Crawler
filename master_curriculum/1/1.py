from ..log import log_conifg

logger = log_conifg.setup_logging(__name__)



logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')