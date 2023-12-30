import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=4)
data = puzzle.input_data

passports = [dict(entry.split(':') for entry in p.split()) for p in data.split('\n\n')]


puzzle.answer_a = sum(
    all(field in p for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))
    for p in passports
)

puzzle.answer_b = sum(
    bool(
        (byr := p.get('byr')) and re.fullmatch(r'\d{4}', byr) and 1920 <= int(byr) <= 2002
        and (iyr := p.get('iyr')) and re.fullmatch(r'\d{4}', iyr) and 2010 <= int(iyr) <= 2020
        and (eyr := p.get('eyr')) and re.fullmatch(r'\d{4}', eyr) and 2020 <= int(eyr) <= 2030
        and (hgt := p.get('hgt')) and (m := re.fullmatch(r'(\d+)(in|cm)', hgt))
        and (150 if m[2] == 'cm' else 59) <= int(m[1]) <= (193 if m[2] == 'cm' else 76)
        and (hcl := p.get('hcl')) and re.fullmatch(r'#[0-9a-f]{6}', hcl)
        and (ecl := p.get('ecl')) and re.fullmatch('(amb|blu|brn|gry|grn|hzl|oth)', ecl)
        and (pid := p.get('pid')) and re.fullmatch(r'\d{9}', pid)
    )
    for p in passports
)
