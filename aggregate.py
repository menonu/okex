#!/usr/bin/env python3
import sys
import csv
from collections import defaultdict
from decimal import Decimal
from datetime import datetime

with open(sys.argv[1]) as f:

    d = defaultdict(Decimal)
    r = csv.reader(f)
    next(r)
    for line in r:
        d[line[-1]] += Decimal(line[-4])



time = datetime.utcnow().isoformat(sep=' ')
print('Koinly Date,Amount,Currency,Label')
for k,v in d.items():
    print(f'{time},-{v},{k},margin fee')