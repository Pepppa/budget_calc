simplificator = {
"Аксессуары для волос": ["snalica"],
"Бреф": ["bref"],
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
"Кондиционер для стирки": ["lenor"],
"Кости на суп": ["junece mesnate kosti"],
"Круассаны": ["7days"],
"Курица":["pile "],
"Лимонная кислота":["limuntus"],
"Лук": ["crni luk", "luk mladi", "luk crni"],
"Майонез": ["majonez"],
"Макароны": ["nudle", "testenina"],
"Масло": ["maslac"],
"Минеральная вода":["knjaz milos"],
"Молоко": ["mleko"],
"Мороженое": ["sladoled"],
"Мука": ["brasno"],
"Мясные деликатесы": ["pecenica dimljena", "dimljeni vrat", "slanina"],
"Овощная заморозка": ["zamrzuta mesavina za rusku salatu"],
"Овсяные хлопья": ["pahulice ovsene", "ovsene pahuljice"],
"Огурцы":["krastavac"],
"Отбеливатель": ["maramice za blistavo beli ves", "izbeljivac", "za izbeljivanje rublja"],
"Пакет": ["biorazgradiva kesa", "kesa velika", "kesa za zamrzivac"],
"Подсолнечное масло": ["ulje"],
"Приправы": ["paprika slatka", "majcina dusica", "lovorov list", "ruzmarin", "bujon govedji"],
"Пиво": ["pivo"],
"Разрыхлитель для теста": ["prasak za pecivo"],
"Рис": ["riso pronto"],
"Рулет": ["rolat jumbo roll"],
"Рыбные палочки": ["riblji stapici"],
"Сахар": ["secer kristal", "secer u prahu"],
"Свинина": ["svinjski but"],
"Сметана": ["mileram"],
"Соевый соус": ["sos soja"],
"Сосиски": ["virsla", "pileci hot dog"],
"Средство для прочистки труб": ["za otpusavanje slivnika"],
"Стиральный порошок": ["persil"],
"Сыр": ["sir"],
"Томателло": ["tomatello"],
"Туалетная бумага":["perfex comfort"],
"Хлеб": ["hleb"],
"Чай": ["caj"],
"Чеснок": ["beli luk"],
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
