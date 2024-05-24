from openfisca_core.simulation_builder import SimulationBuilder
from openfisca_country_template import CountryTaxBenefitSystem

# all children minors
# all children depepdent
# citizenship boolean


TEST_CASE = {
    'persons': {
        'Ari': {
            'salary': {'2011-01': 5120}
        },
        'Paulos': {
            'salary': {'2011': 3000}
        },
        'Leila': {},
        'Kostas': {},
        'Maria': {},
        'Javier': {
            'salary': {'2011-01': 30000}
        },
        'Mapushi': {},
        'Amarak': {},
    },
    'households': {
        'household_1': {
            'children': ['Leila', 'Kostas', 'Maria'],
            'parents': ['Ari', 'Paul'],
        },
        'household_2': {'parents': ['Javier']}
    },
}

tax_benefit_system = CountryTaxBenefitSystem()

simulation_builder = SimulationBuilder()
simulation = simulation_builder.build_from_entities(tax_benefit_system, TEST_CASE)

children_benefit = simulation.calculate('children_benefit', '2011-01')

print("households", simulation.household.ids)
print("Children Benefit", children_benefit)