# coding=utf-8

from feedback import Feedback
import urllib2
import urllib
import json
import sys
import os.path

JIRA_URL = "http://jira-old.freewheel.tv/browse/"
PROJECTS = ["CLIENTHELP", "MRM", "FDB", "QOS",
            "INK", "OPP", "ESC", "OPS"]

# load all projects
# if os.path.exists("projects.json"):
#     project_file = file("projects.json", "r")
#     results = json.load(project_file)
#     if len(results) > 0:
#         PROJECTS = []
#         for project in results:
#             PROJECTS.append(project['key'])

# generate options for ticket number
if len(sys.argv) == 2:
    query = urllib.quote(sys.argv[1])
    feeds = Feedback()
if query.isdigit():
    for project in PROJECTS:
        ticket_url = "%s%s-%s" % (JIRA_URL, project, query)
        feeds.add_item(title=ticket_url, subtitle=ticket_url, valid='YES', arg=ticket_url, icon='icon.png')
else:
    ticket_url = "%s%s" % (JIRA_URL, query)
    feeds.add_item(title=ticket_url, subtitle=ticket_url, valid='YES', arg=ticket_url, icon='icon.png')
print feeds
    