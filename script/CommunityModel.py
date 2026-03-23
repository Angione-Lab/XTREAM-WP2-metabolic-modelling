from pathlib import Path
import sys
import cobra
import os
import pycomo
test_model_dir = "Geodiabarretti"
named_models = pycomo.load_named_models_from_dir(test_model_dir)

for model in named_models.values():
    print(model.objective)
single_org_models = []
for name, model in named_models.items():
    print(name)
    single_org_model = pycomo.SingleOrganismModel(model, name)
    single_org_models.append(single_org_model)
community_name = "test_community_model"
com_model_obj = pycomo.CommunityModel(single_org_models, community_name)

# Some metabolites are not allowed to accumulate in the medium.
com_model_obj.model
com_model_obj.summary()
com_model_obj.report()
com_model_obj.save("../Downloads/testcommunity.sbml")

