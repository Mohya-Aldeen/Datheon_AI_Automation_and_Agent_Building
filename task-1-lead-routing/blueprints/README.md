# Blueprints

# Make.com Scenario Blueprints

This directory contains the two exported Make.com scenarios used by the lead qualification automation.

## Scenario A: Lead Intake

File: [`scenario-a-lead-intake.blueprint.json`](./scenario-a-lead-intake.blueprint.json)

This is the main automation scenario. It:

1. Receives normalized lead information through a custom webhook.
2. Sends the lead information to OpenAI for qualification.
3. Creates a record in Airtable.
4. Sends a notification with talking points to Slack.

## Scenario B: Tally Translator

File: [`scenario-b-tally-translator.blueprint.json`](./scenario-b-tally-translator.blueprint.json)

This scenario receives submissions from the Tally form, converts the nested Tally fields into the flat format expected by Scenario A, and forwards the lead to Scenario A's webhook.

## Importing the Blueprints into Make

1. Sign in to Make.com.
2. Create a new empty scenario.
3. Open the scenario menu and select **Import Blueprint**.
4. Import `scenario-a-lead-intake.blueprint.json`.
5. Create another empty scenario.
6. Import `scenario-b-tally-translator.blueprint.json`.
7. Reconnect and configure the modules listed below.
8. Save both scenarios and test them using **Run once**.

## Connections and Settings to Replace

### Scenario A

Configure your own:

- Lead Intake custom webhook
- OpenAI connection
- Airtable connection, base and table
- Slack connection and destination channel

### Scenario B

Configure your own:

- Tally Intake custom webhook
- Scenario A webhook URL in the HTTP module

The HTTP module in Scenario B must send data to the **Lead Intake webhook from Scenario A**. Do not point it back to Scenario B's own webhook.

## Security

The exported files do not contain API keys. Never commit real webhook URLs, access tokens or API keys to the repository.
