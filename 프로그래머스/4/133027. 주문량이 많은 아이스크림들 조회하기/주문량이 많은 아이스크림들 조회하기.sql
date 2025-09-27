-- 코드를 입력하세요
SELECT fh.FLAVOR
from FIRST_HALF as fh
join (select j.FLAVOR,sum(j.TOTAL_ORDER) as TOTAL_ORDER from JULY j group by j.flavor) as j
on j.FLAVOR=fh.FLAVOR
order by j.TOTAL_ORDER+fh.TOTAL_ORDER DESC
limit 3
