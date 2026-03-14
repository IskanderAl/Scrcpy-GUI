# scrcpy GUI

<p align="center">
  <a href="README.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/us.png" height="20"> English</a>
  &nbsp;|&nbsp;
  <a href="README_RU.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/ru.png" height="20"> Русский</a>
  &nbsp;|&nbsp;
  <a href="README_CN.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/cn.png" height="20"> 中文</a>
  &nbsp;|&nbsp;
  <a href="README_KZ.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/kz.png" height="20"> Қазақша</a>
  &nbsp;|&nbsp;
  <a href="README_UA.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/ua.png" height="20"> Українська</a>
  &nbsp;|&nbsp;
  <a href="#"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/by.png" height="20"> <b>Беларуская</b></a>
</p>

GUI-абалонка для [scrcpy](https://github.com/Genymobile/scrcpy) — люстраванне і запіс экрана Android-прылады.
Створана для QA-тэсціроўшчыкаў.

## Магчымасці

- **Люстраванне экрана** — адлюстраванне прылады ў рэальным часе ў асобным акне
- **Запіс экрана** — запіс з таймерам у рэальным часе
- **Падтрымка некалькіх прылад** — выбар з спісу падлучаных прылад
- **Аўтавызначэнне прылады** — аўтаматычна паказвае мадэль падлучанай прылады
- **Гнуткія налады** — фармат (MKV/MP4), разрозненне, бітрэйт, FPS, арыентацыя, аўдыё, адлюстраванне дотыкаў
- **Уласная іконка** — фірмовая QA-іконка для хуткага распазнавання
- **Разумнае кіраванне працэсамі** — аўтаматычна закрывае люстэрка пры пачатку запісу, адсочвае закрыццё акна scrcpy

## Усталяванне

### Спосаб 1 — Усталёўшчык (рэкамендуецца)

1. Перайдзі ў [Releases](../../releases/latest)
2. Спампуй `scrcpy-gui-setup-v2.1.0.exe`
3. Запусці → абяры кампаненты → усталюй
4. Цэтлік з'явіцца на працоўным стале

> Калі scrcpy або adb ужо ўсталяваны — можна зняць галачкі пры ўсталяванні.

### Спосаб 2 — ZIP-архіў

1. Спампуй `scrcpy-gui-v2.1.0-win64.zip` з [Releases](../../releases/latest)
2. Распакуй у любую тэчку
3. Запусці `scrcpy-gui.exe`

### Спосаб 3 — З зыходнага коду

```bash
pip install customtkinter
python main.py
```

Патрэбны `scrcpy.exe` побач з `main.py` або ў PATH.

## Патрабаванні

- Windows 10+
- Android-прылада з уключанай USB-адладкай
- USB-кабель

### Як уключыць USB-адладку

1. **Налады** > **Пра тэлефон** > 7 разоў націснуць на **Нумар зборкі**
2. **Налады** > **Для распрацоўшчыкаў** > уключыць **Адладка па USB**
3. Падлучыць тэлефон па USB і дазволіць адладку ва ўсплываючым акне

## Выкарыстанне

1. Падлучы прыладу па USB
2. Запусці **scrcpy GUI** — імя прылады вызначыцца аўтаматычна
3. Калі падлучана некалькі прылад — абяры патрэбную са спісу
4. Націсні **Mirror Screen** — адкрыецца акно люстравання
5. Наладзь параметры: фармат, разрозненне, бітрэйт, FPS, арыентацыя, аўдыё
6. Націсні **Record** — люстэрка закрыецца, пачнецца запіс з таймерам
7. Націсні **Stop** — файл захаваецца як `record_YYYY-MM-DD_HH-MM-SS.mkv`

## Ліцэнзія

Гэты праект выкарыстоўвае [scrcpy](https://github.com/Genymobile/scrcpy) (Genymobile / Romain Vimont), які распаўсюджваецца пад ліцэнзіяй [Apache License 2.0](https://github.com/Genymobile/scrcpy/blob/master/LICENSE).

scrcpy GUI з'яўляецца незалежнай абалонкай і не мадыфікуе scrcpy.
