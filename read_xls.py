import sys
import io
import os

# Force UTF-8 output
os.environ['PYTHONIOENCODING'] = 'utf-8'
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import pandas as pd
import numpy as np

df = pd.read_excel(r'C:\Users\Mgbot\Downloads\society-of-amercian-military-engineers-san-francisco-post_content_1771194457360.xls', sheet_name='All posts', header=1)
df.columns = ['title','link','type','campaign','posted_by','created','camp_start','camp_end','audience','impressions','views','offsite','clicks','ctr','likes','comments','reposts','follows','engagement','content_type']

print('Shape:', df.shape)
print()

for i in range(5):
    row = df.iloc[i]
    title = str(row['title'])[:100] if pd.notna(row['title']) else 'NaN'
    # Replace non-ascii for safe printing
    title_safe = title.encode('ascii', 'replace').decode('ascii')
    print(f'Row {i}: type={row["type"]}, created={row["created"]}, posted_by={row["posted_by"]}, impressions={row["impressions"]}, likes={row["likes"]}, comments={row["comments"]}, reposts={row["reposts"]}')
    print(f'  title: {title_safe}')
    print(f'  link: {row["link"]}')
    print()

nan_count = df['title'].isna().sum()
empty_count = (df['title'] == '').sum()
print(f'NaN titles: {nan_count}, Empty titles: {empty_count}')
print(f'Total rows: {len(df)}')
print(f'Valid rows: {len(df) - nan_count - empty_count}')
print()

print('Unique types:', df['type'].unique().tolist())
print('Unique posted_by:', df['posted_by'].unique().tolist())
print('Created range:', df['created'].min(), 'to', df['created'].max())
print()

print('Impressions range:', df['impressions'].min(), '-', df['impressions'].max())
print('Likes range:', df['likes'].min(), '-', df['likes'].max())
