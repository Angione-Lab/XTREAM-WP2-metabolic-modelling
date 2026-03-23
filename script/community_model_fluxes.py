# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:14:38 2026

@author: U0034546PC
"""
import pycomo
import cobra
pycomo.configure_logger(level="info")
conf = cobra.Configuration()
conf.solver = "gurobi"
conf.processes = 8

com_cobra_model = pycomo.CommunityModel.load("../models/communitypycomofinal.sbml")
print(com_cobra_model.model.optimize())

summary = com_cobra_model.summary()
print(summary)

with com_cobra_model.model:
    fva = com_cobra_model.run_fva(fraction_of_optimum=1., loopless=False)
fva

fba = com_cobra_model.run_fba()
fba.to_csv("../results/community_fba.csv")

max_growth = com_cobra_model.max_growth_rate(return_abundances=True)
max_growth.to_csv("../results/community_max_growth.csv")

