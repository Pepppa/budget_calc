simplificator = {
"Аксессуары для волос": ["snalica"],
"Бреф": ["bref"],
"Газировка": ["sok gazirani","aloe vera"],
"Говядина": ["juneci but"],
"Готовая еда на обед": ["sarma"],
"Дрожжи": ["svezi kvasac"],
"Жевательная резинка": ["zvake"],
"Зубные щётки": ["cetka za zube"],
"Йогурт в баночке": ["jogurt grekos", "dukatos jogurt"],
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
"Макароны": ["nudle"],
"Масло": ["maslac"],
"Минеральная вода":["knjaz milos"],
"Молоко": ["mleko"],
"Мороженое": ["sladoled"],
"Мука": ["brasno"],
"Мясные деликатесы": ["pecenica dimljena", "dimljeni vrat", "slanina"],
"Овощная заморозка": ["zamrzuta mesavina za rusku salatu"],
"Овсяные хлопья": ["pahulice ovsene", "ovsene pahuljice"],
"Огурцы":["krastavac"],
"Пакет": ["biorazgradiva kesa", "kesa velika"],
"Подсолнечное масло": ["ulje"],
"Приправы": ["paprika slatka", "majcina dusica", "lovorov list", "ruzmarin", "bujon govedji"],
"Разрыхлитель для теста": ["prasak za pecivo"],
"Рис": ["riso pronto"],
"Рыбные палочки": ["riblji stapici"],
"Сахар": ["secer kristal"],
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
"Шоколад": ["cokolada"],
"Яйца": ["jaja"]

}






def simplify_name_by_table(original) :
    for simple_cat in simplificator :
        for var in simplificator[simple_cat] :
            if original.find(var) != -1 :
                return ("found", simple_cat)
    return ("not found", original)
