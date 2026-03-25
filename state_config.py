"""
State configuration for this EffluentWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "TX"
STATE_NAME = "Texas"
APP_NAME = "EffluentWatch"
APP_TAGLINE = "Texas Discharge Monitoring"
DOMAIN = "effluentwatch.org"
DATA_FILE = "tx_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@effluentwatch.org"
MAILING_ADDRESS = "PO Box 1501, Austin, TX 78767"
TIMEZONE_LABEL = "CST"
EPA_REGION = 6
