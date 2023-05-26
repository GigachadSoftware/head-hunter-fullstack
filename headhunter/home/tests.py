from django.test import TestCase


CITY_NAMES = {
    "kyiv": "Київ",
    "kharkiv": "Харків",
    "odesa": "Одеса",
    "dnipro": "Дніпро",
    "donetsk": "Донецьк",
    "zaporizhzhia": "Запоріжжя",
    "lviv": "Львів",
    "kryvyi_rih": "Кривий Ріг",
    "mykolaiv": "Миколаїв",
    "sevastopol": "Севастополь",
    "mariupol": "Маріуполь",
    "luhansk": "Луганськ",
    "vinnytsia": "Вінниця",
    "makiivka": "Макіївка",
    "simferopol": "Сімферополь",
    "chernihiv": "Чернігів",
    "kherson": "Херсон",
    "poltava": "Полтава",
    "khmelnytskyi": "Хмельницький",
    "cherkasy": "Черкаси",
    "chernivtsi": "Чернівці",
    "zhytomyr": "Житомир",
    "sumy": "Суми",
    "rivne": "Рівне",
    "horlivka": "Горлівка",
    "ivano_frankivsk": "Івано-Франківськ",
    "kamianske": "Кам'янське",
    "ternopil": "Тернопіль",
    "kropyvnytskyi": "Кропивницький",
    "kremenchuk": "Кременчук",
    "lutsk": "Луцьк",
    "bila_tserkva": "Біла Церква",
    "kerch": "Керч",
    "melitopol": "Мелітополь",
    "kramatorsk": "Краматорськ",
    "uzhhorod": "Ужгород",
    "brovary": "Бровари",
    "yevpatoria": "Євпаторія",
    "berdiansk": "Бердянськ",
    "nikopol": "Нікополь",
    "sloviansk": "Слов'янськ",
    "alchevsk": "Алчевськ",
    "pavlohrad": "Павлоград",
    "sievierodonetsk": "Сєвєродонецьк",
    "kamianets_podilskyi": "Кам'янець-Подільський",
    "lysychansk": "Лисичанськ",
    "mukachevo": "Мукачево",
    "konotop": "Конотоп",
    "uman": "Умань",
    "krasnyi_luch": "Хрустальний (Khrustalnyi)",
    "yalta": "Ялта",
    "oleksandriia": "Олександрія",
    "yenakiieve": "Єнакієве",
    "drohobych": "Дрогобич",
    "berdychiv": "Бердичів",
    "kadiivka": "Кадіївка",
    "shostka": "Шостка",
    "bakhmut": "Бахмут",
    "izmail": "Ізмаїл",
    "novomoskovsk": "Новомосковськ",
    "kostiantynivka": "Костянтинівка",
    "kovel": "Ковель",
    "feodosia": "Феодосія",
    "nizhyn": "Ніжин",
    "smila": "Сміла",
    "kalush": "Калуш",
    "chervonohrad": "Червоноград",
    "boryspil": "Бориспіль",
    "pervomaisk": "Первомайськ",
    "sverdlovsk": "Довжанськ (Dovzhansk)",
    "irpin": "Ірпінь",
    "korosten": "Коростень",
    "pokrovsk": "Покровськ",
    "kolomyia": "Коломия",
    "stryi": "Стрий",
    "chornomorsk": "Чорноморськ",
    "khartsyzk": "Харцизьк",
    "rubizhne": "Рубіжне",
    "zviahel": "Звягель",
    "druzhkivka": "Дружківка",
    "lozova": "Лозова",
    "chystiakove": "Чистякове",
    "enerhodar": "Енергодар",
    "pryluky": "Прилуки",
    "antratsyt": "Антрацит",
    "novovolynsk": "Нововолинськ",
    "horishni_plavni": "Горішні Плавні",
    "shakhtarsk": "Шахтарськ",
    "bilhorod_dnistrovskyi": "Білгород-Дністровський",
    "okhtyrka": "Охтирка",
    "myrnohrad": "Мирноград",
    "snizhne": "Сніжне",
    "izium": "Ізюм",
    "marhanets": "Марганець",
    "rovenky": "Ровеньки",
    "nova_kakhovka": "Нова Каховка",
    "brianka": "Брянка",
    "fastiv": "Фастів",
    "lubny": "Лубни",
    "svitlovodsk": "Світловодськ",
    "zhovti_vody": "Жовті Води",
    "krasnodon": "Сорокине (Sorokyne)",
    "vyshneve": "Вишневе",
    "varash": "Вараш",
    "shepetivka": "Шепетівка",
    "podilsk": "Подільськ",
    "yuzhnoukrainsk": "Южноукраїнськ",
    "myrhorod": "Миргород",
    "romny": "Ромни",
    "pokrov": "Покров",
    "volodymyr": "Володимир",
    "dzhankoi": "Джанкой",
    "vasylkiv": "Васильків",
    "dubno": "Дубно",
    "bucha": "Буча",
    "netishyn": "Нетішин",
    "pervomaisk": "Первомайськ",
    "kakhovka": "Каховка",
    "boyarka": "Боярка",
    "slavuta": "Славута",
    "sambir": "Самбір",
    "yasynuvata": "Ясинувата",
    "starokostiantyniv": "Староко­стянтинів",
    "zhmerynka": "Жмеринка",
    "voznesensk": "Вознесенськ",
    "obukhiv": "Обухів",
    "boryslav": "Борислав",
    "yuzhne": "Южне",
    "vyshhorod": "Вишгород",
    "hlukhiv": "Глухів",
    "avdiivka": "Авдіївка",
    "chuhuiv": "Чугуїв",
    "toretsk": "Торецьк",
    "novoiavorivsk": "Новояворівськ",
    "kostopil": "Костопіль",
    "alushta": "Алушта",
    "mohyliv_podilskyi": "Могилів-Подільський",
    "tokmak": "Токмак",
    "synelnykove": "Синельникове",
    "pervomaiskyi": "Первомайський",
    "sarny": "Сарни",
    "dobropillia": "Добропілля",
    "truskavets": "Трускавець",
    "chortkiv": "Чортків",
    "khust": "Хуст",
    "novyi_rozdil": "Новий Розділ",
    "pershotravensk": "Першотравенськ",
    "zolotonosha": "Золотоноша",
    "kirovske": "Хрестівка (Khrestivka)",
    "ternivka": "Тернівка",
    "kupiansk": "Куп'янськ",
    "khmilnyk": "Хмільник",
    "balakliia": "Балаклія",
    "kirovsk": "Голубівка (Holubivka)",
    "pereiaslav": "Переяслав",
    "bakhchysarai": "Бахчисарай",
    "haisyn": "Гайсин",
    "malyn": "Малин",
    "vynohradiv": "Виноградів",
    "perevalsk": "Перевальськ",
    "slavutych": "Славутич",
    "krasnoperekopsk": "Краснопере­копськ",
    "zdolbuniv": "Здолбунів",
    "korostyshiv": "Коростишів",
    "oleshky": "Олешки",
    "debaltseve": "Дебальцеве",
    "saky": "Саки",
    "lebedyn": "Лебедин",
    "zolochiv": "Золочів",
    "kaniv": "Канів",
    "berehove": "Берегове",
    "brody": "Броди",
    "hadiach": "Гадяч",
    "dokuchaievsk": "Докучаєвськ",
    "koziatyn": "Козятин",
    "ladyzhyn": "Ладижин",
    "nadvirna": "Надвірна",
    "molodohvardiisk": "Молодо­гвардійськ",
    "vilnohirsk": "Вільногірськ",
    "krolevets": "Кролевець",
    "selydove": "Селидове",
    "znamianka": "Знам'янка",
    "volnovakha": "Волноваха",
    "merefa": "Мерефа",
    "armiansk": "Армянськ",
    "kremenets": "Кременець",
    "sokal": "Сокаль",
    "dolyna": "Долина",
    "sukhodilsk": "Суходільськ",
    "polonne": "Полонне",
    "lyman": "Лиман",
    "stebnyk": "Стебник",
    "liubotyn": "Люботин",
    "krasnohrad": "Красноград",
    "trostianets": "Тростянець",
    "popasna": "Попасна",
    "yahotyn": "Яготин",
    "henichesk": "Генічеськ",
    "kiliia": "Кілія",
    "kalynivka": "Калинівка",
    "krasyliv": "Красилів",
    "kurakhove": "Курахове",
    "volochysk": "Волочиськ",
    "piatykhatky": "П'ятихатки",
    "kreminna": "Кремінна",
    "polohy": "Пологи",
    "balta": "Балта",
    "amvrosiivka": "Амвросіївка",
    "dniprorudne": "Дніпрорудне",
    "reni": "Рені",
    "vovchansk": "Вовчанськ",
    "derhachi": "Дергачі",
    "bakhmach": "Бахмач",
    "starobilsk": "Старобільськ",
    "vatutine": "Ватутіне",
    "zvenyhorodka": "Звенигородка",
    "zuhres": "Зугрес",
    "skadovsk": "Скадовськ",
    "svatove": "Сватове",
    "shpola": "Шпола",
    "novoukrainka": "Новоукраїнка",
    "korsun_shevchenkivskyi": "Корсунь-Шевченківський",
    "lutuhyne": "Лутугине",
    "bilohirsk": "Білогірськ",
    "dolynska": "Долинська",
    "iziaslav": "Ізяслав",
    "bilopillia": "Білопілля",
    "bohodukhiv": "Богодухів",
    "skvyra": "Сквира",
    "karlivka": "Карлівка",
    "orikhiv": "Оріхів",
    "bilozerske": "Білозерське",
    "zolote": "Золоте",
    "yunokomunarivsk": "Бунге (Bunhe)",
    "pidhorodne": "Підгородне",
    "rozdilna": "Роздільна",
    "horodok": "Городок",
    "chervono­partyzansk": "Вознесенівка (Voznesenivka)",
    "ilovaisk": "Іловайськ",
    "berezhany": "Бережани",
    "novohrodivka": "Новогродівка",
    "vuhledar": "Вугледар",
    "berezan": "Березань",
    "putyvl": "Путивль",
    "bolhrad": "Болград",
    "bar": "Бар",
    "svaliava": "Свалява",
    "bohuslav": "Богуслав",
    "huliaipole": "Гуляйполе",
    "zmiiv": "Зміїв",
    "ovruch": "Овруч",
    "verkhnodniprovsk": "Верхньодніп­ровськ",
    "ochakiv": "Очаків",
    "krasnohorivka": "Красногорівка",
    "kivertsi": "Ківерці",
    "pyriatyn": "Пирятин",
    "mykolaivka": "Миколаївка",
    "chasiv_yar": "Часів Яр",
    "vilniansk": "Вільнянськ",
    "dunaivtsi": "Дунаївці",
    "apostolove": "Апостолове",
    "talne": "Тальне",
    "artsyz": "Арциз",
    "novyi_buh": "Новий Буг",
    "tulchyn": "Тульчин",
    "haivoron": "Гайворон",
    "horodok": "Городок",
    "hola_prystan": "Гола Пристань",
    "nosivka": "Носівка",
    "zhashkiv": "Жашків",
    "horodyshche": "Городище",
    "vasylivka": "Василівка",
    "kamianka_dniprovska": "Кам'янка-Дніпровська",
    "petrovske": "Петровське",
    "beryslav": "Берислав",
    "snihurivka": "Снігурівка",
    "radomyshl": "Радомишль",
    "burshtyn": "Бурштин",
    "rakhiv": "Рахів",
    "novhorod_siverskyi": "Новгород-Сіверський",
    "kamianka": "Кам'янка",
    "tetiiv": "Тетіїв",
    "mykolaiv": "Миколаїв",
    "ostroh": "Острог",
    "zelenodolsk": "Зеленодольськ",
    "vakhrusheve": "Боково-Хрустальне (Bokovo-Khrustalne)",
    "khorol": "Хорол",
    "storozhynets": "Сторожинець",
    "sudak": "Судак",
    "siversk": "Сіверськ",
    "koriukivka": "Корюківка",
    "biliaivka": "Біляївка",
    "hirnyk": "Гірник",
    "ukrainka": "Українка",
    "nova_odesa": "Нова Одеса",
    "horodnia": "Городня",
    "shchastia": "Щастя",
    "kaharlyk": "Кагарлик",
    "zhdanivka": "Жданівка",
    "berezne": "Березне",
    "terebovlia": "Теребовля",
    "vynnyky": "Винники",
    "rozhyshche": "Рожище",
    "yavoriv": "Яворів",
    "zhovkva": "Жовква",
    "tarashcha": "Тараща",
    "myronivka": "Миронівка",
    "bershad": "Бершадь",
    "ukrainsk": "Українськ",
    "zbarazh": "Збараж",
    "novomyrhorod": "Новомиргород",
    "uzyn": "Узин",
    "svitlodarsk": "Світлодарськ",
    "soledar": "Соледар",
    "bashtanka": "Баштанка",
    "mala_vyska": "Мала Виска",
    "irmino": "Ірміно",
    "barvinkove": "Барвінкове",
    "prymorsk": "Приморськ",
    "mena": "Мена",
    "hlobyne": "Глобине",
    "hnivan": "Гнівань",
    "komsomolske": "Кальміуське (Kalmiuske)",
    "ichnia": "Ічня",
    "novoazovsk": "Новоазовськ",
    "baranivka": "Баранівка",
    "buchach": "Бучач",
    "lokhvytsia": "Лохвиця",
    "snovsk": "Сновськ",
    "bobrynets": "Бобринець",
    "nemyriv": "Немирів",
    "kobeliaky": "Кобеляки",
    "rodynske": "Родинське",
    "chyhyryn": "Чигирин",
    "bobrovytsia": "Бобровиця",
    "sosnivka": "Соснівка",
    "zhydachiv": "Жидачів",
    "yampil": "Ямпіль",
    "mospyne": "Моспине",
    "borzna": "Борзна",
    "shcholkine": "Щолкіне",
    "buryn": "Буринь",
    "kamianka_buzka": "Кам'янка-Бузька",
    "hrebinka": "Гребінка",
    "khrystynivka": "Христинівка",
    "hirske": "Гірське",
    "tavriisk": "Таврійськ",
    "borshchiv": "Борщів",
    "zymohiria": "Зимогір'я",
    "khotyn": "Хотин",
    "illintsi": "Іллінці",
    "pomichna": "Помічна",
    "olevsk": "Олевськ",
    "kamin_kashyrskyi": "Камінь-Каширський",
    "tatarbunary": "Татарбунари",
    "pohrebyshche": "Погребище",
    "marinka": "Мар'їнка",
    "bolekhiv": "Болехів",
    "inkerman": "Інкерман",
    "zinkiv": "Зіньків",
    "khodoriv": "Ходорів",
    "sniatyn": "Снятин",
    "derazhnia": "Деражня",
    "liuboml": "Любомль",
    "valky": "Валки",
    "novodnistrovsk": "Новодністровськ",
    "radyvyliv": "Радивилів",
    "vuhlehirsk": "Вуглегірськ",
    "sokyriany": "Сокиряни",
    "verkhivtseve": "Верхівцеве",
    "zalishchyky": "Заліщики",
    "staryi_krym": "Старий Крим",
    "bilytske": "Білицьке",
    "pereshchepyne": "Перещепине",
    "andrushivka": "Андрушівка",
    "pustomyty": "Пустомити",
    "horodenka": "Городенка",
    "tysmenytsia": "Тисмениця",
    "tiachiv": "Тячів",
    "semenivka": "Семенівка",
    "dubrovytsia": "Дубровиця",
    "kodyma": "Кодима",
    "irshava": "Іршава",
    "berezivka": "Березівка",
    "ananiv": "Ананьїв",
    "monastyryshche": "Монастирище",
    "reshetylivka": "Решетилівка",
    "lypovets": "Липовець",
    "vylkove": "Вилкове",
    "radekhiv": "Радехів",
    "mostyska": "Мостиська",
    "artemivsk": "Кипуче (Kypuche)",
    "novodruzhesk": "Новодружеськ",
    "zavodske": "Заводське",
    "alupka": "Алупка",
    "horokhiv": "Горохів",
    "pryvillia": "Привілля",
    "chop": "Чоп",
    "zastavna": "Заставна",
    "zorynsk": "Зоринськ",
    "tlumach": "Тлумач",
    "teplodar": "Теплодар",
    "lanivtsi": "Ланівці",
    "busk": "Буськ",
    "korets": "Корець",
    "rohatyn": "Рогатин",
    "pivdenne": "Південне",
    "dubliany": "Дубляни",
    "rzhyshchiv": "Ржищів",
    "novoselytsia": "Новоселиця",
    "vorozhba": "Ворожба",
    "kosiv": "Косів",
    "pochaiv": "Почаїв",
    "rava_ruska": "Рава-руська",
    "molochansk": "Молочанськ",
    "yaremche": "Яремче",
    "turka": "Турка",
    "kitsman": "Кіцмань",
    "peremyshliany": "Перемишляни",
    "blahovishchenske": "Благовіщенське",
    "seredyna_buda": "Середина-Буда",
    "zboriv": "Зборів",
    "khorostkiv": "Хоростків",
    "oster": "Остер",
    "sharhorod": "Шаргород",
    "perechyn": "Перечин",
    "oleksandrivsk": "Олександрівськ",
    "kopychyntsi": "Копичинці",
    "skole": "Сколе",
    "zalizne": "Залізне",
    "sudova_vyshnia": "Судова Вишня",
    "halych": "Галич",
    "morshyn": "Моршин",
    "monastyryska": "Монастириська",
    "miusynsk": "Міусинськ",
    "vashkivtsi": "Вашківці",
    "velyki_mosty": "Великі Мости",
    "druzhba": "Дружба",
    "staryi_sambir": "Старий Самбір",
    "broshniv_osada": "Брошнів-Осада",
    "chudniv": "Чуднів",
    "shumsk": "Шумськ",
    "sviatohirsk": "Святогірськ",
    "almazna": "Алмазна",
    "vyzhnytsia": "Вижниця",
    "dobromyl": "Добромиль",
    "rudky": "Рудки",
    "khyriv": "Хирів",
    "skalat": "Скалат",
    "komarno": "Комарно",
    "bibrka": "Бібрка",
    "novyi_kalyniv": "Новий Калинів",
    "hlyniany": "Глиняни",
    "pidhaitsi": "Підгайці",
    "baturyn": "Батурин",
    "belz": "Белз",
    "ustyluh": "Устилуг",
    "hertsa": "Герца",
    "berestechko": "Берестечко",
    "chernobyl": "Чорнобиль",
    "uhniv": "Угнів",
    "pripyat": "Прип'ять",
}


def get_city_name(city: str):
    return CITY_NAMES.get(city, "<?>")
