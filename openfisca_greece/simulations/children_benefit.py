from openfisca_core.simulation_builder import SimulationBuilder
from openfisca_greece import CountryTaxBenefitSystem

# all children minors
# all children depepdent
# citizenship boolean


TEST_CASE = {
    'persons': {
        'Ari': {
            'categ_of_citizenship' : { '2019': 'Έλληνας πολίτης' },
            'tax_years':{ '2019': 5 }
            },
        'Paulos': {
            'categ_of_citizenship' : { '2019': 'Πολίτης άλλου κράτους' },
            'tax_years':{ '2019': 15 }
            },
        'Leila': {
            'birth': {'ETERNITY': '2005-01-15'},
            'marital_status_child' : { '2019': True },
            'disability_status' : { '2019': False },
            'study_status' : { '2019': 'Μαθητής' }
            },
        'Kostas': {
            'birth': {'ETERNITY': '2005-01-15'},
            'marital_status_child' : { '2019': True },
            'disability_status' : { '2019': False },
            'study_status' : { '2019': 'Μαθητής' }
            },
        'Maria': {
            'birth': {'ETERNITY': '2005-01-15'},
            'marital_status_child' : { '2019': True },
            'disability_status' : { '2019': False },
            'study_status' : { '2019': 'Μαθητής' }
            },
        'Mara': {
            'categ_of_citizenship' : { '2019': 'Πολίτης άλλου κράτους' },
            'tax_years':{ '2019': 6 }
            },
        'Javier': {
            'categ_of_citizenship' : { '2019': 'Πολίτης άλλου κράτους' },
            'tax_years':{ '2019': 16 }
            },
        'Mapushi': {
            'birth': {'ETERNITY': '2005-01-15'},
            'marital_status_child' : { '2019': True },
            'disability_status' : { '2019': False },
            'study_status' : { '2019': 'Μαθητής' }
            },
        'Amarak': {
            'birth': {'ETERNITY': '2005-01-15'},
            'marital_status_child' : { '2019': True },
            'disability_status' : { '2019': False },
            'study_status' : { '2019': 'Μαθητής' }
            },
        'Amaraki': {
            'birth': {'ETERNITY': '2000-12-25'},
            'marital_status_child' : { '2019': True },
            'disability_status' : { '2019': False },
            'study_status' : { '2019': 'Φοιτητής' }
            },
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
        },
        'family_3': {
            'parents': ['Mara'],
            'children': ['Amaraki'],
            'family_income': {
                '2019': 10000,
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
citizenship = simulation.calculate('child_benefit_citizenship', '2019')
dependent_children = simulation.calculate('dependent_children', '2019')

print("child_benefit_citizenship", citizenship)
print("dependent_children", dependent_children)
print("eq_scale", eq_scale)
print("eq_income", eq_income)
print("eq_income_scale", eq_income_scale)
print("children_benefit", children_benefit)