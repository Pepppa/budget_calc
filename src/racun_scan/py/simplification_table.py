simplificator = {
"Аксессуары для волос": ["snalica"],
"Ананас": ["ananas svez"],
"Бреф": ["bref"],
"Валерьянка": ["valeriana"],
"Ванилин": ["vanil secer"],
"Варенье малиновое": ["slatko malina"],
"Витамины": ["magnezijum", "omega3"],
"Газировка": ["sok gazirani","aloe vera", "fanta"],
"Говядина": ["juneci but"],
"Готовая еда на обед": ["sarma"],
"Дрожжи": ["svezi kvasac"],
"Жевательная резинка": ["zvake", "orbit"],
"Зубные щётки": ["cetka za zube"],
"Йогурт в баночке": ["jogurt grekos", "dukatos jogurt"],
"Йогурт питьевой": ["jogurt 2.8%mm"],
"Канцтовары": ["selotejp traka", "koverte", "fascikla", "skalper", "spajalice", "stipaljke"],
"Капуста": ["kupus"],
"Картошка": ["krompir"],
"Кефир": ["kefir"],
"Колбаса": ["mortadella", "salama"],
"Кондиционер для стирки": ["lenor"],
"Кокос": ["kokos napitak"],
"Конфеты": ["haribo"],
"Кости на суп": ["junece mesnate kosti"],
"Кофе растворимый": ["nescafe"],
"Круассаны": ["7days"],
"Курица":["pile ", "pileca krila"],
"Лимонная кислота":["limuntus"],
"Лук": ["crni luk", "luk mladi", "luk crni"],
"Майонез": ["majonez"],
"Макароны": ["nudle", "testenina"],
"Масло": ["maslac"],
"Минеральная вода":["knjaz milos"],
"Молоко": ["mleko"],
"Молочный десерт": ["puding"],
"Морковь": ["sargarepa"],
"Мороженое": ["sladoled", "slad.delhaize", "slad.ducale"],
"Мука": ["brasno"],
"Мюсли": ["musli"],
"Мясные деликатесы": ["pecenica dimljena", "dimljeni vrat", "slanina", "dim.svinj.spic reb", "pecenica dim", "vrat dimlj"],
"Носки": ["socks", "nazuvica"],
"Овощная заморозка": ["zamrzuta mesavina za rusku salatu"],
"Овсяные хлопья": ["pahulice ovsene", "ovsene pahuljice"],
"Огурцы":["krastavac"],
"Отбеливатель": ["maramice za blistavo beli ves", "izbeljivac", "za izbeljivanje rublja", "dr.beck.eliminator", "lovac na boje"],
"Пакет": ["biorazgradiva kesa", "kesa velika", "kesa za zamrzivac", "kesa tregerica", "kese ap kom", "kesa trgovacka", "dm pap. kesa recik"],
"Персики": ["breskva domaca"],
"Подсолнечное масло": ["ulje"],
"Приправы": ["paprika slatka", "majcina dusica", "lovor", "ruzmarin", "bujon govedji", "crni bib"],
"Пиво": ["pivo", "staropramen", "lowenbrau", "somersby"],
"Разрыхлитель для теста": ["prasak za pec"],
"Рис": ["riso pronto"],
"Рулет": ["rolat jumbo roll"],
"Рыбные палочки": ["riblji stapici"],
"Сахар": ["secer kristal", "secer u prahu"],
"Свинина": ["svinjski but", "svinjski vrat bk"],
"Сироп": ["deser.preliv"],
"Сливки": ["pavlaka za slag"],
"Сметана": ["mileram"],
"Соевый соус": ["sos soja"],
"Соль": ["so mors"],
"Сосиски": ["virsla", "pileci hot dog"],
"Средство для прочистки труб": ["za otpusavanje slivnika"],
"Средство для укладки": ["taft"],
"Стиральный порошок": ["persil"],
"Сыр": ["sir", "gauda"],
"Томателло": ["tomatello"],
"Туалетная бумага":["perfex comfort"],
"Хлеб": ["hleb"],
"Чай": ["caj"],
"Чеснок": ["beli luk"],
"Чипсы": ["cips"],
"Чистящее средство": ["cif"],
"Шоколад": ["cokolada"],
"Яблоки": ["jabuka crveni delises"],
"Яйца": ["jaja"]

}


def simplify_name_by_table(original) :
    for simple_cat in simplificator :
        for var in simplificator[simple_cat] :
            if original.find(var) != -1 :
                return ("found", simple_cat)
    return ("not found", original)
