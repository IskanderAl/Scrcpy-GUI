# scrcpy GUI

> 🌐 **Language / Язык / 语言:**
> [🇺🇸 English](README.md) | [**🇷🇺 Русский**](#) | [🇨🇳 中文](README_CN.md)

GUI-обёртка для [scrcpy](https://github.com/Genymobile/scrcpy) — запись экрана Android-устройства в один клик.
Сделано для QA-тестировщиков.

## Установка

### Способ 1 — Установщик (рекомендуется)

1. Перейди в [Releases](../../releases/latest)
2. Скачай `scrcpy-gui-setup-v1.0.0.exe`
3. Запусти → выбери компоненты → установи
4. Ярлык появится на рабочем столе

> Если у тебя уже есть scrcpy или adb — можно снять галочки при установке.

### Способ 2 — ZIP-архив

1. Скачай `scrcpy-gui-v1.0.0-win64.zip` из [Releases](../../releases/latest)
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
2. Запусти **scrcpy GUI**
3. Выбери папку для сохранения
4. Нажми **Start Recording**
5. Когда закончишь — нажми **Stop Recording**
6. Файл сохранится как `record_YYYY-MM-DD_HH-MM-SS.mkv`

## Лицензия

Этот проект использует [scrcpy](https://github.com/Genymobile/scrcpy) (Genymobile / Romain Vimont), распространяемый под лицензией [Apache License 2.0](https://github.com/Genymobile/scrcpy/blob/master/LICENSE).

scrcpy GUI является независимой обёрткой и не модифицирует scrcpy.
