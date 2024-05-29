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
                '2011': 10000,
            },
        },
        'family_2': {
            'parents': ['Javier'],
            'children': ['Mapushi', 'Amarak'],
            'family_income': {
                '2011': 16000,
            },
        }
    },
}

tax_benefit_system = CountryTaxBenefitSystem()

simulation_builder = SimulationBuilder()
simulation = simulation_builder.build_from_entities(tax_benefit_system, TEST_CASE)

children_benefit = simulation.calculate('children_benefit', '2011')

print("children_benefit", children_benefit)