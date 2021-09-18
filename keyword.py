
from pytrends.request import TrendReq


a = input("keyword: ")
# b = trends.build_payload(kw_list=[a])
# data = trends.interest_by_region()
# print(data.sample(50))
trends = TrendReq()

data = trends.trending_searches(pn=a)
print(data.head(11))
