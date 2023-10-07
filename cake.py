cake1 = "bf"
cake2 = "vc"
cake3 = "cc"

mc1 = 150
mc2 = 170
mc3 = 180

t_c = 40

tc_mc1 = mc1+t_c
tc_mc2 = mc2+t_c
tc_mc3 = mc3+t_c

uc1 = (tc_mc1 *5)/100
uc2 = (tc_mc2 *5)/100
uc3 = (tc_mc3 *5)/100

s_c = 30

st_c = 40

total_c1 = tc_mc1+uc1+s_c+st_c
total_c2 = tc_mc2+uc2+s_c+st_c
total_c3 = tc_mc3+uc3+s_c+st_c

print(total_c1,total_c2,total_c3)

d_c1 = (800*8)/100
d_c2 = (850*10)/100
d_c3 = (900*12)/100
print(d_c1,d_c2,d_c3)
ad_c1 = (800-64)
ad_c2 = (850-85)
ad_c3 = (900-108)
print(ad_c1,ad_c2,ad_c3)
ts_c1 = (736*5)
ts_c2 = (765*12)
ts_c3 = (792*12)
print(ts_c1,ts_c2,ts_c3)

p_c1 = (736-269.5)
p_c2 = (765-290.5)
p_c3 = (792-301)
print(p_c1,p_c2,p_c3)
totals_c = ts_c1+ts_c2+ts_c3
print(totals_c)
