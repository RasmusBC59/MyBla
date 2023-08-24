import logging
import mybla._version


__version__ = mybla._version.__version__



logger = logging.getLogger(__name__)
logger.info(f'Imported myblaversion: {__version__}')
