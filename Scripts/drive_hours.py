#!/usr/bin/env python3

print('years:')
years = int(input())
if years >= 1:
    years = (365 * years)

print('months:')
months = int(input())
if months >= 1:
    months = (30 * months)

print('days')
days = int(input())

print((years + months + days) * 24)
