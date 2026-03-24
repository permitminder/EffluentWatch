# EffluentWatch

Automated water discharge permit exceedance monitoring for Texas NPDES facilities.

EffluentWatch tracks permit exceedances reported through the EPA ECHO (Enforcement and Compliance History Online) system, surfaces them in an interactive dashboard, and sends daily email alerts to subscribers.

## Key Features

- **Automated Data Collection** — GitHub Actions scrapes EPA ECHO bulk DMR data weekly, filtering to Texas permits
- **Exceedance Detection** — Compares reported discharge values against permit limits to identify exceedances
- **Daily Email Alerts** — Subscribers receive notifications when facilities exceed permit limits
- **Interactive Dashboard** — Streamlit + Plotly charts for exploring exceedance data by county, parameter, and time
- **Stripe-Integrated Paywall** — Free tier (20 results/query) and Pro tier ($29/month for unlimited access + daily alerts)
- **Supabase Backend** — Authentication, subscription management, and data storage

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Python 3.11, Streamlit |
| Data Processing | Pandas, NumPy |
| Charts | Plotly |
| Database | Supabase (PostgreSQL) |
| Payments | Stripe |
| Automation | GitHub Actions |
| Hosting | Render |

## Architecture

```
EPA ECHO (bulk DMR data)
    │
    ▼
echo_dmr_scraper.py  ←── GitHub Actions (weekly, Monday 6AM UTC)
    │
    ▼
tx_exceedances_launch_ready.csv  (append-only, deduped)
    │
    ├──► main.py (Streamlit app on Render)
    │       ├── Search Records
    │       ├── Email Alerts (Supabase signups)
    │       └── Dashboard (Plotly charts)
    │
    └──► send_notifications.py  ←── GitHub Actions (daily, 8AM CST)
            └── Gmail SMTP → subscribers
```

## Data Source

All data is sourced from the EPA ECHO ICIS-NPDES bulk download:
https://echo.epa.gov/tools/data-downloads/icis-npdes-dmr-and-limit-data-set

Texas permits are filtered by `STATE_CODE = "TX"` or permit number prefix `TX`.

## Revenue Model

| Tier | Price | Features |
|------|-------|----------|
| Free | $0 | 20 results per query |
| Pro | $29/month | Unlimited results + daily email alerts |

## Environment Variables

The following secrets are required for full operation (not set up yet):

```
SUPABASE_URL        # Supabase project URL
SUPABASE_KEY        # Supabase anon key
STRIPE_SECRET_KEY   # Stripe API key
STRIPE_PRICE_ID     # Stripe price ID for Pro tier
GMAIL_USER          # Sender Gmail address
GMAIL_PASS          # Gmail app password
```

## License

MIT License — see [LICENSE](LICENSE) for details.
