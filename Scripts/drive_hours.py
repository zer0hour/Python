#!/usr/bin/env python3

years = int(input('Years: '))
if years >= 1:
    years = (365 * years)

months = int(input('Months: '))
if months >= 1:
    months = (30 * months)

days = int(input('Days: '))

total = (years + months + days) * 24

print('Total drive hours: ' + str(total))
