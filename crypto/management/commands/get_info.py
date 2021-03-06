from django.core.management.base import BaseCommand
from crypto.models import CryptoCurrency
import time

from pycoingecko import CoinGeckoAPI


class Command(BaseCommand):
    help = 'Get info about cryptocurrency'

    def handle(self, *args, **kwargs):
        cg = CoinGeckoAPI()
        while True:
            info_rate = cg.get_price(ids='bitcoin,litecoin,ethereum,tether,ripple,dogecoin,solana,monero,bowscoin,travala',
                                 vs_currencies=['usd', 'eur'])
            for crypt, values in info_rate.items():
                record = CryptoCurrency(title=crypt, usd_rate=values['usd'], eur_rate=values['eur'])
                record.save()
            time.sleep(3600)








