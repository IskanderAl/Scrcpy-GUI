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
  <a href="#"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/ua.png" height="20"> <b>Українська</b></a>
  &nbsp;|&nbsp;
  <a href="README_BY.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/by.png" height="20"> Беларуская</a>
</p>

GUI-обгортка для [scrcpy](https://github.com/Genymobile/scrcpy) — дзеркалювання та запис екрану Android-пристрою.
Створено для QA-тестувальників.

## Можливості

- **Дзеркалювання екрану** — відображення пристрою в реальному часі в окремому вікні
- **Запис екрану** — запис з таймером у реальному часі
- **Підтримка кількох пристроїв** — вибір з-поміж підключених пристроїв
- **Автовизначення пристрою** — автоматично показує модель підключеного пристрою
- **Гнучкі налаштування** — формат (MKV/MP4), роздільна здатність, бітрейт, FPS, орієнтація, аудіо, відображення дотиків
- **Власна іконка** — фірмова QA-іконка для швидкого розпізнавання
- **Розумне керування процесами** — автоматично закриває дзеркало при початку запису, відстежує закриття вікна scrcpy

## Встановлення

### Спосіб 1 — Інсталятор (рекомендовано)

1. Перейди до [Releases](../../releases/latest)
2. Завантаж `scrcpy-gui-setup-v2.1.0.exe`
3. Запусти → обери компоненти → встанови
4. Ярлик з'явиться на робочому столі

> Якщо scrcpy або adb вже встановлені — можна зняти галочки під час встановлення.

### Спосіб 2 — ZIP-архів

1. Завантаж `scrcpy-gui-v2.1.0-win64.zip` з [Releases](../../releases/latest)
2. Розпакуй у будь-яку теку
3. Запусти `scrcpy-gui.exe`

### Спосіб 3 — З вихідного коду

```bash
pip install customtkinter
python main.py
```

Потрібен `scrcpy.exe` поруч з `main.py` або в PATH.

## Вимоги

- Windows 10+
- Android-пристрій з увімкненою USB-налагодженням
- USB-кабель

### Як увімкнути USB-налагодження

1. **Налаштування** > **Про телефон** > 7 разів натиснути на **Номер збірки**
2. **Налаштування** > **Для розробників** > увімкнути **Налагодження USB**
3. Підключити телефон по USB і дозволити налагодження у спливаючому вікні

## Використання

1. Підключи пристрій по USB
2. Запусти **scrcpy GUI** — ім'я пристрою визначиться автоматично
3. Якщо підключено кілька пристроїв — обери потрібний зі списку
4. Натисни **Mirror Screen** — відкриється вікно дзеркалювання
5. Налаштуй параметри: формат, роздільна здатність, бітрейт, FPS, орієнтація, аудіо
6. Натисни **Record** — дзеркало закриється, почнеться запис з таймером
7. Натисни **Stop** — файл збережеться як `record_YYYY-MM-DD_HH-MM-SS.mkv`

## Ліцензія

Цей проєкт використовує [scrcpy](https://github.com/Genymobile/scrcpy) (Genymobile / Romain Vimont), що розповсюджується під ліцензією [Apache License 2.0](https://github.com/Genymobile/scrcpy/blob/master/LICENSE).

scrcpy GUI є незалежною обгорткою і не модифікує scrcpy.
