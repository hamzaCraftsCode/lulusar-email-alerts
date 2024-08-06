# Email Alerts Module

This repository contains code that can be used as a separate module in any project for sending email alerts.

## email_alerts.py

The `email_alerts.py` file contains the code which is used to send email alerts to the email addresses specified in the configuration file.

## Config File

The `config.yml` file provided here is a sample. You must create your own `config.yml` file in your project directory.

### Sample `config.yml`

```yaml
EMAIL: 'your_email@example.com'
PASSWORD: 'your_email_password'
ALERTS_ENABLED: true
RECEIVERS:
  - 'receiver1@example.com'
  - 'receiver2@example.com'
