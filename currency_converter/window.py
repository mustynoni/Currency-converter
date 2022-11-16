from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.uic import loadUi
from .helper import get_exchange_rates
from requests.exceptions import ConnectionError as RequestsConnectionError
import subprocess


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.rates = {}

        try:
            url = 'http://data.fixer.io/api/latest?access_key=df40c22735c1047c1fb330798103cd30'
            rates_file = './rates.json'
            self.rates = get_exchange_rates(url, rates_file)['rates']
        except RequestsConnectionError:
            self.uic = loadUi('./gui/error.ui', self)
            self.buttonBox.rejected.connect(self.cancel_error)
            self.buttonBox.accepted.connect(self.retry_error)
        else:
            self.uic = loadUi('./gui/cex.ui', self)
            # fill the combobox
            self._fill_combobox()
            # set up event handlers
            self.pushButton_3.clicked.connect(self.convert)
            self.pushButton_2.clicked.connect(self.swap)
            self.pushButton.clicked.connect(self.openin)
            self.actionYoruba.triggered.connect(self.Yoruba_lang)  #
            self.actionIgbo.triggered.connect(self.Igbo_lang)  #
            self.actionHausa.triggered.connect(self.Hausa_lang)  #
            self.actionEnglish.triggered.connect(self.English_lang)  #
            lang = 'will be'

    def convert(self) -> None:
        from_iso_code = self.comboBox.currentText()[0:3]
        to_iso_code = self.comboBox_2.currentText()[0:3]
        amount = self.doubleSpinBox.value()
        from_rate = self.rates[from_iso_code]
        to_rate = self.rates[to_iso_code]
        result = (to_rate / from_rate) * amount
        result = round(result, 3)
        result = '{:,}'.format(result)
        # output the result
        self.doubleSpinBox_2.setText(result)
##################################################################################
        story = str(amount)+' '+str(self.comboBox.currentText())+' = '+str(result)+' in '+str(self.comboBox_2.currentText())
        self.label_3.setText(story)#
        #self.label_3.adjustsize()
