#try:
#    from galapagos.api.metadata import PopulationMetadata
#    from galapagos.api.metadata import TournamentSelectionMetadata
#except ModuleNotFoundError:
import sys
sys.path.append('..')
from galapagos.api.metadata import PopulationMetadata
from galapagos.api.metadata import ChromosomeMetadata
#sys.path.append('..')

def population_metadata_test():
    population_metadata = PopulationMetadata()
    population_metadata.survival_rate = .25
    print(population_metadata.survival_rate)

def chromosome_metadata_test():
    chromosome_metadata = ChromosomeMetadata()
    chromosome_metadata.name = "test"
    print(chromosome_metadata.name)

#population_metadata_test()
chromosome_metadata_test()
