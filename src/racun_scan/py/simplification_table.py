simplificator = {
"Яйца": ["jaja"],
"Хлеб": ["hleb"],
"Приправы": ["paprika slatka", "majcina dusica", "lovorov list", "ruzmarin", "bujon govedji"],
"Йогурт в баночке": ["jogurt grekos"],
"Сыр": ["sir"],
"Макароны": ["nudle"],
"Круассаны": ["7days"],
"Разрыхлитель для теста": ["prasak za pecivo"],
"Чай": ["caj"],
"Чеснок": ["beli luk"],
"Капуста": ["kupus"],
"Зубные щётки": ["cetka za zube"],
"Дрожжи": ["svezi kvasac"],
"Масло": ["maslac"],
"Картошка": ["krompir"],
"Сосиски": ["virsla"],
"Овощная заморозка": ["zamrzuta mesavina za rusku salatu"],
"Шоколад": ["cokolada"],
"Сметана": ["mileram"],
"Лук": ["crni luk"],
"Говядина": ["juneci but"],
"Рыбные палочки": ["riblji stapici"],
"Майонез": ["majonez"],
"Мука": ["brasno"],
"Сахар": ["secer kristal"],
"Кондиционер для стирки": ["lenor"],
"Подсолнечное масло": ["ulje"],
"Рис": ["riso pronto"],
"Томателло": ["tomatello"],
"Бреф": ["bref"],
"Стиральный порошок": ["persil"],
"Средство для прочистки труб": ["za otpusavanje slivnika"],
"Кефир": ["kefir"],
"Мясные деликатесы": ["pecenica dimljena", "dimljeni vrat"],
"Кости на суп": ["junece mesnate kosti"],
"Молоко": ["mleko"]

 }


def simplify_name_by_table(original) :
    for simple_cat in simplificator :
        for var in simplificator[simple_cat] :
            if original.find(var) != -1 :
                return simple_cat
    return original
