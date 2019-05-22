from lxml import html
import requests
import pyfiglet
from prettytable import PrettyTable

page = requests.get("https://www.theguardian.com/football/premierleague/table")
tree = html.fromstring(page.content)

clubs = tree.xpath("//a[@class='team-name__long']/text()")
points = tree.xpath("//tr/td[10]/b[1]/text()")
goal_difference = tree.xpath("//td[9]/text()")
goals_for = tree.xpath("//td[7]/text()")
goals_against = tree.xpath("//td[8]/text()")

x = PrettyTable()

column_names = ["Club", "Points", "Goal Difference", "Goals for", "Goals against"]

x.add_column(column_names[0], clubs)
x.add_column(column_names[1], points)
x.add_column(column_names[2], goal_difference)
x.add_column(column_names[3], goals_for)
x.add_column(column_names[4], goals_against)

print(x)
print("")
print("The data provided is gathered from the Guardian website, https://www.theguardian.com/football/premierleague/table")

#print("clubs %s" % clubs)
#print("points %s" % points)
#print("goal_difference %s" % goal_difference)
#print("goals_for %s" % goals_for)
#print("goals_against %s" % goals_against)
