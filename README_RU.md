# scrcpy GUI

<p align="center">
  <a href="README.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/us.png" height="20"> English</a>
  &nbsp;|&nbsp;
  <a href="#"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/ru.png" height="20"> <b>Русский</b></a>
  &nbsp;|&nbsp;
  <a href="README_CN.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/cn.png" height="20"> 中文</a>
  &nbsp;|&nbsp;
  <a href="README_KZ.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/kz.png" height="20"> Қазақша</a>
  &nbsp;|&nbsp;
  <a href="README_UA.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/ua.png" height="20"> Українська</a>
  &nbsp;|&nbsp;
  <a href="README_BY.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/by.png" height="20"> Беларуская</a>
</p>

GUI-обёртка для [scrcpy](https://github.com/Genymobile/scrcpy) — зеркалирование и запись экрана Android-устройства.
Сделано для QA-тестировщиков.

## Возможности

- **Зеркалирование экрана** — отображение устройства в реальном времени в отдельном окне
- **Запись экрана** — запись с таймером в реальном времени
- **Поддержка нескольких устройств** — выбор из списка подключённых устройств
- **Автоопределение устройства** — автоматически показывает модель подключённого устройства
- **Гибкие настройки** — формат (MKV/MP4), разрешение, битрейт, FPS, ориентация, аудио, отображение касаний
- **Кастомная иконка** — фирменная QA-иконка для быстрого распознавания
- **Умное управление процессами** — автоматически закрывает зеркало при начале записи, отслеживает закрытие окна scrcpy

## Установка

### Способ 1 — Установщик (рекомендуется)

1. Перейди в [Releases](../../releases/latest)
2. Скачай `scrcpy-gui-setup-v2.1.0.exe`
3. Запусти → выбери компоненты → установи
4. Ярлык появится на рабочем столе

> Если у тебя уже есть scrcpy или adb — можно снять галочки при установке.

### Способ 2 — ZIP-архив

1. Скачай `scrcpy-gui-v2.1.0-win64.zip` из [Releases](../../releases/latest)
2. Распакуй в любую папку
3. Запусти `scrcpy-gui.exe`

### Способ 3 — Из исходников

```bash
pip install customtkinter
python main.py
```

Требуется `scrcpy.exe` рядом с `main.py` или в PATH.

## Требования

- Windows 10+
- Android-устройство с включённой USB-отладкой
- USB-кабель

### Как включить USB-отладку

1. **Настройки** > **О телефоне** > 7 раз нажать на **Номер сборки**
2. **Настройки** > **Для разработчиков** > включить **Отладка по USB**
3. Подключить телефон по USB и разрешить отладку во всплывающем окне

## Использование

1. Подключи устройство по USB
2. Запусти **scrcpy GUI** — имя устройства определится автоматически
3. Если подключено несколько устройств — выбери нужное из списка
4. Нажми **Mirror Screen** — откроется окно зеркалирования
5. Настрой параметры: формат, разрешение, битрейт, FPS, ориентация, аудио
6. Нажми **Record** — зеркало закроется, начнётся запись с таймером
7. Нажми **Stop** — файл сохранится как `record_YYYY-MM-DD_HH-MM-SS.mkv`

## Лицензия

Этот проект использует [scrcpy](https://github.com/Genymobile/scrcpy) (Genymobile / Romain Vimont), распространяемый под лицензией [Apache License 2.0](https://github.com/Genymobile/scrcpy/blob/master/LICENSE).

scrcpy GUI является независимой обёрткой и не модифицирует scrcpy.
