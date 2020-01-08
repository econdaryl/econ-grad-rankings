#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:56:15 2018

@author: m1dbl01
"""

import os
from bs4 import BeautifulSoup
import pandas as pd
from functools import reduce
import subprocess
from pprint import pprint

fields = ["agriculture", "banking", "business", "behavioral", "computation", "competition", "demographics", "development", "econometrics", "education", 
          "productivity", "energy", "entrepreneurship", "environmental", "experimental", "finance", "geography", "growth", "gametheory", "health", "history", "intfinance",
          "indorganization", "trade", "labor", "law", "labormarkets", "inequality", "macro", "micro", "micfin", "migration", "monetary", "neuro", "public", "political", "pubfin",
          "resource", "sports", "transport", "urban", "econ", "student"]
#interest = ["migration", "urban", "labor", "health", "demographics", "education", "inequality", "behavioral", "political", "macro", "micro", "econometrics", "econ", "student"]
path = input('Please enter path where you would like the rankings to be stored.')

interest = []
i = 0
print('Choose your interests from the following fields: ')
print(*fields, sep = "\n")
while 1:
    i+=1
    inter = input('Enter interest %d (Leave blank if complete): '%i)
    if inter=='':
        break
    interest.append(str.lower(inter))
print(interest)


filepath = os.path.join(path, 'page_econ.html')
os.system("wget ''https://ideas.repec.org/top/top.econdept.html'' -O %s" % filepath)

with open("%s" % filepath, encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")
    table = soup.find('table', attrs = {"class":"shorttop"})
    for p in soup("p"):
        p.decompose()
    econ = pd.concat(pd.read_html(str(table)))
    econ.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
    econ.rename(columns = {"Rank":"overall"}, inplace = True)
os.remove('%s' % filepath)

filepath = os.path.join(path, 'page_stu.html')
os.system("wget ''https://ideas.repec.org/top/top.inst.students.html'' -O %s" % filepath)

with open("%s" % filepath, encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")
    table = soup.find('table', attrs = {"class":"shorttop"})
    for p in soup("p"):
        p.decompose()
    stu = pd.concat(pd.read_html(str(table)))
    stu.drop(['Score', 'Students'], axis = 1, inplace = True)
    stu.rename(columns = {"Rank":"student"}, inplace = True)
os.remove('%s' % filepath)

dfs = [econ, stu]

if "agriculture" in interest:
    filepath = os.path.join(path, 'page_agr.html')
    os.system("wget ''https://ideas.repec.org/top/top.agr.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        agr = pd.concat(pd.read_html(str(table)))
        agr.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        agr.rename(columns = {"Rank":"agriculture"}, inplace = True)
    dfs.append(agr)
    os.remove('%s' % filepath)

if "banking" in interest:
    filepath = os.path.join(path, 'page_ban.html')
    os.system("wget ''https://ideas.repec.org/top/top.ban.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        ban = pd.concat(pd.read_html(str(table)))
        ban.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        ban.rename(columns = {"Rank":"banking"}, inplace = True)
    dfs.append(ban)
    os.remove('%s' % filepath)

if "business" in interest:
    filepath = os.path.join(path, 'page_bec.html')
    os.system("wget ''https://ideas.repec.org/top/top.bec.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        bec = pd.concat(pd.read_html(str(table)))
        bec.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        bec.rename(columns = {"Rank":"business"}, inplace = True)
    dfs.append(bec)
    os.remove('%s' % filepath)

if "behavioral" in interest:
    filepath = os.path.join(path, 'page_cbe.html')
    os.system("wget ''https://ideas.repec.org/top/top.cbe.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        cbe = pd.concat(pd.read_html(str(table)))
        cbe.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        cbe.rename(columns = {"Rank":"behavioral"}, inplace = True)
    dfs.append(cbe)
    os.remove('%s' % filepath)

if "computation" in interest:
    filepath = os.path.join(path, 'page_cmp.html')
    os.system("wget ''https://ideas.repec.org/top/top.cmp.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        cmp = pd.concat(pd.read_html(str(table)))
        cmp.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        cmp.rename(columns = {"Rank":"computation"}, inplace = True)
    dfs.append(cmp)
    os.remove('%s' % filepath)

if "competition" in interest:
    filepath = os.path.join(path, 'page_com.html')
    os.system("wget ''https://ideas.repec.org/top/top.com.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        com = pd.concat(pd.read_html(str(table)))
        com.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        com.rename(columns = {"Rank":"competition"}, inplace = True)
    dfs.append(com)
    os.remove('%s' % filepath)

if "demographics" in interest:
    filepath = os.path.join(path, 'page_dem.html')
    os.system("wget ''https://ideas.repec.org/top/top.dem.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        dem = pd.concat(pd.read_html(str(table)))
        dem.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        dem.rename(columns = {"Rank":"demographics"}, inplace = True)
    dfs.append(dem)
    os.remove('%s' % filepath)

if "development" in interest:
    filepath = os.path.join(path, 'page_dev.html')
    os.system("wget ''https://ideas.repec.org/top/top.dev.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        dev = pd.concat(pd.read_html(str(table)))
        dev.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        dev.rename(columns = {"Rank":"development"}, inplace = True)
    dfs.append(dev)
    os.remove('%s' % filepath)

if "econometrics" in interest:
    filepath = os.path.join(path, 'page_ecm.html')
    os.system("wget ''https://ideas.repec.org/top/top.ecm.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        ecm = pd.concat(pd.read_html(str(table)))
        ecm.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        ecm.rename(columns = {"Rank":"econometrics"}, inplace = True)
    dfs.append(ecm)
    os.remove('%s' % filepath)

if "education" in interest:
    filepath = os.path.join(path, 'page_edu.html')
    os.system("wget ''https://ideas.repec.org/top/top.edu.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        edu = pd.concat(pd.read_html(str(table)))
        edu.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        edu.rename(columns = {"Rank":"education"}, inplace = True)
    dfs.append(edu)
    os.remove('%s' % filepath)

if "productivity" in interest:
    filepath = os.path.join(path, 'page_eff.html')
    os.system("wget ''https://ideas.repec.org/top/top.eff.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        eff = pd.concat(pd.read_html(str(table)))
        eff.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        eff.rename(columns = {"Rank":"productivity"}, inplace = True)
    dfs.append(eff)
    os.remove('%s' % filepath)

if "energy" in interest:
    filepath = os.path.join(path, 'page_ene.html')
    os.system("wget ''https://ideas.repec.org/top/top.ene.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        ene = pd.concat(pd.read_html(str(table)))
        ene.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        ene.rename(columns = {"Rank":"energy"}, inplace = True)
    dfs.append(ene)
    os.remove('%s' % filepath)

if "entrepreneurship" in interest:
    filepath = os.path.join(path, 'page_ent.html')
    os.system("wget ''https://ideas.repec.org/top/top.ent.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        ent = pd.concat(pd.read_html(str(table)))
        ent.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        ent.rename(columns = {"Rank":"entrepreneurship"}, inplace = True)
    dfs.append(ent)
    os.remove('%s' % filepath)

if "environmental" in interest:
    filepath = os.path.join(path, 'page_env.html')
    os.system("wget ''https://ideas.repec.org/top/top.env.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        env = pd.concat(pd.read_html(str(table)))
        env.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        env.rename(columns = {"Rank":"environmental"}, inplace = True)
    dfs.append(env)
    os.remove('%s' % filepath)

if "experimental" in interest:
    filepath = os.path.join(path, 'page_exp.html')
    os.system("wget ''https://ideas.repec.org/top/top.exp.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        exp = pd.concat(pd.read_html(str(table)))
        exp.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        exp.rename(columns = {"Rank":"experimental"}, inplace = True)
    dfs.append(exp)
    os.remove('%s' % filepath)

if "finance" in interest:
    filepath = os.path.join(path, 'page_fin.html')
    os.system("wget ''https://ideas.repec.org/top/top.fin.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        fin = pd.concat(pd.read_html(str(table)))
        fin.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        fin.rename(columns = {"Rank":"finance"}, inplace = True)
    dfs.append(fin)
    os.remove('%s' % filepath)

if "geography" in interest:
    filepath = os.path.join(path, 'page_geo.html')
    os.system("wget ''https://ideas.repec.org/top/top.geo.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        geo = pd.concat(pd.read_html(str(table)))
        geo.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        geo.rename(columns = {"Rank":"geography"}, inplace = True)
    dfs.append(geo)
    os.remove('%s' % filepath)

if "growth" in interest:
    filepath = os.path.join(path, 'page_gro.html')
    os.system("wget ''https://ideas.repec.org/top/top.gro.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        gro = pd.concat(pd.read_html(str(table)))
        gro.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        gro.rename(columns = {"Rank":"growth"}, inplace = True)
    dfs.append(gro)
    os.remove('%s' % filepath)

if "gametheory" in interest:
    filepath = os.path.join(path, 'page_gth.html')
    os.system("wget ''https://ideas.repec.org/top/top.gth.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        gth = pd.concat(pd.read_html(str(table)))
        gth.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        gth.rename(columns = {"Rank":"gametheory"}, inplace = True)
    dfs.append(gth)
    os.remove('%s' % filepath)

if "health" in interest:
    filepath = os.path.join(path, 'page_hea.html')
    os.system("wget ''https://ideas.repec.org/top/top.hea.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        hea = pd.concat(pd.read_html(str(table)))
        hea.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        hea.rename(columns = {"Rank":"health"}, inplace = True)
    dfs.append(hea)
    os.remove('%s' % filepath)

if "history" in interest:
    filepath = os.path.join(path, 'page_hpe.html')
    os.system("wget ''https://ideas.repec.org/top/top.hpe.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        hpe = pd.concat(pd.read_html(str(table)))
        hpe.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        hpe.rename(columns = {"Rank":"history"}, inplace = True)
    dfs.append(hpe)
    os.remove('%s' % filepath)

if "intfinance" in interest:
    filepath = os.path.join(path, 'page_ifn.html')
    os.system("wget ''https://ideas.repec.org/top/top.ifn.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        ifn = pd.concat(pd.read_html(str(table)))
        ifn.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        ifn.rename(columns = {"Rank":"intfinance"}, inplace = True)
    dfs.append(ifn)
    os.remove('%s' % filepath)

if "indorganization" in interest:
    filepath = os.path.join(path, 'page_ind.html')
    os.system("wget ''https://ideas.repec.org/top/top.ind.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        ind = pd.concat(pd.read_html(str(table)))
        ind.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        ind.rename(columns = {"Rank":"indorganization"}, inplace = True)
    dfs.append(ind)
    os.remove('%s' % filepath)

if "trade" in interest:
    filepath = os.path.join(path, 'page_int.html')
    os.system("wget ''https://ideas.repec.org/top/top.int.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        intl = pd.concat(pd.read_html(str(table)))
        intl.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        intl.rename(columns = {"Rank":"trade"}, inplace = True)
    dfs.append(intl)
    os.remove('%s' % filepath)

if "labor" in interest:
    filepath = os.path.join(path, 'page_lab.html')
    os.system("wget ''https://ideas.repec.org/top/top.lab.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        lab = pd.concat(pd.read_html(str(table)))
        lab.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        lab.rename(columns = {"Rank":"labor"}, inplace = True)
    dfs.append(lab)
    os.remove('%s' % filepath)

if "law" in interest:
    filepath = os.path.join(path, 'page_law.html')
    os.system("wget ''https://ideas.repec.org/top/top.law.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        law = pd.concat(pd.read_html(str(table)))
        law.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        law.rename(columns = {"Rank":"law"}, inplace = True)
    dfs.append(law)
    os.remove('%s' % filepath)

if "labormarkets" in interest:
    filepath = os.path.join(path, 'page_lma.html')
    os.system("wget ''https://ideas.repec.org/top/top.lma.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        lma = pd.concat(pd.read_html(str(table)))
        lma.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        lma.rename(columns = {"Rank":"labormarkets"}, inplace = True)
    dfs.append(lma)
    os.remove('%s' % filepath)

if "inequality" in interest:
    filepath = os.path.join(path, 'page_ltv.html')
    os.system("wget ''https://ideas.repec.org/top/top.ltv.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        ltv = pd.concat(pd.read_html(str(table)))
        ltv.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        ltv.rename(columns = {"Rank":"inequality"}, inplace = True)
    dfs.append(ltv)
    os.remove('%s' % filepath)

if "micfin" in interest:
    filepath = os.path.join(path, 'page_mfd.html')
    os.system("wget ''https://ideas.repec.org/top/top.mfd.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        mfd = pd.concat(pd.read_html(str(table)))
        mfd.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        mfd.rename(columns = {"Rank":"micfin"}, inplace = True)
    dfs.append(mfd)
    os.remove('%s' % filepath)

if "macro" in interest:
    filepath = os.path.join(path, 'page_mac.html')
    os.system("wget ''https://ideas.repec.org/top/top.mac.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        mac = pd.concat(pd.read_html(str(table)))
        mac.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        mac.rename(columns = {"Rank":"macro"}, inplace = True)
    dfs.append(mac)
    os.remove('%s' % filepath)

if "micro" in interest:
    filepath = os.path.join(path, 'page_mic.html')
    os.system("wget ''https://ideas.repec.org/top/top.mic.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        mic = pd.concat(pd.read_html(str(table)))
        mic.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        mic.rename(columns = {"Rank":"micro"}, inplace = True)
    dfs.append(mic)
    os.remove('%s' % filepath)

if "migration" in interest:
    filepath = os.path.join(path, 'page_mig.html')
    os.system("wget ''https://ideas.repec.org/top/top.mig.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        mig = pd.concat(pd.read_html(str(table)))
        mig.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        mig.rename(columns = {"Rank":"migration"}, inplace = True)
    dfs.append(mig)
    os.remove('%s' % filepath)

if "monetary" in interest:
    filepath = os.path.join(path, 'page_mon.html')
    os.system("wget ''https://ideas.repec.org/top/top.mon.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        mon = pd.concat(pd.read_html(str(table)))
        mon.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        mon.rename(columns = {"Rank":"monetary"}, inplace = True)
    dfs.append(mon)
    os.remove('%s' % filepath)

if "neuro" in interest:
    filepath = os.path.join(path, 'page_pbe.html')
    os.system("wget ''https://ideas.repec.org/top/top.pbe.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        neu = pd.concat(pd.read_html(str(table)))
        neu.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        neu.rename(columns = {"Rank":"neuro"}, inplace = True)
    dfs.append(neu)
    os.remove('%s' % filepath)

if "public" in interest:
    filepath = os.path.join(path, 'page_pbe.html')
    os.system("wget ''https://ideas.repec.org/top/top.pbe.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        pbe = pd.concat(pd.read_html(str(table)))
        pbe.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        pbe.rename(columns = {"Rank":"public"}, inplace = True)
    dfs.append(pbe)
    os.remove('%s' % filepath)

if "political" in interest:
    filepath = os.path.join(path, 'page_pol.html')
    os.system("wget ''https://ideas.repec.org/top/top.pol.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        pol = pd.concat(pd.read_html(str(table)))
        pol.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        pol.rename(columns = {"Rank":"political"}, inplace = True)
    dfs.append(pol)
    os.remove('%s' % filepath)

if "pubfin" in interest:
    filepath = os.path.join(path, 'page_pub.html')
    os.system("wget ''https://ideas.repec.org/top/top.pub.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        pub = pd.concat(pd.read_html(str(table)))
        pub.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        pub.rename(columns = {"Rank":"pubfin"}, inplace = True)
    dfs.append(pub)
    os.remove('%s' % filepath)

if "resource" in interest:
    filepath = os.path.join(path, 'page_res.html')
    os.system("wget ''https://ideas.repec.org/top/top.res.html'' -O %s" % filepath)
    
    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        res = pd.concat(pd.read_html(str(table)))
        res.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        res.rename(columns = {"Rank":"resource"}, inplace = True)
    dfs.append(res)
    os.remove('%s' % filepath)

if "sports" in interest:
    filepath = os.path.join(path, 'page_spo.html')
    os.system("wget ''https://ideas.repec.org/top/top.spo.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        spo = pd.concat(pd.read_html(str(table)))
        spo.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        spo.rename(columns = {"Rank":"sports"}, inplace = True)
    dfs.append(spo)
    os.remove('%s' % filepath)

if "transport" in interest:
    filepath = os.path.join(path, 'page_tre.html')
    os.system("wget ''https://ideas.repec.org/top/top.tre.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        tre = pd.concat(pd.read_html(str(table)))
        tre.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        tre.rename(columns = {"Rank":"transport"}, inplace = True)
    dfs.append(tre)
    os.remove('%s' % filepath)

if "urban" in interest:
    filepath = os.path.join(path, 'page_ure.html')
    os.system("wget ''https://ideas.repec.org/top/top.ure.html'' -O %s" % filepath)

    with open("%s" % filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find('table', attrs = {"class":"shorttop"})
        for p in soup("p"):
            p.decompose()
        ure = pd.concat(pd.read_html(str(table)))
        ure.drop(['Score', 'Authors', 'Author shares'], axis = 1, inplace = True)
        ure.rename(columns = {"Rank":"urban"}, inplace = True)
    dfs.append(ure)
    os.remove('%s' % filepath)
    
os.chdir('%s' % path)
finalpath = os.path.join(path, 'rankings.csv')
df_final = reduce(lambda left,right: pd.merge(left,right,on='Institution', how = 'outer'), dfs)
df_final.to_csv("%s" % finalpath, index = False)

dofile = "grad.do"
cmd = ["stata", "do", dofile]

subprocess.call(cmd)
