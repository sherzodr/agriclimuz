# Ўзбекистонда (эталон) эвапотранспирацияни ўрганиш

# СЎЗ БОШИ

Ушбу тадқиқотлардан асосий мақсад қуйидаги саволларнинг барига аниқ жавоб топиш:

 * Экин йил мобайнида қанча сув талаб қилади?
 * Бугун экин қанча сув талаб қилди?
 * Охриги суғорилгандан бери тупроқда яна қанча сув запаси қолди?

Бу ва бошқа шу кайфиятдаги саволларга жавоб бериш учун бугунги кундаги бирламча 
йўриқнома, сўзсиз, [БМТ-ФАО нинг "56-суғориш ва дренаж" бюллетени][1]дир. Бу бюллетенда 
[Пенман-Монтит][3] тенглмасидан фойдаланган ҳолда турли иқлим шароитларидан келиб чиқиб
экинларнинг сув сарфини аниқ ҳисоблаш усули тарғиб қилинган. 

Шу пайтгача Ўзбекистон иқлимидаги экинларнинг сув сарфи ҳақида тўлиқ,
бирламчи маълумот манбаъларини тополмадик. Натижада ушбу проект Дунёга келди.

github.com порталининг бизга қўл келадиган жиҳати шундаки, бу маълумотлардан 
истаган одам нусха олиб, унга ҳиссасини қўшиб, яна порталда чоп қилиши мумкун. Зеро
бу Замин, бу Қуёш ва бу оби-ҳаёт барчамизники!

# ФАЙЛЛАР ҲАҚИДА

## reports/

Проектнинг асосий ҳосиласи **reports/** директориясидир. Бу директорияда
барча тадқиқотларнинг натижалари чоп қилинади. 

## script.py ва script.ipynb

Бирчалми маълумотларни таҳлил қилиб, **penmon.eto** кутубхонасидан фойдаланиб
*ETo*ни ҳисобловчи дастур айнан шу дастурдир. Унинг ишлаши учун аввал "pypi.org" 
порталидан **penmon** кутубхонасини ўрнатишингиз талаб қилинади:

	% pip install penmon

## data/

Бу директорияда ҳисоботлар яратиш учун ишлатилган маълумотлар сақланган.

### data/sourcedata

Бу директорияда барча *.csv* файллар [Texas A&M университетининг Global Weather Data][2]
порталидан кўчириб олинган, бирламчи маълумотлар ҳисобланади.

### data/eto.csv

**script.py** дастури бирламчи маълумотларни қайта ишлаб, эвапотранспирацияни
ҳисоблагач барча бирламчи маълумотларни қўшиб шу файлга кўчиради. 

### data/eto.xlsx

Бу файл Excel файли бўлиб, унда eto.csv файлидаги маълумотлар таҳлил қилиниб,
ҳисоботда ишлатилган диаграмма ва жадваллар яратилади. 

## help/

Бу директорияда **penmon.eto** модулидан фойдаланиш бўйича йўриқномалар 
топасиз.

[1]: http://www.fao.org/3/x0490e/x0490e00.htm
[2]: https://globalweather.tamu.edu/
[3]: http://www.fao.org/3/x0490e/x0490e06.htm





