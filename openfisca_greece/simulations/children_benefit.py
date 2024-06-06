from openfisca_core.simulation_builder import SimulationBuilder
from openfisca_greece import CountryTaxBenefitSystem

# all children minors
# all children depepdent
# citizenship boolean


TEST_CASE = {
    'persons': {
        'Ari': {},
        'Paulos': {},
        'Leila': {},
        'Kostas': {},
        'Maria': {},
        'Javier': {},
        'Mapushi': {},
        'Amarak': {},
    },
    'families': {
        'family_1': {
            'children': ['Leila', 'Kostas', 'Maria'],
            'parents': ['Ari', 'Paulos'],
            'family_income': {
                '2019': 10000,
            },
        },
        'family_2': {
            'parents': ['Javier'],
            'children': ['Mapushi', 'Amarak'],
            'family_income': {
                '2019': 16000,
            },
        }
    },
}

tax_benefit_system = CountryTaxBenefitSystem()

simulation_builder = SimulationBuilder()
simulation = simulation_builder.build_from_entities(tax_benefit_system, TEST_CASE)

children_benefit = simulation.calculate('children_benefit', '2019')
eq_income = simulation.calculate('eq_income', '2019')
eq_income_scale = simulation.calculate('eq_income_scale', '2019')
eq_scale = simulation.calculate('eq_scale', '2019')

print("eq_scale", eq_scale)
print("eq_income", eq_income)
print("eq_income_scale", eq_income_scale)
print("children_benefit", children_benefit)