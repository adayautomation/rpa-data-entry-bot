# rpa-affinity-bot

Automated data entry bot for the **Affinity** platform using Python RPA. Reads member records from Excel, parses address data with AI, and fills in web forms automatically using visual recognition — no API access to the target system required.

---

## What It Does

1. Reads member data from an Excel file (`sample_members.xlsx`)
2. Navigates the Affinity platform UI using screenshot-based detection
3. Fills in personal details, fiscal address, province, and municipality fields
4. Handles dropdown menus with dynamic scroll-and-detect logic
5. Confirms completion and moves on

This was built to automate a repetitive manual data entry workflow, reducing processing time from ~8 minutes per record to under 60 seconds.

---

## Tech Stack

| Tool | Role |
|---|---|
| Python 3.11 | Core language |
| pyautogui | Screen detection & mouse/keyboard control |
| pandas | Excel data loading |
| Groq API | AI-powered address parsing |
| openpyxl | Excel file handling |
| python-dotenv | Secure API key management |

---

## Project Structure

```
rpa-affinity-bot/
├── scripts/
│   ├── robot_affinity_completo.py   # Main bot — full form automation
│   ├── leer_excel.py                # Excel reader with AI address parsing
│   └── probar_movimiento.py         # Visual detection test script
├── assets/
│   └── *.png                        # Reference screenshots for UI detection
├── sample_members.xlsx              # Input data (fictional sample included)
├── .env.example                     # Environment variable template
├── requirements.txt
└── README.md
```

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/adayautomation/rpa-affinity-bot.git
cd rpa-affinity-bot
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure your API key**
```bash
cp .env.example .env
# Edit .env and add your Groq API key
```

**4. Add your UI screenshots**

The bot uses image recognition to find buttons and fields on screen. Capture your own screenshots of the target interface and place them in the `assets/` folder:

- `boton_anadir.png` — "Add" button
- `selector_empresa.png` — Entity type selector
- `opcion_fisica.png` — "Physical person" option
- `casilla_nif.png`, `casilla_nombre.png`, `casilla_apellido.png` — Identity fields
- `pestana_domicilio.png` — Address tab
- `casilla_calle.png`, `casilla_cp.png` — Address fields
- `campo_provincia.png`, `opcion_provincia.png` — Province dropdown
- `campo_municipio.png`, `zona_lista_municipios.png`, `opcion_municipio.png` — Municipality scroll

**5. Run**
```bash
python scripts/robot_affinity_completo.py
```

You have 5 seconds after launch to switch focus to the target application window.

---

## Environment Variables

Create a `.env` file based on `.env.example`:

```
GROQ_API_KEY=your_key_here
```

Get a free Groq API key at [console.groq.com](https://console.groq.com)

---

## Key Design Decisions

**Why pyautogui instead of Selenium?**
The target platform is a desktop-style web app with no stable DOM selectors. Visual detection via screenshots was more reliable than trying to target elements with CSS selectors.

**Scroll-and-detect for dropdowns**
The municipality list has 80+ entries with no search input. The bot scrolls in small increments and checks for the target option after each scroll — a common pattern when you can't inject keystrokes into a dropdown.

**AI for address parsing**
Raw addresses from legacy Excel files are inconsistent. Groq + LLaMA handles normalization (splitting street name, number, floor) before the bot writes to the form.

---

## Limitations

- Requires the target window to be visible and unobstructed during execution
- Screenshot references are resolution/zoom-dependent — recapture if display settings change
- Currently processes one record at a time (loop extension is straightforward)
- `pyautogui.FAILSAFE = True` — move mouse to top-left corner to emergency stop

---

## Author

**adayautomation** — Automation Developer  
[github.com/adayautomation](https://github.com/adayautomation)
