import logging

from freqtrade.exchange import Exchange
from freqtrade.exchange.exchange_types import FtHas


logger = logging.getLogger(__name__)


class Alpaca(Exchange):
    """
    Alpaca exchange class. Contains adjustments needed for Freqtrade to work
    with this exchange.

    Only Alpaca's crypto markets are supported (spot, USD-quoted pairs).
    Crypto orders support "GTC" and "IOC" time in force only, and stop orders
    are limited to stop_limit - so `stoploss_on_exchange` is not supported.
    """

    _ft_has: FtHas = {
        "order_time_in_force": ["GTC", "IOC"],  # alpaca crypto: no FOK/PO
    }