##################################################################################

    def cancel_error(self) -> None:
        self.close()

    def retry_error(self) -> None:
        self.close()
        subprocess.call(['python', './main.py'])

    def swap(self) -> None:
        from_index = self.comboBox.currentIndex()
        to_index = self.comboBox_2.currentIndex()
        self.comboBox_2.setCurrentIndex(from_index)
        self.comboBox.setCurrentIndex(to_index)

    def _fill_combobox(self) -> None:
        currency = [
            'AED - United Arab Emirates Dirham',
            'AFN - Afghan Afghani',
            'ALL - Albanian Lek',
            'AMD - Armenian Dram',
            'ANG - Netherlands Antillean Guilder',
            'AOA - Angolan Kwanza',
            'ARS - Argentine Peso',
            'AUD - Australian Dollar',
            'AWG - Aruban Florin',
            'AZN - Azerbaijani Manat',
            'BAM - Bosnia-Herzegovina Convertible Mark',
            'BBD - Barbadian Dollar',
            'BDT - Bangladeshi Taka',
            'BGN - Bulgarian Lev',
            'BHD - Bahraini Dinar',
            'BIF - Burundian Franc',
            'BMD - Bermudan Dollar',
            'BND - Brunei Dollar',
            'BOB - Bolivian Boliviano',
            'BRL - Brazilian Real',
            'BSD - Bahamian Dollar',
            'BTC - Bitcoin',
            'BTN - Bhutanese Ngultrum',
            'BWP - Botswanan Pula',
            'BYN - New Belarusian Ruble',
            'BYR - Belarusian Ruble',
            'BZD - Belize Dollar',
            'CAD - Canadian Dollar',
            'CDF - Congolese Franc',
            'CHF - Swiss Franc',
            'CLF - Chilean Unit of Account (UF)',
            'CLP - Chilean Peso',
            'CNY - Chinese Yuan',
            'COP - Colombian Peso',
            'CRC - Costa Rican Colón',
            'CUC - Cuban Convertible Peso',
            'CUP - Cuban Peso',
            'CVE - Cape Verdean Escudo',
            'CZK - Czech Republic Koruna',
            'DJF - Djiboutian Franc',
            'DKK - Danish Krone',
            'DOP - Dominican Peso',
            'DZD - Algerian Dinar',
            'EGP - Egyptian Pound',
            'ERN - Eritrean Nakfa',
            'ETB - Ethiopian Birr',
            'EUR - Euro',
            'FJD - Fijian Dollar',
            'FKP - Falkland Islands Pound',
            'GBP - British Pound Sterling',
            'GEL - Georgian Lari',
            'GGP - Guernsey Pound',
            'GHS - Ghanaian Cedi',
            'GIP - Gibraltar Pound',
            'GMD - Gambian Dalasi',
            'GNF - Guinean Franc',
            'GTQ - Guatemalan Quetzal',
            'GYD - Guyanaese Dollar',
            'HKD - Hong Kong Dollar',
            'HNL - Honduran Lempira',
            'HRK - Croatian Kuna',
            'HTG - Haitian Gourde',
            'HUF - Hungarian Forint',
            'IDR - Indonesian Rupiah',
            'ILS - Israeli New Sheqel',
            'IMP - Manx pound',
            'INR - Indian Rupee',
            'IQD - Iraqi Dinar',
            'IRR - Iranian Rial',
            'ISK - Icelandic Króna',
            'JEP - Jersey Pound',
            'JMD - Jamaican Dollar',
            'JOD - Jordanian Dinar',
            'JPY - Japanese Yen',
            'KES - Kenyan Shilling',
            'KGS - Kyrgystani Som',
            'KHR - Cambodian Riel',
            'KMF - Comorian Franc',
            'KPW - North Korean Won',
            'KRW - South Korean Won',
            'KWD - Kuwaiti Dinar',
            'KYD - Cayman Islands Dollar',
            'KZT - Kazakhstani Tenge',
            'LAK - Laotian Kip',
            'LBP - Lebanese Pound',
            'LKR - Sri Lankan Rupee',
            'LRD - Liberian Dollar',
            'LSL - Lesotho Loti',
            'LTL - Lithuanian Litas',
            'LVL - Latvian Lats',
            'LYD - Libyan Dinar',
            'MAD - Moroccan Dirham',
            'MDL - Moldovan Leu',
            'MGA - Malagasy Ariary',
            'MKD - Macedonian Denar',
            'MMK - Myanma Kyat',
            'MNT - Mongolian Tugrik',
            'MOP - Macanese Pataca',
            'MRO - Mauritanian Ouguiya',
            'MUR - Mauritian Rupee',
            'MVR - Maldivian Rufiyaa',
            'MWK - Malawian Kwacha',
            'MXN - Mexican Peso',
            'MYR - Malaysian Ringgit',
            'MZN - Mozambican Metical',
            'NAD - Namibian Dollar',
            'NGN - Nigerian Naira',
            'NIO - Nicaraguan Córdoba',
            'NOK - Norwegian Krone',
            'NPR - Nepalese Rupee',
            'NZD - New Zealand Dollar',
            'OMR - Omani Rial',
            'PAB - Panamanian Balboa',
            'PEN - Peruvian Nuevo Sol',
            'PGK - Papua New Guinean Kina',
            'PHP - Philippine Peso',
            'PKR - Pakistani Rupee',
            'PLN - Polish Zloty',
            'PYG - Paraguayan Guarani',
            'QAR - Qatari Rial',
            'RON - Romanian Leu',
            'RSD - Serbian Dinar',
            'RUB - Russian Ruble',
            'RWF - Rwandan Franc',
            'SAR - Saudi Riyal',
            'SBD - Solomon Islands Dollar',
            'SCR - Seychellois Rupee',
            'SDG - Sudanese Pound',
            'SEK - Swedish Krona',
            'SGD - Singapore Dollar',
            'SHP - Saint Helena Pound',
            'SLL - Sierra Leonean Leone',
            'SOS - Somali Shilling',
            'SRD - Surinamese Dollar',
            'STD - São Tomé and Príncipe Dobra',
            'SVC - Salvadoran Colón',
            'SYP - Syrian Pound',
            'SZL - Swazi Lilangeni',
            'THB - Thai Baht',
            'TJS - Tajikistani Somoni',
            'TMT - Turkmenistani Manat',
            'TND - Tunisian Dinar',
            'TOP - Tongan Paʻanga',
            'TRY - Turkish Lira',
            'TTD - Trinidad and Tobago Dollar',
            'TWD - New Taiwan Dollar',
            'TZS - Tanzanian Shilling',
            'UAH - Ukrainian Hryvnia',
            'UGX - Ugandan Shilling',
            'USD - United States Dollar',
            'UYU - Uruguayan Peso',
            'UZS - Uzbekistan Som',
            'VEF - Venezuelan Bolívar Fuerte',
            'VND - Vietnamese Dong',
            'VUV - Vanuatu Vatu',
            'WST - Samoan Tala',
            'XAF - CFA Franc BEAC',
            'XAG - Silver (troy ounce)',
            'XAU - Gold (troy ounce)',
            'XCD - East Caribbean Dollar',
            'XDR - Special Drawing Rights',
            'XOF - CFA Franc BCEAO',
            'XPF - CFP Franc',
            'YER - Yemeni Rial',
            'ZAR - South African Rand',
            'ZMK - Zambian Kwacha (pre-2013)',
            'ZMW - Zambian Kwacha',
            'ZWL - Zimbabwean Dollar'
        ]
        # set the currency for both combo boxes
        for x in currency:
            self.comboBox.addItem(x)
            self.comboBox_2.addItem(x)
#######################################################################################
    def English_lang(self):  #
        self.label.setText('Base currency')
        self.label_2.setText('Quote Currency')
        self.pushButton_2.setText('Swap')
        self.pushButton_3.setText('Convert')
        self.label_3.setText(' ')
        lang='Will be'

    def Hausa_lang(self):  #
        self.label.setText('Maida daga')
        self.label_2.setText('Kudi tana canzawa zuwa')
        self.pushButton_2.setText(' ')
        self.pushButton_3.setText('Amsa')
        self.label_3.setText(' ')
        lang='zai kasance'

    def Igbo_lang(self):  #
        self.label.setText('Tọghata site na')
        self.label_2.setText("Ego n'ịtụgharị na")
        self.pushButton_2.setText(' ')
        self.pushButton_3.setText('Azịza')
        self.label_3.setText(' ')
        lang='ga-abụ'

    def Yoruba_lang(self):
        self.label.setText('Iyipada lati')
        self.label_2.setText('Owo iyipada si')
        self.pushButton_2.setText(' ')
        self.pushButton_3.setText('Idahun')
        self.label_3.setText(' ')
        lang='yio je'
##################################################################################
    def openin(self):
        options = QFileDialog.Options()
        #
        #fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Image files (*.jpg *.gif *.png)", options=options)
        #
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.gif *.png *.)")
        if fileName:
            print(fileName)
        self.le.setPixmap(QPixmap(fileName))#display image in label

    # def openin(self):
    #     self.uic = loadUi('./gui/open1.ui', self)
    #     pass

    # def submit(self):
        #     pass
