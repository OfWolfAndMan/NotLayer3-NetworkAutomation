# NotLayer3 Network Automation

> **Archived.** This repository is no longer maintained, and its code does not run as
> published. What was worth keeping now lives in
> [Automate teh Network](https://github.com/OfWolfAndMan/Automate-teh-Network), modernised and
> tested. **Start there.**
>
> The device passwords in this repository's files are sample values from the course, and some
> of its sample addresses are real, publicly routable ones. Do not reuse either.

This was the 2020 edition of a network automation course: Python basics, a second set of
lessons on classes, regular expressions and Jinja2 templates, and a final project, a
config-compliance service built from a small Flask API, Netmiko and CiscoConfParse.

A later edition, [Network-Automation-Mini-Course](https://github.com/OfWolfAndMan/Network-Automation-Mini-Course)
(also archived), refined the same service. Both were folded into Automate teh Network.

## Where things went

| Here | Now |
|------|-----|
| The compliance service: `APIs/`, `main.py`, `pre-checks.py`, `utils.py`, `Final Project Details/` | [`playbooks/network/compliance.yml`](https://github.com/OfWolfAndMan/Automate-teh-Network/blob/main/playbooks/network/compliance.yml) with its policies in [`policies/compliance.yml`](https://github.com/OfWolfAndMan/Automate-teh-Network/blob/main/policies/compliance.yml). Policies are validated data and the check runs offline. See [`docs/compliance.md`](https://github.com/OfWolfAndMan/Automate-teh-Network/blob/main/docs/compliance.md). |
| `runner.py` (CDP neighbour collection) | [`playbooks/network/show.yml`](https://github.com/OfWolfAndMan/Automate-teh-Network/blob/main/playbooks/network/show.yml): any `show` command, parsed and saved as JSON per host |
| `advanced_python/` (classes, comprehensions, regex) and `basic-python/connections.py` | the [`examples/python/`](https://github.com/OfWolfAndMan/Automate-teh-Network/tree/main/examples/python) lessons, rewritten so each one runs, is tested and keeps credentials out of the source |
| Jinja2 config templates (`advanced_python/configTemplates/`) | retired: rendering whole configurations is the approach the new repository moved away from |
| First-week Python exercises, `git-basics.txt`, the Postman notes, the committed `log.txt` | not carried over |

Every file here has a recorded successor or a reason it was left behind, in
[`docs/retirements.md`](https://github.com/OfWolfAndMan/Automate-teh-Network/blob/main/docs/retirements.md#absorbed-notlayer3-networkautomation-2020).
