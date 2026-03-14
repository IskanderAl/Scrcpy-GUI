# scrcpy GUI

<p align="center">
  <a href="README.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/us.png" height="20"> English</a>
  &nbsp;|&nbsp;
  <a href="README_RU.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/ru.png" height="20"> Русский</a>
  &nbsp;|&nbsp;
  <a href="README_CN.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/cn.png" height="20"> 中文</a>
  &nbsp;|&nbsp;
  <a href="#"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/kz.png" height="20"> <b>Қазақша</b></a>
  &nbsp;|&nbsp;
  <a href="README_UA.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/ua.png" height="20"> Українська</a>
  &nbsp;|&nbsp;
  <a href="README_BY.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/by.png" height="20"> Беларуская</a>
</p>

[scrcpy](https://github.com/Genymobile/scrcpy) үшін GUI-қабықша — Android құрылғысының экранын айналау және жазу.
QA-тестілеушілерге арналған.

## Мүмкіндіктер

- **Экранды айналау** — құрылғыны бөлек терезеде нақты уақытта көрсету
- **Экранды жазу** — нақты уақыттағы таймермен жазу
- **Бірнеше құрылғыны қолдау** — қосылған құрылғылар тізімінен таңдау
- **Құрылғыны автоанықтау** — қосылған құрылғының моделін автоматты көрсетеді
- **Икемді баптаулар** — формат (MKV/MP4), ажыратымдылық, битрейт, FPS, бағдар, аудио, түрту көрсету
- **Арнайы белгіше** — QA брендтік белгішесі, оңай тану үшін
- **Ақылды процесс басқару** — жазу басталғанда айналауды автоматты жабады, scrcpy терезесінің жабылуын қадағалайды

## Орнату

### 1-тәсіл — Орнатушы (ұсынылады)

1. [Releases](../../releases/latest) бетіне өт
2. `scrcpy-gui-setup-v2.1.0.exe` файлын жүктеп ал
3. Іске қос → компоненттерді таңда → орнат
4. Жұмыс үстелінде таңбаша пайда болады

> Егер scrcpy немесе adb орнатылған болса — орнату кезінде құсбелгіні алып тастауға болады.

### 2-тәсіл — ZIP-мұрағат

1. [Releases](../../releases/latest) бетінен `scrcpy-gui-v2.1.0-win64.zip` жүктеп ал
2. Кез келген қалтаға шығар
3. `scrcpy-gui.exe` іске қос

### 3-тәсіл — Бастапқы кодтан

```bash
pip install customtkinter
python main.py
```

`scrcpy.exe` файлы `main.py` жанында немесе PATH-та болуы керек.

## Талаптар

- Windows 10+
- USB жөндеу қосылған Android құрылғысы
- USB кабель

### USB жөндеуді қалай қосу керек

1. **Параметрлер** > **Телефон туралы** > **Құрастыру нөмірін** 7 рет бас
2. **Параметрлер** > **Әзірлеуші параметрлері** > **USB жөндеу** қос
3. Телефонды USB арқылы қосып, қалқымалы терезеде жөндеуге рұқсат бер

## Қолдану

1. Құрылғыны USB арқылы қос
2. **scrcpy GUI** іске қос — құрылғы атауы автоматты анықталады
3. Бірнеше құрылғы қосылған болса — тізімнен қажеттісін таңда
4. **Mirror Screen** бас — айналау терезесі ашылады
5. Баптауларды реттеу: формат, ажыратымдылық, битрейт, FPS, бағдар, аудио
6. **Record** бас — айналау жабылады, таймермен жазу басталады
7. **Stop** бас — файл `record_YYYY-MM-DD_HH-MM-SS.mkv` ретінде сақталады

## Лицензия

Бұл жоба [scrcpy](https://github.com/Genymobile/scrcpy) (Genymobile / Romain Vimont) пайдаланады, [Apache License 2.0](https://github.com/Genymobile/scrcpy/blob/master/LICENSE) лицензиясымен таратылады.

scrcpy GUI — тәуелсіз қабықша, scrcpy-ді өзгертпейді.
