import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin 


class TestBitCoin(TestCase):

    @patch('bitcoin.get_bitcoin_data')
    def test_convert_dollars(self, mock_bitcoin_api):

        mock_bitcoin_api.return_value = {"time":{"updated":"Nov 19, 2020 22:00:00 UTC",
            "updatedISO":"2020-11-19T22:00:00+00:00",
            "updateduk":"Nov 19, 2020 at 22:00 GMT"},
            "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin",
            "bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"17,962.7805","description":"United States Dollar","rate_float":17962.7805},
            "GBP":{"code":"GBP","symbol":"&pound;","rate":"13,532.0990","description":"British Pound Sterling","rate_float":13532.099},
            "EUR":{"code":"EUR","symbol":"&euro;","rate":"15,121.6075","description":"Euro","rate_float":15121.6075}}}


        expected_dollars = 1796278.05
        dollars = bitcoin.convert_bitcoin_to_dollars(100)
        self.assertEqual(expected_dollars, dollars)
        
    @patch('bitcoin.get_bitcoin_data')
    def test_convert_bitcoin_to_their_value(self,mock_get_get_bitcoin_data):
        mock_get_get_bitcoin_data.return_value = {'bpi': {'EUR': {'code': 'EUR',
                 'description': 'Euro',
                 'rate': '26,104.2715',
                 'rate_float': 26104.2715,
                 'symbol': '&euro;'},
         'GBP': {'code': 'GBP',
                 'description': 'British Pound Sterling',
                 'rate': '22,391.4285',
                 'rate_float': 22391.4285,
                 'symbol': '&pound;'},
         'USD': {'code': 'USD',
                 'description': 'United States Dollar',
                 'rate': '26,797.0833',
                 'rate_float': 26797.0833,
                 'symbol': '&#36;'}},
 'chartName': 'Bitcoin',
 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index '
               '(USD). Non-USD currency data converted using hourly conversion '
               'rate from openexchangerates.org',
 'time': {'updated': 'Oct 12, 2023 00:44:00 UTC',
          'updatedISO': '2023-10-12T00:44:00+00:00',
          'updateduk': 'Oct 12, 2023 at 01:44 BST'}}
        
        bitcoin_dummy_amount = 11
        
        expected_value_dollar  = 294767.9163
        
        actual_dollar = bitcoin.convert_bitcoin_to_dollars(bitcoin_dummy_amount)
        
        
        self.assertEqual(expected_value_dollar, actual_dollar)
        


if __name__ == '__main__':
    unittest.main()