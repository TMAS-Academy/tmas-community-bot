# TMAS Academy Community Bot

A Discord bot built for the **TMAS Academy** community server. It provides slash commands that help members discover educational resources, explore TMAS Academy books, and access useful information about the organization and its Discord community.

> **Project Status:** Core functionality implemented and locally verified. Live Discord testing and deployment are pending.

## Features

The bot currently provides eight slash commands:

| Command | Description |
|---|---|
| `/help` | Displays the available bot commands and how to use them. |
| `/resources` | Shares useful TMAS Academy educational resources. |
| `/recommend` | Recommends a TMAS Academy book based on a subject or topic. |
| `/about` | Provides information about TMAS Academy. |
| `/website` | Links members to the TMAS Academy website. |
| `/server_info` | Displays information about the Discord server. |
| `/rules` | Displays the community rules. |
| `/ping` | Checks the bot's response latency. |

### Book Recommendation System

The `/recommend` command uses a curated book catalog and topic-keyword matching system to help members find relevant TMAS Academy publications.

The catalog currently covers:

- AMC 10 and AMC 12
- AP Calculus AB and BC
- AP Physics 1
- AP Physics C: Mechanics
- AP Chemistry
- AP Computer Science Principles
- AP Statistics
- AP Biology
- AP Psychology
- AP Human Geography
- Multivariable Calculus
- Differential Equations and Linear Algebra

Recommendations use predefined topic keywords rather than an AI-powered semantic search system.

## Technology Stack

- **Python** — Core programming language
- **discord.py** — Discord API integration and slash commands
- **python-dotenv** — Environment-variable management

The Community Bot does not currently require a database.

## Project Structure

```text
tmas-community-bot/
├── src/
│   └── tmas_bot/
│       ├── __init__.py
│       ├── config.py
│       ├── bot.py
│       └── commands/
│           ├── __init__.py
│           ├── about.py
│           ├── help.py
│           ├── ping.py
│           ├── recommend.py
│           ├── resources.py
│           ├── rules.py
│           ├── server_info.py
│           └── website.py
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- A Discord application and bot token
- Access to a Discord server where the bot can be tested

### 1. Clone the Repository

```bash
git clone https://github.com/AdityaB2007/tmas-community-bot.git
cd tmas-community-bot
```

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the repository root using `.env.example` as a template:

```env
DISCORD_TOKEN=your_discord_bot_token
GUILD_ID=your_discord_server_id
```

| Variable | Description |
|---|---|
| `DISCORD_TOKEN` | Authentication token for the Discord bot. |
| `GUILD_ID` | Discord server ID used for guild-specific slash-command synchronization during development. |

**Important:** Never commit your `.env` file or expose your Discord bot token publicly.

### 5. Run the Bot

From the repository root:

**Windows PowerShell:**

```powershell
$env:PYTHONPATH = "src"
python -m tmas_bot.bot
```

The bot loads its command extensions and synchronizes slash commands with the configured development guild.

## Development and Verification

Commands are organized into separate extensions under `src/tmas_bot/commands/`. The main bot module loads these extensions dynamically.

The following local verification checks have been completed:

- Python compilation and import checks
- Book recommendation tests, including unknown-topic handling
- Dependency consistency verification using `pip check`
- Git status and commit-history checks

Live interaction testing in Discord and production deployment remain pending.

## Deployment Status

**Deployment is currently pending.**

The bot has been developed and verified locally, but it is not currently running on a production hosting provider. Hosting has been deferred until after the current academic term.

Future deployment will require:

- A persistent hosting environment suitable for a continuously running Discord bot
- Secure configuration of production environment variables
- Live testing of all slash commands in the target Discord server
- Verification of reliable operation and automatic reconnection

No production hosting provider or active 24/7 deployment is currently designated.

## TMAS Academy

- **Website:** https://www.tmasacademy.com/
- **Books:** https://www.tmasacademy.com/books

## License

See the [LICENSE](LICENSE) file for license details.