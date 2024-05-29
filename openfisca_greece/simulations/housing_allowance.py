from openfisca_core.simulation_builder import SimulationBuilder
from openfisca_greece import CountryTaxBenefitSystem

TEST_CASE = {
    'persons': {
        'Ari': {
            'salary': {'2011-01': 1000} # from date 2011-01 to now, the salary is 1000
        },
        'Paul': {},
        'Leila': {},
        'Kostas': {},
        'Maria': {},
        'Javier': {
            'salary': {'2011-01': 3000}
        }
    },
    'households': {
        'household_1': {
            'children': ['Leila'],
            'parents': ['Ari', 'Paul'],
            'rent': {'1970-01': 300, '2011-01': 300} # double entries to test, that the latest entry is taken into account
        },
        'household_2': {'parents': ['Javier'], 'rent': {'2011-01': 500}}
    },
}

tax_benefit_system = CountryTaxBenefitSystem()

simulation_builder = SimulationBuilder()
simulation = simulation_builder.build_from_entities(tax_benefit_system, TEST_CASE)

housing_allowance = simulation.calculate('housing_allowance', '2011-01')

print("households", simulation.household.ids)
print("housing_allowance", housing_allowance)