# Ўзбекистонда (эталон) эвапотранспирация ҳисоботи

Ушбу тадқиқот асосий мақсад - Ўзбекистон иқлим шаротида экинларнинг мавсум 
мобайнида қанча сув талаб қилишини аниқлаш. Шу мақсадда Ўзбекистоннинг 70дан 
ортиқ нуқталаридаги 35 йиллик иқлим мъалумоти тадқиқ қилиниб, ФАОнинг 
[ йўриқномасига кўра ][1] эталон экиннинг сув талаби ҳисоблаб чиқилди. 

Энди биз ҳар бир вилоятда исталган экиннинг муайян ойдаги ўртача сув талабини 
биламиз.

Экинларнинг сув талаби ўрганишнинг асосий йўриқномаси сўзсиз, 
[БМТ-ФАО нинг "56-суғориш ва дренаж" бюллетени][1]дир. Бу бюллетенда 
[Пенман-Монтит][3] тенглмасидан фойдаланган ҳолда турли иқлим шароитларидан 
келиб чиқиб экинларнинг сув сарфини аниқ ҳисоблаш усули тарғиб қилинган. 

Шу пайтгача Ўзбекистон иқлимидаги экинларнинг сув сарфи ҳақида тўлиқ,
бирламчи маълумот манбаълари тополмадик. Натижада ушбу проект Дунёга келди.

Бирламчи манбаълар **data/sourcedata** директориясида сақланади. Унда *.csv 
туридаги файлларни топасиз. Бу файллар турли манзиллардаги об-хаво 
маълумотларидир. Ҳар бир файл битта манзил маълумотини сақлайди. Ҳар файлда 
1979-2014 йиллар оралиғидаги кунлик маълумотлар сақланади.

**script.py** дастури эса айнан ўша маълумотларни ўқиб, Панман-Монтит
тенгламаси орқали EToни ҳисоблаб, маълумотлар жамлаб **data/eco.csv** файлига
кўчиради. Айнан шу файл барча тадқиқотда ишлатилган маълумотларнинг барини
сақлайди. github.com порталига бу файлни қўйишнинг имкони бўлмади, сабаби 
у 100мб дан ошиб кетти. Шу сабабли уни яратиш учун "script.py" дастурини
ишлатиш керак бўлади.

**eto.xlsx** файли эса Excel жадвали бўлиб, унда eto.csvдаги маълумотлар
*Power Pivot* дастури орқали таҳлил қилиниб, унда диаграмма ва жамловчи жадваллар
яратилди.

Диаграммалардан фойдаланган ҳолда **report/eto-report.docx** ҳисоботи ёзилган.
**eto-report.pdf** файли эса *.docx* файлининг айнидир.

# Evapotranspiration study in UZBEKISTAN

By studying 35-year climate data from 70 agricultural locations of Uzbekistan
we were able to calculate reference crop evapotranspiration based on 
[Penman-Monteith Equation][3] as detailed in 
[FAO's Irrigation and Drainage Paper #56][1]

You can find the final report in [report/ folder][report]. As of this 
writing the report is available in Uzbek. There is a plan to translate the report
into other languages. Contributors are welcome!

If Uzbek language is not accessible for you,[ eto.xlsx][] file located inside
[ data/ folder ][data] is the actual data file used to generate the above report.
Column labels are left in English.

[1]: http://www.fao.org/3/x0490e/x0490e00.htm
[3]: http://www.fao.org/3/x0490e/x0490e06.htm
[report]: https://github.com/sherzodr/agriclimuz/tree/master/report
[data]: https://github.com/sherzodr/agriclimuz/tree/master/data
[eto.xlsx]: https://github.com/sherzodr/agriclimuz/raw/master/data/eto.xlsx